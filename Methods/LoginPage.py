import requests
from TestData import test_data
from Logs import logs_file

class LoginMethods:

    log = logs_file.get_logs()

    def check_login_with_correct_cred(self):
        """
        this method checks the status of Login API with correct credentials
        :return: status
        """
        flag = True
        try:
            self.log.info(f"API is: {test_data.login_base_url}")
            self.log.info(f"Input Data is: {test_data.correct_login_credentials}")
            r = requests.post(test_data.login_base_url, data=test_data.correct_login_credentials)
            if r.status_code == 200:
                self.log.info(f"Status code of API is: {r.status_code}")
            else:
                self.log.error(f"Status code of API is: {r.status_code}, Expected Status code: 200")
                flag = False
            if r.json()['token']:
                self.log.info(f"Token is generated successfully: {r.json()['token']}")
            else:
                self.log.error(f"Token is not generated successfully")
                flag = False
        except Exception as e:
            self.log.error(f"Exception {e} occurred")
        return flag

    def check_login_with_incorrect_cred(self):
        """
        this method checks the status of Login API with incorrect credentials
        :return: status
        """
        flag = True
        try:
            self.log.info(f"API is: {test_data.login_base_url}")
            self.log.info(f"Input Data is: {test_data.incorrect_login_credentials}")
            r = requests.post(test_data.login_base_url, data=test_data.incorrect_login_credentials)
            if r.status_code == 400:
                self.log.info(f"Status code of API is: {r.status_code}")
            else:
                self.log.error(f"Status code of API is: {r.status_code}, Expected Status code: 400")
                flag = False
            if r.json()['error'] == "user not found":
                self.log.info(f"Error message is correct")
            else:
                self.log.error(f"Error message is not correct")
                self.log.error(f"Actual message: {r.json()['error']}, Expected message: 'user not found'")
                flag = False
        except Exception as e:
            self.log.error(f"Exception {e} occurred")
        return flag