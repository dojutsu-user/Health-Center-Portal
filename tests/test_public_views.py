import pytest
from ddf import G
from django.contrib.auth.models import AnonymousUser, User


@pytest.mark.django_db
class TestPublicViewResponse:

    def test_homepage_returns_200(self, client):
        response = client.get('/')
        assert response.status_code == 200, 'Homepage should return 200 OK response'
        announcements = response.context_data.get('announcements')
        assert len(announcements) == 0, '0 announcements are present'

    def test_doctors_page(self, client):
        response = client.get('/available-doctors/')
        assert response.status_code == 200
        doctors = response.context_data.get('object_list')
        assert len(doctors) == 0, 'No doctors are present in db'

    def test_about_page(self, client):
        response = client.get('/about/')
        assert response.status_code == 200, 'About page must return 200 OK response'

    def test_login_page_with_anonymous_user(self, client):
        response = client.get('/login/')
        assert response.status_code == 200, 'Login page must return 200 OK response if the user is not authenticated'
        assert isinstance(response.context.get('user'), AnonymousUser)

    def test_login_page_with_authenticated_user(self, client):
        user = G(User)
        client.force_login(user)
        response = client.get('/login/')
        assert response.status_code == 302, 'Logged in user should get redirected on accessing login page'
        assert response.has_header('location') == True, 'Redirection url should be present in response header'
        assert response.get('location') == '/', 'Location header must contain redirection url which is homepage in this case.'
