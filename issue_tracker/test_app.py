from django.apps import apps
from django.test import TestCase
from .apps import IssueTrackerConfig

class TestIssueTrackerConfig(TestCase):
    def test_app(self):
        self.assertEqual("issue_tracker", IssueTrackerConfig.name)
        self.assertEqual("issue_tracker", apps.get_app_config("issue_tracker").name)