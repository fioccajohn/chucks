#!/usr/bin/env python

### TODO Integrate the auth_server.py file to work as the web browser to authenticate.

import json
import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient, LegacyApplicationClient, MobileApplicationClient, WebApplicationClient
import time


class OAuth2Auth:
    def __init__(self, config_file):
        self.load_config(config_file)
        self.state = None
    
    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)
        self.client_id = self.config['client_id']
        self.client_secret = self.config['client_secret']
        self.authorization_url = self.config['authorization_url']
        self.token_url = self.config['token_url']
        self.refresh_url = self.config['refresh_url']
        self.redirect_uri = self.config['redirect_uri']
        self.scope = self.config['scope']
    
    def get_authorization_url(self):
        client = WebApplicationClient(self.client_id)
        oauth = OAuth2Session(client=client, redirect_uri=self.redirect_uri, scope=self.scope)
        auth_url, self.state = oauth.authorization_url(self.authorization_url)
        return auth_url
    
    def fetch_token(self, authorization_response):
        client = WebApplicationClient(self.client_id)
        oauth = OAuth2Session(client=client, redirect_uri=self.redirect_uri, state=self.state)
        token = oauth.fetch_token(self.token_url, authorization_response=authorization_response, client_secret=self.client_secret)
        self.token_saver(token)
        return token
    
    def refresh_token(self, refresh_token):
        extra = {'client_id': self.client_id, 'client_secret': self.client_secret}
        client = WebApplicationClient(self.client_id)
        oauth = OAuth2Session(client=client, token={'refresh_token': refresh_token, 'token_type': 'Bearer'}, auto_refresh_kwargs=extra, auto_refresh_url=self.refresh_url, token_updater=self.token_saver)
        token = oauth.refresh_token(self.refresh_url)
        return token
    
    def token_saver(self, token):
        with open('./chucks/auth/access_token.json', 'w') as f:
            json.dump(token, f)
    
    def load_token(self):
        try:
            with open('./chucks/auth/access_token.json', 'r') as f:
                token = json.load(f)
                return token
        except FileNotFoundError:
            return None
    
    def is_token_valid(self, token):
        if 'expires_at' in token:
            return token['expires_at'] > time.time()
        return False

    def client_credentials_flow(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=self.token_url, client_id=self.client_id, client_secret=self.client_secret)
        self.token_saver(token)
        return token
    
    def password_credentials_flow(self, username, password):
        client = LegacyApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=self.token_url, username=username, password=password, client_id=self.client_id, client_secret=self.client_secret)
        self.token_saver(token)
        return token
    
    def implicit_flow(self):
        client = MobileApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client, redirect_uri=self.redirect_uri, scope=self.scope)
        auth_url, state = oauth.authorization_url(self.authorization_url)
        return auth_url, state
