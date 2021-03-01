from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import os
import PIL

url = 'https://scholar.google.com/'

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Volumes/macbackup2/_cancer_research"}
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome('/Users/austin/Downloads/chromedriver', chrome_options=chromeOptions)
wait = WebDriverWait(driver, 5)
extended_wait = WebDriverWait(driver, 10)
driver.get(url)
time.sleep(1)
# what I want to search
#search_topic = input("what topic?: ")
search_topic = "covid 19"
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gs_hdr_tsi"]')))
#time.sleep(2)
driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]').send_keys(search_topic)

#click search
#//*[@id="gs_hdr_tsb"]/span/span[1]
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gs_hdr_tsb"]/span/span[1]')))
driver.find_element_by_xpath('//*[@id="gs_hdr_tsb"]/span/span[1]').click()

# first pdf link
# //*[@id="gs_res_ccl_mid"]/div[1]/div[1]/div/div/a
# //*[@id="gs_res_ccl_mid"]/div[2]/div[1]/div/div/a
# //*[@id="gs_res_ccl_mid"]/div[4]/div[1]/div/div/a
# //*[@id="gs_res_ccl_mid"]/div[6]/div[1]/div/div/a

def get_pdfs_from_page():
    #x = 0
    for i in range(1, 11):
        #x = x + 1
        i_string = str(i)
        first_half_xpath = '//*[@id="gs_res_ccl_mid"]/div['
        second_half_xpath = ']/div[1]/div/div/a'
        full_xpath = first_half_xpath + i_string + second_half_xpath
        #print(driver.current_url)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, full_xpath)))
            pdf_available = driver.find_element_by_xpath(full_xpath).text
            print(pdf_available)
            if '[PDF]' in pdf_available:
                chrome_url = driver.current_url
                # print(chrome_url)
                driver.find_element_by_xpath(full_xpath).click()

                #x, y = pyautogui.position()
                time.sleep(3)
                #print(x,y)
                if chrome_url == driver.current_url:
                    pass
                else:
                    #x_ = str(x) + "breast" + ".jpg"

                    pyautogui.hotkey('command', 's')
                    time.sleep(1.5)

                    # # 1128, 191 are the coordinates for the download button
                    # x, y = pyautogui.position()
                    # #print(x,y)
                    # pyautogui.moveTo(1128, 191, duration=0.25)
                    # pyautogui.click(1128, 191)
                    #
                    # time.sleep(1)
                    #
                    # x, y = pyautogui.position()
                    # 250, 489 harddrive coordinates in finder window
                    if i < 5 :
                        pyautogui.moveTo(250, 489, duration=0.25)
                        pyautogui.click(250, 489)
                        time.sleep(0.5)
                        pyautogui.click(250, 489)
                        time.sleep(3)
                        pyautogui.press('enter')
                    else:
                        pyautogui.press('enter')
                        #print(x,y)
                        # 989, 601 is the save button coordinates
                        # pyautogui.moveTo(989, 601, duration=0.25)
                        # pyautogui.click(989, 601)


                    # time.sleep(1)
                    # image = pyautogui.screenshot()
                    # image.save("/Volumes/nada/cancer_research/breast_cancer/" + x_)

                    # let file download for for seconds
                    time.sleep(4)

                    # goes back a page
                    driver.execute_script("window.history.go(-1)")
        except:
            pass
for x in range(1,200):
    get_pdfs_from_page()
# next page //*[@id="gs_n"]/center/table/tbody/tr/td[12]/a/b
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a/b')))
        driver.find_element_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a/b').click()
    except:
        pyautogui.scroll(500)
        time.sleep(0.1)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a/b')))
        driver.find_element_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a/b').click()

