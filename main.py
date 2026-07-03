import tkinter as tk
from tkinter import filedialog
import sys
from pathlib import Path
from ImageEXIFCleaner import clean_file, read_file

def select_files_for_cleaning():
	files = filedialog.askopenfilenames(
		title="Select files for cleaning"
		)

	for file in files:
		result = clean_file(Path(file))
		output.insert(tk.END, result + "\n")

def select_files_for_reading():
	files = filedialog.askopenfilenames(
		title="Select files for reading"
		)

	for file in files:
		result = read_file(Path(file))
		output.insert(tk.END, result + "\n")


window = tk.Tk()
window.title("Image EXIF Cleaner")
window.geometry("500x300")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

button_clean = tk.Button(
	button_frame,
	text="Remove EXIF",
	command=select_files_for_cleaning,
	width=15
	)

button_clean.grid(row=0, column=0, padx=10)

button_read = tk.Button(
	button_frame,
	text="Read EXIF",
	command=select_files_for_reading,
	width=15
	)

button_read.grid(row=0, column=1, padx=10)

output = tk.Text(window)
output.pack(expand=True, fill="both")

window.mainloop()

'''
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
'''


if __name__ == "__main__":
    main()