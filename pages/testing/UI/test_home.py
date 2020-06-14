from selenium import webdriver


driver = webdriver.Chrome()
driver.set_page_load_timeout(30)

driver.maximize_window()
driver.get('http://127.0.0.1:8000/')

#confirming done
print("Done") 


def test_check_title():
    assert driver.title == 'Bienvenue chez pure beurre'


def test_verify_main_title():
    assert driver.find_element_by_id('main-title').text == 'DU GRAS, OUI, MAIS DE QUALITÉ!'

#Close the driver successfully
#uncomment the line below to close the browser
#driver.quit()