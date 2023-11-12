import os
import zipfile

def export_file():
    download_dir = os.path.abspath("/home/aio-pc/Downloads")
    unzip_dir = "/home/aio-pc/Desktop/Arabic"
    files = os.listdir(download_dir)

    for file in files:
        absolute_path = os.path.join(download_dir, file)
        if zipfile.is_zipfile(absolute_path):  # Check if it's a zip file
            try:
                with zipfile.ZipFile(absolute_path, 'r') as zip_ref:
                    zip_ref.extractall(unzip_dir)
                    print(f"Unzipped File: {file} to {unzip_dir}")
                os.remove(absolute_path)
            except Exception as e:
                print(f"An error occurred while processing {file}: {e}")
        else:
            print(f"{file} is not a zip file.")
    print("done!")

export_file()