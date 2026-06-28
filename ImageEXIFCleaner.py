from PIL import Image, UnidentifiedImageError
from pathlib import Path

def clean_file(path):
	try:
		# PIL filters non-image files
		with Image.open(path) as img:
			print(f"{path} recognized as a valid {img.format} image")

			# Create a new image without EXIF metadata
			clean_img = Image.new(img.mode, img.size)
			clean_img.putdata(img.getdata())

			output_folder = path.parent / "clean_files"
			output_folder.mkdir(exist_ok=True)

			output_path = output_folder / f"{path.stem}_clean{path.suffix}"

			if output_path.exists():
				print(f"{output_path} already exists, skipping process")
				return

			clean_img.save(output_path, format=img.format)

	except (UnidentifiedImageError, OSError) as e:
		print(f"{path} is not a valid image file: {e}")



