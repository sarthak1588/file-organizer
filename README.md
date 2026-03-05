# File Organizer

A simple Python script that automatically organizes files in a folder by their file type.

---

## Overview

File Organizer is a Python utility that scans a directory and sorts files into categorized folders based on their extensions.
It helps keep folders clean and organized by automatically separating files like images, documents, videos, and audio.

---

## Features

* Automatically detects file types
* Organizes files into categorized folders
* Creates folders if they do not already exist
* Simple and lightweight script
* Works with common file formats

---

## Technologies Used

* Python 3
* `os` module
* File handling

---

## File Categories

The script organizes files into folders such as:

* Images
* Documents
* Videos
* Audio
* Archives
* Others

---

## How It Works

1. The script scans all files in the target directory.
2. It checks the extension of each file.
3. Based on the extension, the file is moved into a specific folder.

Example:

Before running the script

Downloads/
photo.jpg
notes.pdf
video.mp4

After running the script

Downloads/
Images/photo.jpg
Documents/notes.pdf
Videos/video.mp4

---

## How to Run

Clone the repository:

git clone https://github.com/sarthak1588/file-organizer.git

Navigate to the folder:

cd file-organizer

Run the script:

python file_organizer.py

---

## Example Use Case

If you download many files into one folder, running this script will automatically organize them into different categories.

---

## Future Improvements

* Add a graphical user interface (GUI)
* Allow users to define custom categories
* Schedule automatic organization
* Support more file extensions

---

## Author

**Sarthak Semwal**

GitHub: https://github.com/sarthak1588
