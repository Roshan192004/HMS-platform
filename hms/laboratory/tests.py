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
        # Login to set session
        self.client.post(reverse('laboratory_login'), {
            'laboratory_name': 'Dr. Test',
            'laboratory_password': 'pass'
        })

    def test_dashboard_shows_name(self):
        response = self.client.get(reverse('laboratory_dashboard'))
        if response.status_code != 200:
            print(f"Status Code: {response.status_code}")
            print(f"Redirect URL: {response.get('Location')}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dr. Test")

    def test_profile_shows_details(self):
        response = self.client.get(reverse('laboratory_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dr. Test")
        self.assertContains(response, "test@example.com")

    def test_dashboard_search(self):
        from django.utils.timezone import now
        LabTest.objects.create(
            test_id="LAB-SEARCH-1",
            patient_name="Searchable Patient",
            test_type="Blood",
            status="Pending",
            priority="Normal",
            date=now().date()
        )
        response = self.client.get(reverse('laboratory_dashboard') + "?q=Searchable")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Searchable Patient")
        
        response_none = self.client.get(reverse('laboratory_dashboard') + "?q=NonExistent")
        self.assertNotContains(response_none, "Searchable Patient")
