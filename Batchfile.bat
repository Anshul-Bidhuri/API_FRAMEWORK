rem pytest -m LoginPage -S reqres.in --html=.\\Report\\api_automation_report.html
pytest -m LoginPage -S reqres.in --alluredir=.\\Report\\allure-results
allure generate Report\allure-results -o Report\allure-report --clean