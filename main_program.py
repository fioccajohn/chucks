#!/usr/bin/env python

from chucks.auth.oauth import OAuth2Auth
import time
import subprocess
import webbrowser
import requests

# TODO This kind of server loop check should be built into the code flow for authentication!
def get_access_token():
    oauth2_auth = OAuth2Auth('chucks/auth/config.json')

    token = oauth2_auth.load_token()

    if not token or not oauth2_auth.is_token_valid(token):
        
        try:
            # Start the Flask server
            flask_process = subprocess.Popen(['python3', 'chucks/auth/auth_server.py'])
            time.sleep(2)  # Wait to ensure the server is up

            # Open the authorization URL in the default web browser
            auth_url = oauth2_auth.get_authorization_url()
            webbrowser.open(auth_url)
            
            print("Waiting for the authorization to complete...")
            
            # Wait for the token file to be created
            while not token or not oauth2_auth.is_token_valid(token):
                token = oauth2_auth.load_token()
                time.sleep(1)

        finally:
            # Terminate the Flask server process
            flask_process.terminate()

    return token['access_token']

def get_schwab_profile(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get('https://api.schwabapi.com/trader/v1/accounts', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response content:", response.text)
        return None

def get_movers(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get('https://api.schwabapi.com/marketdata/v1/movers/%24SPX?sort=PERCENT_CHANGE_DOWN&frequency=0', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response content:", response.text)
        return None

def get_price_history(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get('https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=AAPL', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response content:", response.text)
        return None

if __name__ == "__main__":
    # Example usage
    access_token = get_access_token()
    # print(f"Access Token: {access_token}")

    # Make a test API call to get Schwab profile information
    # profile = get_schwab_profile(access_token)
    # if profile:
    #     print("Schwab Profile Information:")
    #     print(profile)
    # else:
    #     print("Failed to retrieve Schwab profile information.")

    # print(get_movers(access_token))
    print(get_price_history(access_token))
