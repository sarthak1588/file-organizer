import os
import shutil

source_folder = "test_folder"

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".mkv"],
    "audio": [".mp3", ".wav"]
}

files = os.listdir(source_folder)

for file in files:
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):

                destination_folder = os.path.join(source_folder, folder)
                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(destination_folder, file))

                print(f"Moved {file} → {folder}")
                break

print("File organization complete!")