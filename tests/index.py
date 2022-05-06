import os
import pathlib
import unittest

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

    def index_title(self):
        driver.get(file_uri("index.html"))
        self.assertEqual(driver.title, "Shon Santhosh (@mjvbz)")

    def main_title(self):
        driver.get(file_uri("index.html"))
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "Shon Santhosh")

    def paragraph(self):
        driver.get(file_uri("index.html"))
        paragraphClass = driver.find_element_by_class_name("p")
        self.assertEqual(driver.paragraphClass.text, not "")

    def github_link(self):
        driver.get(file_uri("index.html"))
        findGithub = driver.find_element_by_class_name("Github-link")
        findGithub.click()
        self.assertEqual(driver.find_element_by_xpath("https://github.com/itsMeShon"))

    def stackoverflow_link(self):
        driver.get(file_uri("index.html"))
        findsof = driver.find_element_by_class_name("StackOverFlow-link")
        findsof.click()
        self.assertEqual(driver.find_element_by_xpath("https://stackoverflow.com/users/17189428/itsmeshon"))

    def website_link(self):
        driver.get(file_uri("index.html"))
        findWebsite = driver.find_element_by_class_name("Website-link")
        findWebsite.click()
        self.assertEqual(driver.find_element_by_xpath("https://itsmeshon.github.io"))

if __name__ == "__main__":
    unittest.main()
