"""Writing test cases for Slack API
"""
from src.fetch import slack
from tests.mocks.mock_function import mock_api_success
import pytest

def test_add_success():
    """Test case for success
    """
    result = slack.add(10,20)
    assert result == 30

def test_add_negative():
    """Test case for negative params
    """
    with pytest.raises(TypeError):
        slack.add(10, "20")

def test_add_no_params():
    """test case for no params
    """
    with pytest.raises(TypeError):
        slack.add()

'''def test_get_conversations_list_success():
    """Test case for successfully getting response
    """
    base_url = "https://slack.com/api"
    response = slack.get_conversations_list(base_url)
    assert response.status_code == 200

def test_get_conversations_list_fail():
    """test case for requested resource not found
    """
    base_url = "https://slack.com/apl"
    response = slack.get_conversations_list(base_url)
    assert response.status_code == 404'''

#import pdb; pdb.set_trace()

# def test_get_conversations_list_success(mocker):
#     """Test case for mocking successful API response
#     """
#     mocker.patch("requests.get", mock_api_success)
#     response = slack.get_conversations_list("test_url")
#     json_data = response.json()
#     assert response.status_code == 200
#     assert json_data["key"] == "Success"

@pytest.mark.vcr()
def test_get_conversations_list_vcr():
    """Test case for mocking using vcr
    """
    base_url = "https://slack.com/api"
    response = slack.get_conversations_list(base_url)
    assert response.status_code == 200