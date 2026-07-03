from PIL import Image, ExifTags, UnidentifiedImageError
from pathlib import Path

def read_file(path):
	with Image.open(path) as img:
		exif = img.getexif()

	if not exif:
		return f"No metadata found in {path.name}"

	msg = f"EXIF metadata for {path.name}:\n"

	for tag_id, value in exif.items():
		tag_name = ExifTags.TAGS.get(tag_id, tag_id)

		if tag_name == "GPSInfo":
			continue

		msg += f"{tag_name}:{value}\n"


	gps_info = exif.get(ExifTags.IFD.GPSInfo)

	if gps_info:
		msg += "\nGPS metadata:\n"

		for tag_id, value in gps_info.items():
			tag_name = ExifTags.GPSTAGS.get(tag_id, tag_id)
			msg += f'{tag_name}: {value}'

	else:
		msg += "\nNo GPS metadata found"

	return msg
				

		
# Creates a new copy of the image without embedded metadata such as EXIF information.
def clean_file(path):
	try:
		# PIL filters non-image files
		with Image.open(path) as img:
			message = f"{path} recognized as a valid {img.format} image."

			# Create a new image without EXIF metadata
			clean_img = Image.new(img.mode, img.size)
			clean_img.putdata(img.getdata())

			output_folder = path.parent / "clean_files"
			output_folder.mkdir(exist_ok=True)

			output_path = output_folder / f"{path.stem}_clean{path.suffix}"

			if output_path.exists():
				return f"{output_path} already exists, skipping process"

			clean_img.save(output_path, format=img.format)

			return f"{message} Metadata stripped from {path.name}."

	except (UnidentifiedImageError, OSError) as e:
		return f"{path} is not a valid image file: {e}"



