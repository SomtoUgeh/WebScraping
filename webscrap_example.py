from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("— incognito")

browser = webdriver.Chrome()
browser.get("https://github.com/SomtoUgeh")

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_class_name("js-repo")
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]

print('titles:')
print(titles, '\n')


language_element = browser.find_elements_by_class_name("text-gray")
languages = [x.text for x in language_element]
print("languages: ")
print(languages, '\n')


for title, language in zip(titles, languages):
    print("RepoName: Language")
    print(title + ": " + language, '\n')
