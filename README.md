## Overview
This repository contains a Python script named `main.py`, designed to download Quranic audio files from www.assabile.com. The script automates web browsing and file management tasks to retrieve and organize audio files for various reciters and collections.

### `main.py`
#### Purpose
`main.py` is a script for downloading Quranic audio files from www.assabile.com. It utilizes the Selenium library to automate web interactions and file handling.

#### Requirements
- Python 3.x
- Selenium library
- Chrome WebDriver (or compatible browser driver)

#### Usage
1. Clone the repository or download `main.py`.
2. Install the required dependencies if not already installed, including Python 3.x and the Selenium library.
3. Run the script using the `python3 main.py` command.
4. Provide the download directory path and the URL of the website containing the audio files when prompted.

Example:
```bash
python3 main.py
Enter the download directory path: /home/aio-pc/Downloads
Enter a URL (or 'q' to quit): https://www.assabile.com/nadir-al-qallawi-765/collection/al-mus-haf-al-murattal-3329
Clicked download button
Clicked Final BIG download button
Downloaded surah: Al-Fatiha
Clicked download button
Clicked Final BIG download button
Downloaded surah: Al-Baqara
Clicked download button
Clicked Final BIG download button
Downloaded surah: Aal-e-Imran
All files not downloaded!
nadir-al-qallawi-002-al-baqara-108626-9176.zip.crdownload is not a zip file.
Unzipped File: nadir-al-qallawi-001-al-fatiha-108627-3383.zip to /path/to/your/download/directory
nadir-al-qallawi-003-al-i-mran-108625-1506.zip.crdownload is not a zip file.
done!
```

1. The downloaded files will be organized, and their metadata will be updated with Surah names from the Quran.

2. The script provides feedback on the progress and any errors encountered during the process.
