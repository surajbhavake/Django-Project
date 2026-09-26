from rest_framework import status
from rest_framework.test import APITestCase

from .models import URL
from django.db import IntegrityError

class URLAPITests(APITestCase):

    def test_create_url(self):
        response = self.client.post(
            "/api/urls/",
            {
                "original_url": "https://example.com"
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            URL.objects.count(),
            1,
        )

    def test_list_urls(self):
        URL.objects.create(
            original_url="https://google.com",
            short_code="abc123",
        )

        URL.objects.create(
            original_url="https://github.com",
            short_code="xyz789",
        )

        response = self.client.get("/api/urls/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            2,
        )

    def test_retrieve_url(self):
        url = URL.objects.create(
            original_url="https://example.com",
            short_code="abc123",
        )

        response = self.client.get(
            f"/api/urls/{url.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["original_url"],
            "https://example.com",
        )

        self.assertEqual(
            response.data["short_code"],
            "abc123",
        )

    def test_retrieve_nonexistent_url(self):
        response = self.client.get(
            "/api/urls/999/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_delete_url(self):
        url = URL.objects.create(
            original_url="https://example.com",
            short_code="abc123",
        )

        response = self.client.delete(
            f"/api/urls/{url.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertEqual(
            URL.objects.count(),
            0,
        )

    def test_delete_nonexistent_url(self):
        response = self.client.delete(
            "/api/urls/999/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_redirect(self):
        URL.objects.create(
            original_url="https://example.com",
            short_code="abc123",
        )

        response = self.client.get(
            "/abc123"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_302_FOUND,
        )

        self.assertEqual(
            response.url,
            "https://example.com",
        )

    def test_invalid_url(self):
        response = self.client.post(
            "/api/urls/",
            {
                "original_url": "not-a-valid-url"
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertEqual(
            URL.objects.count(),
            0,
        )

    def test_invalid_short_code(self):
        response = self.client.get(
            "/doesnotexist"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )
    def test_short_code_must_be_unique(self):
        URL.objects.create(
            original_url="https://google.com",
            short_code="abc123",
        )

        with self.assertRaises(IntegrityError):
            URL.objects.create(
                original_url="https://github.com",
                short_code="abc123",
            )