import pytest
import allure

from Methods.LoginPage import LoginMethods


class TestLogin(LoginMethods):
    @allure.link('https://www.youtube.com/channel/UCSPUF_fElVzLyFuqyKHXCPA', name='Click Me')
    @allure.title("To add custom title in Allure report")
    @pytest.mark.LoginPage
    def test_login_apis_correct_cred(self):
        """LOGIN PAGE: test login API with correct credentials """
        status = self.check_login_with_correct_cred()
        assert status

    @pytest.mark.LoginPage
    def test_login_apis_incorrect_cred(self):
        """LOGIN PAGE: test login API with incorrect credentials """
        status = self.check_login_with_incorrect_cred()
        assert status