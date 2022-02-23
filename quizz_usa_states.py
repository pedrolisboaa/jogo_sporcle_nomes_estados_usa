from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

site_quizz = 'https://www.sporcle.com/games/g/states'

driver = webdriver.Chrome()
driver.get(site_quizz)

sleep(3)
driver.find_element(By.XPATH, '//*[@id="playPadding"]/a').click()

sleep(1)
state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
               "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
               "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
               "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
               "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
               "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
               "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
               "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

for i in state_names:
    driver.find_element(By.ID, 'gameinput').send_keys(i)
    print(f'Deu certo {i}')
    sleep(0.3)

sleep(100)
driver.quit()
