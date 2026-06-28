import sys
from pathlib import Path
from MetadataCleaner import clean_file

def main():
	# sys.argv[0] is always "MetadataCLeaner.exe"
	# if sys.argv = ["MetadataCleaner.exe"] -> len(sys.argv) == 1
	if len(sys.argv) < 2:
		print("No files provided")
		return

	for file_path in sys.argv[1:]:
		path = Path(file_path)

		if path.is_file():
			clean_file(path)

		if path.is_dir():
			for file in path.iterdir():
				if file.is_file():
					clean_file(file)


if __name__ == "__main__":
    main()