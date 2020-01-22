from selenium import webdriver
driver =webdriver.Chrome(r'C:\Users\Vardan\PycharmProjects\untitled\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver')
driver.get('https://github.com/')
driver.find_element_by_id ("user[login]").send_keys("sofyapetrosyan03")
driver.find_element_by_id ("user[email]").send_keys("sonapetrosyan06@mail.ru")
driver.find_element_by_id ("user[password]").send_keys("Dd395411410")
driver.find_element_by_css_selector ("body > div.application-main > main > div.py-6.py-sm-8.jumbotron-codelines > div > div > div.mx-auto.col-sm-8.col-md-6.hide-sm > div > form > button").click()

