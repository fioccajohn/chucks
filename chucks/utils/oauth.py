import os
import webbrowser
import json
from pathlib import Path
import threading
from flask import Flask, request, redirect, jsonify
from requests_oauthlib import OAuth2Session
from token_manager import TokenManager


class OAuthApp:
    def __init__(self, config_file="~/.config/chucks/config.json"):
        with open(Path(config_file).expanduser()) as f:
            self.config = json.load(f)

        self.client_id = self.config["client_id"]
        self.client_secret = self.config["client_secret"]
        self.redirect_uri = self.config["redirect_uri"]
        self.authorization_base_url = self.config["authorization_base_url"]
        self.token_url = self.config["token_url"]
        self.refresh_url = self.token_url
        self.scope = self.config["scope"]

        self.cert_path = Path(
            self.config.get("cert_path", "~/.config/chucks/cert.pem")
        ).expanduser()
        self.key_path = Path(
            self.config.get("key_path", "~/.config/chucks/key.pem")
        ).expanduser()

        self.token_manager = TokenManager(
            self.config.get("token_file", "~/.config/chucks/access_token.json")
        )

        self.app = Flask(__name__)
        self.app.secret_key = os.urandom(24)

        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/callback", "callback", self.callback, methods=["GET"])

    def check_token(self):
        token = self.token_manager.load_token()
        if token and not self.token_manager.is_token_expired(token):
            return token
        return None

    def start_auth_flow(self):
        webbrowser.open(self.get_auth_url())
        self.run_server_thread()

    def get_auth_url(self):
        oauth_session = OAuth2Session(
            self.client_id, redirect_uri=self.redirect_uri, scope=self.scope
        )
        authorization_url, _ = oauth_session.authorization_url(
            self.authorization_base_url
        )
        return authorization_url

    def index(self):
        token = self.check_token()
        if token:
            return jsonify({"message": "You are already authenticated."})
        return redirect(self.get_auth_url())

    def callback(self):
        oauth_session = OAuth2Session(
            self.client_id, redirect_uri=self.redirect_uri, scope=self.scope
        )
        token = oauth_session.fetch_token(
            self.token_url,
            client_secret=self.client_secret,
            authorization_response=request.url,
        )
        self.token_manager.save_token(token)
        return jsonify(token)

    def run_server(self):
        self.app.run(port=8182, ssl_context=(self.cert_path, self.key_path))

    def run_server_thread(self):
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()


if __name__ == "__main__":
    oauth_app = OAuthApp()
    token = oauth_app.check_token()
    if token is None:
        oauth_app.start_auth_flow()
    else:
        print("Token is valid, no need for authentication flow.")
        access_token = oauth_app.token_manager.get_access_token()
        print(f"Access Token: {access_token}")
