from django.test import TestCase, Client
from accounts.models import laboratory
from django.urls import reverse

class LaboratoryDashboardTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.lab = laboratory.objects.create(
            laboratory_name="Dr. Test",
            laboratory_password="pass",
            laboratory_email="test@example.com",
            laboratory_number="1234567890"
        )
        # Manually set session because it's required by the view
        session = self.client.session
        session['laboratory_id'] = self.lab.id
        session['laboratory_name'] = self.lab.laboratory_name
        session.save()

    def test_dashboard_shows_name(self):
        response = self.client.get(reverse('laboratory_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dr. Test")

    def test_profile_shows_details(self):
        response = self.client.get(reverse('laboratory_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dr. Test")
        self.assertContains(response, "test@example.com")
