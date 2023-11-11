import os
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def make_chrome_driver():
  options = Options()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')

  prefs = {'download.default_directory': "/home/aio-pc/Downloads"}
  options.add_experimental_option('prefs', prefs)

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  return driver

def find_element(driver: webdriver, type: By, xpath: str) -> webdriver:
  try:
    return WebDriverWait(driver, 60).until(
      EC.element_to_be_clickable((type, xpath))
    )
  except TimeoutException as e:
    print(f"TimeoutException: {e}")
    return None 

def clear_directory(directory_path):
  try:
    for filename in os.listdir(directory_path):
      file_path = os.path.join(directory_path, filename)
      if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Removed file: {file_path}")
    print(f"Directory cleared: {directory_path}")
  except OSError as e:
    print(f"Error clearing directory: {directory_path} - {e}")

def check_files_finished_downloading(download_dir: str, max_time_to_wait: int) -> bool:
    """Check if files have finished downloading. Files in progress have an extension of .crdownload.
    
    Args:
        download_dir (str): Directory where files are being downloaded.
        max_time_to_wait (int): Maximum amount of time this function should wait for.
        logger (logging.Logger): Logger for logging messages.

    Returns:
        bool: True on successful download and False if still downloading.
    """
    num_of_iterations = max(1, int(max_time_to_wait / 5))  # Ensure at least one iteration

    for _ in range(num_of_iterations):
        time.sleep(10)
        if not any(".crdownload" in file for file in os.listdir(download_dir)):
            print("All files downloaded!")
            print(download_dir)
            return True

    print("All files not downloaded!")
    return False


urls = [
  'https://www.assabile.com/nadir-al-qallawi-765/collection/quran-recitations-with-translation-english-3330',
  'https://www.assabile.com/nadir-al-qallawi-765/collection/al-mus-haf-al-murattal-3329',
]

directories = [
  "/home/aio-pc/Desktop/Translations",
  "/home/aio-pc/Desktop/Arabic",
]

counter = 0

for url, directory in zip(urls, directories):
  try:
    for i in range(1, 115):
      driver = make_chrome_driver()
      driver.get(url)
      find_element(driver, By.XPATH, f'//*[@id="ul-play-list"]/li[{i}]/div[1]/div[2]/a/i').click()
      print('Clicked download button')
      find_element(driver, By.ID, 'modal3dnw').click()
      print('Clicked Final BIG download button')
      surah_name = find_element(driver, By.XPATH, f'//*[@id="ul-play-list"]/li[{i}]/div[1]/a/span').text
      print("""Downloaded surah: """, surah_name)
      time.sleep(10)
      driver.quit()

      counter += 1
      print(counter)

    download_dir = os.path.abspath("/home/aio-pc/Downloads")
    check_files_finished_downloading(download_dir, 120)
    files = os.listdir(download_dir)
    unzip_dir = directory

    for file in files:
      absolute_path = os.path.join(download_dir, file)
      with zipfile.ZipFile(absolute_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)
        print(f"Unzipped File: {file} to {unzip_dir}")
      # os.remove(absolute_path)

    print('DONE...')

  finally:
    pass
    