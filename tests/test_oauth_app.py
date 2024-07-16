from .context import chucks

import threading
import time

import unittest
import requests

from chucks.utils.oauth import OAuthApp


class TestOAuthApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = OAuthApp()

        # TODO: Debug mode as kwarg?
        cls.server_thread = threading.Thread(target=cls.app.run)
        cls.server_thread.daemon = True

        time.sleep(1)  # Give the server a second to start

    @classmethod
    def tearDownClass(cls):
        # Terminate the Flask app
        pass

    def test_home_route(self):
        response = requests.get("http://127.0.0.1:5000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, Flask!")


if __name__ == "__main__":
    unittest.main()
