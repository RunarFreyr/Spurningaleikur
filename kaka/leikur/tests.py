#encoding: utf-8

from django.test.client import Client
from django.test import TestCase

class SimpleTest(TestCase):
    def testIsUp(self):
        c = Client()
        response = c.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def testWronganswer(self):
        c = Client()
        response = c.get('/1/a')
        self.failIfEqual(response.content.find("Rangt"), -1)
        self.failUnlessEqual(response.status_code, 200)

    def testRightanswer(self):
        c = Client()
        response = c.get('/1/d')
        self.failIfEqual(response.content.find("Rétt"), -1)
        self.failUnlessEqual(response.status_code, 200)
