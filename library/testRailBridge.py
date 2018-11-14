from elements.globalVariable import GlobalVariable
from library.testrail import APIClient

if __name__ == '__main__':

    client = APIClient(GlobalVariable.testrail_url)
    client.user = GlobalVariable.testrail_username
    client.password = GlobalVariable.testrail_password

    result_id = 'add_result_for_case/' + GlobalVariable.testRun_id + '/' + GlobalVariable.testCase_id

    result = client.send_post(
        result_id,
        {'status_id': 5, 'comment': 'Wadaw !', 'custom_tag': 1}
    )
