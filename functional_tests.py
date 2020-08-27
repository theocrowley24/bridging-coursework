from selenium import webdriver
import unittest
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

class CvTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000/cv")

    def tearDown(self):
        self.browser.quit()

    def testVisitHomePage(self):
        self.assertIn("CV", self.browser.title)

    def testHomePageReturnsCorrectHtml(self):
        titleElement = self.browser.find_element_by_class_name("title")
        self.assertIsNotNone(titleElement, "Title element does not exist")

        myInfoElement = self.browser.find_element_by_id("my-info")
        self.assertIsNotNone(myInfoElement, "My Info element does not exist")

        aboutMeElement = self.browser.find_element_by_id("about-me")
        self.assertIsNotNone(aboutMeElement, "About me element does not exist")

        qualificationsElement = self.browser.find_element_by_id("qualifications")
        self.assertIsNotNone(qualificationsElement, "Qualifications element does not exist")

        experienceElement = self.browser.find_element_by_id("experience")
        self.assertIsNotNone(experienceElement, "Experience element does not exist")

    def testAboutMeExists(self):
        aboutMeElement = self.browser.find_elements_by_id("about-me-text")
        self.assertIsNotNone(aboutMeElement)

    def testAtLeastOneQualification(self):
        parentElement = self.browser.find_element_by_id("qualifications-wrapper")
        children = parentElement.find_elements_by_css_selector("*")

        self.assertGreaterEqual(len(children), 1)

    def testAtLeastOneExperience(self):
        parentElement = self.browser.find_element_by_id("experience-wrapper")
        children = parentElement.find_elements_by_css_selector("*")

        self.assertGreaterEqual(len(children), 1)

class CvEditTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000/cv/edit")

    def tearDown(self):
        self.browser.quit()

    def testEditPageReturnsCorrectHtml(self):
        titleElement = self.browser.find_element_by_id("title")
        self.assertIsNotNone(titleElement, "Title element does not exist")

        formElement = self.browser.find_element_by_tag_name("form")
        self.assertIsNotNone(formElement, "There is no form")

class CvAddQualificationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000/cv/addQualification")

    def tearDown(self):
        self.browser.quit()

    def testAddQualificationPageReturnsCorrectHtml(self):
        titleElement = self.browser.find_element_by_id("title")
        self.assertIsNotNone(titleElement, "Title element does not exist")

        formElement = self.browser.find_element_by_tag_name("form")
        self.assertIsNotNone(formElement, "There is no form")
        
class CvAddExperienceTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000/cv/addExperience")

    def tearDown(self):
        self.browser.quit()

    def testAddExperiencePageReturnsCorrectHtml(self):
        titleElement = self.browser.find_element_by_id("title")
        self.assertIsNotNone(titleElement, "Title element does not exist")

        formElement = self.browser.find_element_by_tag_name("form")
        self.assertIsNotNone(formElement, "There is no form")


if __name__ == "__main__":
    unittest.main(warnings='ignore')