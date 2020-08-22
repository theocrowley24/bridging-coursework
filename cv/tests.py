from django.test import TestCase, Client
from django.urls import resolve
from cv.views import home
from cv.views import addQualification
from cv.views import addExperience
from cv.views import edit
from django.contrib.auth.models import User
from cv.models import Experience
from cv.models import Qualification
from cv.models import Cv

# Create your tests here.
class CvTest(TestCase):
    def setUp(self):
        Cv.objects.create(name="test", address="test", phoneNumber="test", emailAddress="test", aboutMe="test")

        User.objects.create_user("test", password="12345")
        self.loggedInClient = Client()
        self.loggedInClient.login(username="test", password="12345")

    def testRootResolvesToHomePageView(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, home)

    def testEditResolvesToHomePageView(self):
        found = resolve('/cv/edit')
        self.assertEqual(found.func, edit)

    def testAddQualificationResolvesToAddQualificationView(self):
        found = resolve('/cv/addQualification')
        self.assertEqual(found.func.__name__, addQualification.__name__)

    def testAddExperienceResolvesToAddExperienceView(self):
        found = resolve('/cv/addExperience')
        self.assertEqual(found.func.__name__, addExperience.__name__)

    def testUserUpdateCv(self):
        response = self.client.post('/cv/edit')
        self.assertNotEqual(response.status_code, 404)

        self.loggedInClient.post('/cv/edit', data={'name': 'testRenamed', 'address': 'test', 'phoneNumber': 'test', 'emailAddress': 'test', 'aboutMe': 'test'})
        self.assertEqual(Cv.objects.get().name, 'testRenamed')

    def testUserAddExperience(self):
        response = self.client.post('/cv/addExperience')
        self.assertNotEqual(response.status_code, 404)

        countBefore = Experience.objects.count()
        response = self.loggedInClient.post('/cv/addExperience', data={'name': 'Test', 'description': 'Test', 'startDate': '01/01/01', 'endDate': '01/01/01'})
        countAfter = Experience.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(countBefore + 1, countAfter)

    def testUserAddQualification(self):
        response = self.client.post('/cv/addQualification')
        self.assertNotEqual(response.status_code, 404)
        
        countBefore = Qualification.objects.count()
        response = self.loggedInClient.post('/cv/addQualification', data={'name': 'Test', 'description': 'Test', 'startDate': '01/01/01', 'endDate': '01/01/01'})
        countAfter = Qualification.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(countBefore + 1, countAfter)