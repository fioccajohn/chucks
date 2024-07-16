import json
from pathlib import Path
from time import time
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import logging
import base64

logging.basicConfig(level=logging.CRITICAL)


class TokenManager:
    def __init__(
        self,
        token_file="~/.config/chucks/access_token.json",
        config_file="~/.config/chucks/config.json",
    ):
        self.token_file = Path(token_file).expanduser()

        with open(Path(config_file).expanduser()) as f:
            self.config = json.load(f)

        self.client_id = self.config["client_id"]
        self.client_secret = self.config["client_secret"]
        self.redirect_uri = self.config["redirect_uri"]
        self.authorization_base_url = self.config["authorization_base_url"]
        self.token_url = self.config["token_url"]
        self.refresh_url = self.token_url
        self.scope = self.config["scope"]

    def save_token(self, token):
        # Calculate and add the expires_at field
        token["expires_at"] = time() + token["expires_in"]
        with open(self.token_file, "w") as f:
            json.dump(token, f)

    def load_token(self):
        if self.token_file.exists():
            with open(self.token_file, "r") as f:
                return json.load(f)
        return None

    def is_token_expired(self, token):
        return token["expires_at"] < time()

    def refresh_token(self):
        token = self.load_token()
        if token is None:
            raise ValueError("Token not found.")

        logging.debug(f"Loaded token: {token}")

        auth_header_value = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode()

        headers = {
            "Authorization": f"Basic {auth_header_value}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": token.get("refresh_token"),
        }

        try:
            response = OAuth2Session().post(
                self.refresh_url, headers=headers, data=payload
            )
            response.raise_for_status()
            new_token = response.json()
            logging.debug(f"New token: {new_token}")
        except Exception as e:
            logging.error(f"Error during token refresh: {e}")
            logging.error(
                f"Response content: {e.response.content if hasattr(e, 'response') else 'No response content'}"
            )
            raise

        self.save_token(new_token)
        return new_token

    def get_or_refresh_access_token(self):
        token = self.load_token()
        if token and not self.is_token_expired(token):
            return token["access_token"]
        else:
            new_token = self.refresh_token()
            return new_token["access_token"]

    def get_oauth_session(self):
        token = self.load_token()
        if not token or self.is_token_expired(token):
            token = self.refresh_token()

        extra = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        return OAuth2Session(
            client_id=self.client_id,
            token=token,
            auto_refresh_kwargs=extra,
            auto_refresh_url=self.refresh_url,
            token_updater=self.save_token,
        )


if __name__ == "__main__":
    token_manager = TokenManager()
    print(token_manager.get_or_refresh_access_token())
