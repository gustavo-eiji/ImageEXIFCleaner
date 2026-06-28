# Image Metadata Cleaner

A lightweight Python-based utility that removes image metadata (EXIF) from files while preserving the original image content.

It is designed to be simple for non-technical users: just run the program or drag-and-drop images onto the executable.

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

Original files are never modified.

---

## Usage

### Option 1: Drag & Drop (recommended)

After building the `.exe`:

- Drag image files onto `MetadataCleaner.exe`
- A folder named clean_images containing the processed images will be created.