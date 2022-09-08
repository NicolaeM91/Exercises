import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# BY ID
driver.get('http://automationpractice.com/index.php')
search = driver.find_element(By.ID, value='search_query_top')
search.send_keys('T-shirt')
sleep(3)

driver.get(url='https://www.techlistic.com/p/selenium-practice-form.html')
continents = driver.find_element(By.ID, value='continents')
continents.send_keys('Europe')
sleep(3)

driver.get(url='https://www.techlistic.com/p/selenium-practice-form.html')
date = driver.find_element(By.ID, value="datepicker")
date.send_keys('01.01.2022')
sleep(3)

# BY LINK TEXT

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Buttons').click()
sleep(3)

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Dropdown').click()
sleep(3)

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Switch Window').click()
sleep(3)

# BY PARTIAL LINK TEXT

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
sleep(3)

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Key').click()
sleep(3)

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Complete').click()
sleep(3)


# BY NAME

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
first_name = driver.find_element(By.NAME, 'firstname')
first_name.send_keys('Nicu')
sleep(3)

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
last_name = driver.find_element(By.NAME, 'lastname')
last_name.send_keys('Balanica')
sleep(3)

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
continents = driver.find_element(By.NAME, 'continents')
continents.send_keys('Australia')
sleep(3)

# BY TAG

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
input_list = driver.find_elements(By.TAG_NAME, 'input')
input_list[0].send_keys('Nicu')
input_list[1].send_keys('Balanica')
sleep(3)

# BY CLASS NAME

driver.get('https://formy-project.herokuapp.com//form')
tool = driver.find_elements(By.CLASS_NAME, 'form-control')
tool[0].send_keys('Nicu')
tool[1].send_keys('Balanica')
tool[2].send_keys('Student')
tool[3].send_keys('2')
sleep(3)

# BY CSS

# ID
driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
driver.find_element(By.CSS_SELECTOR, 'input#search_query_top').send_keys('Shirt')
sleep(3)

# BY CLASS
driver.get('https://formy-project.herokuapp.com/form')
driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Nicu')
sleep(3)

# BY ATRIBUT=VALOARE
driver.get('https://formy-project.herokuapp.com/form')
driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "Enter last name"]').send_keys('Balanica')
sleep(3)

# BY ATRIBUT = VALOARE_PARTIALA
driver.get('https://formy-project.herokuapp.com/form')
driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('Balanica')
sleep(5)

# BY XPATH

# 3 ATRIBUT-VALOARE
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
first_element = driver.find_element(By.XPATH, '//input[@name ="firstname"]').send_keys('Nicu')
second_element = driver.find_element(By.XPATH, '//input[@name = "lastname"]').send_keys('Balanica')
third_element = driver.find_element(By.XPATH, '//select[@id = "continents"]').send_keys('Africa')
sleep(3)

# 3 DUPA TEXTUL DE PE ELEMENT
driver.get('https://the-internet.herokuapp.com/')
text_element = driver.find_element(By.XPATH, '//a[text() = "Broken Images"]').click()
sleep(3)

driver.get('https://the-internet.herokuapp.com/')
text_element = driver.find_element(By.XPATH, '//a[text() = "Floating Menu"]').click()
sleep(3)

driver.get('https://the-internet.herokuapp.com/')
text_element = driver.find_element(By.XPATH, '//a[text() = "Key Presses"]').click()
sleep(3)

# 1 DUPA PARTIAL TEXT
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
element = driver.find_element(By.XPATH, '//* [contains(@name, "last")]').send_keys('Balanica')
sleep(3)

# 1 CU SAU FOLOSIND PIPE
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
element = driver.find_element(By.XPATH, '//input [@name = "lastname"]| '
                                        '//input[@placeholder = "Enter last name"]').send_keys('Balanica')
sleep(3)

# 1 CU *
driver.get('https://formy-project.herokuapp.com/form')
element = driver.find_element(By.XPATH, '//input[@*="last-name"]').send_keys('Balanica')
sleep(3)

# 1 IN CARE LE IEI CA PE O LISTA DE XPATH SI IN PYTHON AJUNGE 1 ELEMENT, DECI CU (XPATH)[1]
driver.get('https://formy-project.herokuapp.com/form')
element = driver.find_elements(By.XPATH, '//input[@*="form-control"]')
element[1].send_keys('element')
sleep(3)

# 1 IN CARE SA FOLOSESTI PARENT::
driver.get('https://formy-project.herokuapp.com/form')
element = driver.find_elements(By.XPATH, '//*[@type="text"]//parent::div')
print(f"The text  is: {element[2].text}")
sleep(3)


# 1 IN CARE SA FOLOSESTI FRATELE ANTERIOR SAU DE DUPA (LA ALEGERE)
driver.get('https://formy-project.herokuapp.com/form')
element_by_sibling = driver.find_element(By.XPATH, '//*[@type="text"]//parent::div/following-sibling::div')
print(f"The text  is: {element_by_sibling.text}")
sleep(3)


# 1 FUNCTIE CA SI CEA DE LA CLASA PRIN CARE SA POT ALEGE EU PRIN PARAMETRU CU CE ELEMENT VREAU SA INTERACTIONEZ

def formy_input(placeholder_text, input_value):
    driver.get('https://formy-project.herokuapp.com/autocomplete')
    input_ = driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input_.clear()
    input_.send_keys(input_value)

formy_input('Enter address', 'Cluj')
formy_input('Street address', 'Florilor')
formy_input('City', 'Floresti')






