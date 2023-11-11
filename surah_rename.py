import os
import re

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

def rename_files_in_directories(*directories):
    for directory in directories:
        for filename in os.listdir(directory):
            original_path = os.path.join(directory, filename)

            match = re.search(r'^[^-]+-[^-]+-[^-]+-([^-.]+)', filename)
            if match:
                new_filename = f"{match.group(1)}.mp3"
                new_path = os.path.join(directory, new_filename)

                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} to {new_path}")
            else:
                print(f"File does not match the expected pattern: {original_path}")

def rename_files_to_surah_names(directory, surahs_list):
    for filename in os.listdir(directory):
        original_path = os.path.join(directory, filename)

        match = re.search(r'^(\d+)', filename)
        if match:
            surah_index = int(match.group(1))
            if 0 < surah_index <= len(surahs_list):
                new_filename = f"{surahs_list[surah_index - 1]}.mp3"
                new_path = os.path.join(directory, new_filename)

                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} to {new_path}")
            else:
                print(f"Invalid surah index for file: {original_path}")
        else:
            print(f"File does not match the expected pattern: {original_path}")

download_dir = "/home/aio-pc/Desktop/"
translation_dir = os.path.join(download_dir, "Translations")
arabic_dir = os.path.join(download_dir, "Arabic")

rename_files_in_directories(translation_dir, arabic_dir)
rename_files_to_surah_names(translation_dir, surahs)
rename_files_to_surah_names(arabic_dir, surahs)
