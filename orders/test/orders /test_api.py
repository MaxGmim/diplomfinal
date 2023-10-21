import pytest
from model_bakery import baker
from django.conf import settings
settings.configure()
from rest_framework.test import APIClient
import json


def test_something():

 assert True