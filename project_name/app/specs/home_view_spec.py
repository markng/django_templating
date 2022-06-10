import pytest
from django.urls import reverse


def describe_a_home_view():
    @pytest.fixture
    def client():
        from django.test import Client
        return Client()

    def it_renders_an_api_link(client):
        result = client.get('/')
        assert result.status_code == 200
        assert reverse('api-root') in result.content.decode('utf-8')

    def it_renders_a_admin_link(client):
        result = client.get('/')
        assert result.status_code == 200
        assert reverse('admin:index') in result.content.decode('utf-8')
