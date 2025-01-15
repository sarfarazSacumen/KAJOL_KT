"""Slack API call"""

import requests
from requests.adapters import HTTPAdapter
import logging
import json

class Slack:
    def __init__(self, access_token):
        """Initializing headers with bearer token, and configuring the logger

        Args:
            access_token : Slack bot token
        """
        self.access_token = access_token
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel("DEBUG")

        #console_handler = logging.StreamHandler()
        #console_handler.setLevel("DEBUG")
        file_handler = logging.FileHandler("slackLog.log", mode="w", encoding="utf-8")
        file_handler.setLevel(10)

        #self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        #console_formatter = logging.Formatter("%(levelname)s-%(name)s-%(message)s")
        file_formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(name)s-%(message)s")

        #console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)

    def get_conversations_list(self, base_url):
        """List out all the channel names
        """
        slack_adapter = HTTPAdapter(max_retries=2)
        session = requests.Session()

        try:
            session.mount(f"{base_url}/conversations.list", slack_adapter)
            response = session.get(f"{base_url}/conversations.list", headers = self.headers, timeout = 3)

            if response.status_code != 200:
                self.logger.error(f"HTTP Error: {response.status_code} for URL: {response.url}")
                return response
            
        except requests.exceptions.RequestException as e: #network errors, invalid URL, timeouts
            self.logger.exception(f"Request failed {e}")
            return None
        
        self.logger.debug(f"URL = {response.url}")
        self.logger.debug(f"Status code = {response.status_code}")

        try:
            json_data = response.json()
            json_pretty = json.dumps(json_data, indent=4)
            self.logger.info(f"JSON Data = {json_pretty}")
        except Exception as e:
            self.logger.exception(f"Content Not Found {e}")
            return None
            
        return response

    def get_user_list(self, base_url):
        """List out all user details
        """
        slack_adapter = HTTPAdapter(max_retries=2)
        session = requests.Session()

        try:
            session.mount(f"{base_url}/users.list", slack_adapter)
            response = session.get(f"{base_url}/users.list?limit=1&offset=1", headers = self.headers, timeout = 3)
        except Exception as e:
            self.logger.exception(f"{e}")
        
        self.logger.debug(f"URL = {response.url}")
        self.logger.debug(f"Status code = {response.status_code}")

        try:
            json_data = response.json()
            json_pretty = json.dumps(json_data, indent=4)
            self.logger.info(f"JSON Data = {json_pretty}")
        except Exception as e:
            self.logger.error(f"Content Not Found {e}", exc_info=True)
        return response

    def add(self, a: int, b: int) -> int:
        """Add two integer number and return integer result

        Args:
            a (int): first integer number
            b (int): Second integer number

        Returns:
            int: Return sum of a and b
        """
        return a+b

access_token = "xoxb-8228632731095-8243326122850-6C6zj2o4OEQTJZF4ybCswzn6"

slack = Slack(access_token)