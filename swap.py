# a = [23, 65, 19, 90]

# # Swap elements at index 1 and index 3
# a[1], a[3] = a[3], a[1]

# print(a)


from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome() 
url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_"
driver.get(url)

try:
    all_languages_button = driver.find_element(By.XPATH, "//button[contains(text(), 'All Languages')]")
    all_languages_button.click()
    time.sleep(2)
except:
    print("All Languages button not found or already selected.")
while True:
    try:
        load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load more')]")
        load_more_button.click()
        time.sleep(2)
    except:
        break
soup = BeautifulSoup(driver.page_source, "html.parser")
song_links = [a['href'] for a in soup.select("a[href*='/song/']")]

aditya_music_count = 0

for song_link in song_links:
    driver.get("https://www.jiosaavn.com" + song_link)
    time.sleep(2) 

    song_soup = BeautifulSoup(driver.page_source, "html.parser")
    
    copyright_info = song_soup.find("span", string=lambda text: "Aditya Music" in text if text else False)
    if copyright_info:
        aditya_music_count += 1

print(f"Total songs under 'Aditya Music': {aditya_music_count}")

driver.quit()




