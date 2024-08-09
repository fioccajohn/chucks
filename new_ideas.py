# coding: utf-8
import json
from schwab.auth import client_from_login_flow
from pathlib import Path
CONFIG_FILE = Path('/Users/johnfiocca/.config/chucks/config.json')
with open(self.CONFIG_FILE) as f:
            j = json.load(f)
            
with open(CONFIG_FILE) as f:
            j = json.load(f)
            
c = client_from_login_flow(j.get('client_id'), j.get('client_secret'), j.get('redirect_uri'), Path('/Users/johnfiocca/.config/chucks/access_token.json'))
c = client_from_login_flow(j.get('client_id'), j.get('client_secret'), j.get('redirect_uri'), Path('/Users/johnfiocca/.config/chucks/access_token.json'))
r = c.get_accounts()
r.json()
