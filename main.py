import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from ImageEXIFCleaner import clean_file, read_file


class ImageEXIFCleanerApp:
	def __init__(self):
		self.window = tk.Tk()
		self.output = tk.Text(self.window)


	def create_interface(self):
		self.window.title("Image EXIF Cleaner")
		self.window.geometry("500x300")

		button_frame = tk.Frame(self.window)
		button_frame.pack(pady=10)

		button_clean = tk.Button(
			button_frame,
			text="Remove EXIF",
			command= self.select_files_for_cleaning,
			width=15
			)

		button_clean.grid(row=0, column=0, padx=10)

		button_read = tk.Button(
			button_frame,
			text="Read EXIF",
			command= self.select_files_for_reading,
			width=15
			)

		button_read.grid(row=0, column=1, padx=10)

		#output = tk.Text(window)
		self.output.pack(expand=True, fill="both")


	def select_files_for_cleaning(self):
		files = filedialog.askopenfilenames(
			title="Select files for cleaning"
			)

		for file in files:
			result = clean_file(Path(file))
			self.output.insert(tk.END, result + "\n")


	def select_files_for_reading(self):
		files = filedialog.askopenfilenames(
			title="Select files for reading"
			)

		for file in files:
			result = read_file(Path(file))
			self.output.insert(tk.END, result + "\n")


	def runloop(self):
		self.window.mainloop()


def main():
	app = ImageEXIFCleanerApp()

	app.create_interface()
	app.runloop()


if __name__ == "__main__":
    main()