import os
import re
import eyed3
import zipfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

surahs = [
    "001-al-fatiha-(the-opening)",
    "002-al-baqara-(the-cow)",
    "003-aali-imran-(the-family-of-imran)",
    "004-an-nisa'-(the-women)",
    "005-al-ma'idah-(the-table-spread)",
    "006-al-an'am-(the-cattle)",
    "007-al-a'raf-(the-heights)",
    "008-al-anfal-(the-spoils-of-war)",
    "009-at-tawbah-(the-repentance)",
    "010-yunus-(jonah)",
    "011-hud-(hud)",
    "012-yusuf-(joseph)",
    "013-ar-ra'd-(the-thunder)",
    "014-ibrahim-(abraham)",
    "015-al-hijr-(the-rocky-tract)",
    "016-an-nahl-(the-bee)",
    "017-al-isra'-(the-night-journey)",
    "018-al-kahf-(the-cave)",
    "019-maryam-(mary)",
    "020-ta-ha-(ta-ha)",
    "021-al-anbiya-(the-prophets)",
    "022-al-hajj-(the-pilgrimage)",
    "023-al-mu'minun-(the-believers)",
    "024-an-nur-(the-light)",
    "025-al-furqan-(the-criterion)",
    "026-ash-shu'ara-(the-poets)",
    "027-an-naml-(the-ant)",
    "028-al-qasas-(the-stories)",
    "029-al-ankabut-(the-spider)",
    "030-ar-rum-(the-romans)",
    "031-luqman-(luqman)",
    "032-as-sajda-(the-prostration)",
    "033-al-ahzab-(the-combined-forces)",
    "034-saba'-(sheba)",
    "035-fatir-(the-originator)",
    "036-ya-sin-(ya-sin)",
    "037-as-saffat-(those-who-set-the-ranks)",
    "038-sad-(the-letter-sad)",
    "039-az-zumar-(the-troops)",
    "040-ghafir-(the-forgiver)",
    "041-fussilat-(explained-in-detail)",
    "042-ash-shura-(the-consultation)",
    "043-az-zukhruf-(the-gold-adornments)",
    "044-ad-dukhan-(the-smoke)",
    "045-al-jathiya-(the-crouching)",
    "046-al-ahqaf-(the-wind-curved-sandhills)",
    "047-muhammad-(muhammad)",
    "048-al-fath-(the-victory)",
    "049-al-hujurat-(the-rooms)",
    "050-qaf-(the-letter-qaf)",
    "051-adh-dhariyat-(the-winnowing-winds)",
    "052-at-tur-(the-mount)",
    "053-an-najm-(the-star)",
    "054-al-qamar-(the-moon)",
    "055-ar-rahman-(the-beneficent)",
    "056-al-waqi'a-(the-inevitable)",
    "057-al-hadid-(the-iron)",
    "058-al-mujadila-(the-pleading-woman)",
    "059-al-hashr-(the-exile)",
    "060-al-mumtahina-(she-that-is-to-be-examined)",
    "061-as-saff-(the-ranks)",
    "062-al-jumu'a-(the-congregation)",
    "063-al-munafiqun-(the-hypocrites)",
    "064-at-taghabun-(the-mutual-disillusion)",
    "065-at-talaq-(the-divorce)",
    "066-at-tahrim-(the-prohibition)",
    "067-al-mulk-(the-sovereignty)",
    "068-al-qalam-(the-pen)",
    "069-al-haaqqa-(the-reality)",
    "070-al-ma'arij-(the-ascending-stairways)",
    "071-nuh-(noah)",
    "072-al-jinn-(the-jinn)",
    "073-al-muzzammil-(the-enshrouded-one)",
    "074-al-muddathir-(the-cloaked-one)",
    "075-al-qiyama-(the-resurrection)",
    "076-al-insan-(man)",
    "077-al-mursalat-(the-emissaries)",
    "078-an-naba-(the-announcement)",
    "079-an-nazi'at-(those-who-drag-forth)",
    "080-abasa-(he-frowned)",
    "081-at-takwir-(the-overthrowing)",
    "082-al-infitar-(the-cleaving)",
    "083-al-mutaffifin-(defrauding)",
    "084-al-inshiqaq-(the-splitting-open)",
    "085-al-burooj-(the-mansions-of-the-stars)",
    "086-at-tariq-(the-morning-star)",
    "087-al-ala-(the-most-high)",
    "088-al-ghashiya-(the-overwhelming)",
    "089-al-fajr-(the-dawn)",
    "090-al-balad-(the-city)",
    "091-ash-shams-(the-sun)",
    "092-al-lail-(the-night)",
    "093-adh-dhuhaa-(the-morning-hours)",
    "094-ash-sharh-(the-relief)",
    "095-at-tin-(the-fig)",
    "096-al-alaq-(the-clot)",
    "097-al-qadr-(the-power)",
    "098-al-bayyina-(the-clear-proof)",
    "099-az-zalzalah-(the-earthquake)",
    "100-al-adiyat-(the-chargers)",
    "101-al-qari'a-(the-striking-hour)",
    "102-at-takathur-(the-piling-up)",
    "103-al-asr-(the-time)",
    "104-al-humazah-(the-slanderer)",
    "105-al-fil-(the-elephant)",
    "106-quraish-(quraish)",
    "107-al-ma'un-(kindness)",
    "108-al-kawthar-(abundance)",
    "109-al-kafirun-(the-disbelievers)",
    "110-an-nasr-(the-help)",
    "111-al-masad-(the-palm-fiber)",
    "112-al-ikhlas-(the-sincerity)",
    "113-al-falaq-(the-daybreak)",
    "114-an-nas-(mankind)"
]

def make_chrome_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    prefs = {'download.default_directory': download_dir}
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
    num_of_iterations = max(1, int(max_time_to_wait / 5))

    for _ in range(num_of_iterations):
        time.sleep(10)
        if not any(".crdownload" in file for file in os.listdir(download_dir)):
            print("All files downloaded!")
            return True

    print("All files not downloaded!")
    return False

def export_file():
    files = os.listdir(download_dir)

    for file in files:
        absolute_path = os.path.join(download_dir, file)
        if zipfile.is_zipfile(absolute_path):
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

def rename_files_in_directory(directory, new_names):
    mp3_files = [file for file in os.listdir(directory) if file.endswith(".mp3")]

    if len(mp3_files) != len(new_names):
        print("Error: Number of files and names in the list do not match.")
    else:
        for i, mp3_file in enumerate(mp3_files):
            mp3_path = os.path.join(directory, mp3_file)
            audiofile = eyed3.load(mp3_path)
            audiofile.tag.title = new_names[i]
            audiofile.tag.save()
            print(f"Updated metadata for '{mp3_file}' to '{new_names[i]}'")

def main():
    global download_dir, unzip_dir
    download_dir = input("Enter the download directory path: ")

    while True:
        url = input("Enter a URL (or 'q' to quit): ")
        if url == 'q':
            break

        url_name = re.sub(r'[^a-zA-Z0-9]', '_', url)
        directory_name = url_name.split("/")[-1]
        download_dir = os.path.join(download_dir, directory_name)

        try:
            for i in range(1, 115):
                driver = make_chrome_driver()
                driver.get(url)
                find_element(driver, By.XPATH, f'//*[@id="ul-play-list"]/li[{i}]/div[1]/div[2]/a/i').click()
                print('Clicked download button')
                find_element(driver, By.ID, 'modal3dnw').click()
                print('Clicked Final BIG download button')
                surah_name = find_element(driver, By.XPATH, f'//*[@id="ul-play-list"]/li[{i}]/div[1]/a/span').text
                print("Downloaded surah:", surah_name)
                time.sleep(10)
                driver.quit()
            check_files_finished_downloading(download_dir, 120)
            export_file()
            rename_files_in_directory(download_dir, surahs)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    unzip_dir = os.getcwd()
    main()