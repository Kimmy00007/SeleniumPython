import datetime
from elements.globalVariable import GlobalVariable
from unittest import TestSuite, makeSuite
from pyunitreport import HTMLTestRunner
from testcases.surveyTest import Survey
from testcases.loginTest import Login

if __name__ == '__main__':

    today_date = datetime.date.today().strftime('%d:%m:%Y_%H:%m')

    suite = TestSuite()
    suite.addTest(makeSuite(Login))
    # suite.addTest(makeSuite(Survey))

    # DO NOT Update this section Below
    kwargs = {
        "output": GlobalVariable.report_location,
        "report_name": 'Regression_Report' + today_date,
        "failfast": True
    }

    runner = HTMLTestRunner(**kwargs)
    runner.run(suite)
