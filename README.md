# Image Metadata Cleaner

A lightweight Python-based utility that removes image metadata (EXIF) from files while preserving the original image content.

Includes a native desktop GUI built with Tkinter designed to be friendly for non-technical users.

The project was developed as a learning exercise in Python software development, covering image processing, GUI development, file handling, and application packaging.



---

## Download

You can download the latest Windows executable from the **Releases** page.

[Download latest release](https://github.com/gustavo-eiji/ImageEXIFCleaner/releases)

---

## Features

- Removes EXIF metadata from images
- Supports common formats via Pillow:
  - JPEG
  - PNG
  - WEBP
  - BMP
  - TIFF
- Preserves image pixel data
- Automatically creates an output folder
- Safe handling of invalid/corrupt files

---

## How it works

The program:
1. Reads an image file
2. Rebuilds it without metadata
3. Saves a cleaned copy in a `clean_files/` folder

Original files are never modified. This process removes embedded metadata such as EXIF information without altering the visible image.

---

## Usage

### Remove Metadata
1. Launch the application.
2. Click Remove EXIF.
3. Select one or more images.
4. Cleaned copies are saved in a clean_files folder next to the originals.

### Read Metadata
1. Launch the application.
2. Click Read EXIF.
3. Select one or more images.
4. The detected metadata is displayed inside the application.