from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from corrector import convert_data as cd
from corrector import convert_funds as cf
from corrector import convert_nums as cn
import os.path
from os.path import dirname


# AUXILIARY FUNCTIONS:

# collect available upgrades
def collect(section):
    values, elements = list(), list()
    if section == "research":
        for i in range(11, 0, -1):
            research = driver.find_element_by_xpath(f"/html/body/div[1]/div[1]/div/div[2]/div/ul/li[{i}]"
                                                    f"/div/div/button[1]/small")
            values.append(cd(research.text))
            elements.append(research)
    elif section == "hr":
        for i in range(8, 0, -1):
            hr = driver.find_element_by_xpath(f"/html/body/div[1]/div[3]/div/div[2]/div/ul/li[{i}]/div/button/small")
            values.append(cf(hr.text))
            elements.append(hr)
    elif section == "upgrade":
        for i in range(64, 1, -1):
            upgrade = driver.find_element_by_xpath(
                f"/html/body/div[1]/div[4]/div/div[2]/div/ul/li[{i}]/div/button/small")
            values.append(cf(upgrade.text))
            elements.append(upgrade)
    for i in range(len(values)-1, -1, -1):
        if values[i] == "":
            del values[i]
            del elements[i]
        else:
            continue
    if values == ['']:
        return "0", "0"
    else:
        return values, elements


# perform buying action if possible
def buy(what):
    stuff = collect(what)
    if stuff[0] == "0":
        pass
    else:
        if what == "research":
            for value, web_element in zip(stuff[0], stuff[1]):
                data = cn(num_data.text[5:])
                if float(value) < float(data):
                    upgrade_actions = ActionChains(driver)
                    upgrade_actions.move_to_element(web_element)
                    upgrade_actions.click()
                    upgrade_actions.perform()
        else:
            for value, web_element in zip(stuff[0], stuff[1]):
                cash = cn(num_grants.text[12:])
                if float(value) < float(cash):
                    upgrade_actions = ActionChains(driver)
                    upgrade_actions.move_to_element(web_element)
                    upgrade_actions.click()
                    upgrade_actions.perform()


# MAIN SECTION:
num_of_reps = input("Set number of loops: ")
driver = webdriver.Chrome(os.path.join(dirname(__file__)+"/chromedriver.exe"))
driver.get("https://particle-clicker.web.cern.ch/")
driver.implicitly_wait(5)

# change lab name
name = driver.find_element_by_id("labname")
name.send_keys(Keys.CONTROL + "a")
name.send_keys(Keys.DELETE)
name.send_keys("Python Selenium Automated Lab!")

# find button, set up action
button = driver.find_element_by_id("detector-events")
actions = ActionChains(driver)
actions.click(button)

# get your numbers
num_data = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]")
num_grants = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]")

# main loop
for _ in range(10):
    actions.perform()

for _ in range(int(num_of_reps)):
    buy("research")
    actions.perform()
    buy("hr")
    actions.perform()
    buy("upgrade")
    actions.perform()
