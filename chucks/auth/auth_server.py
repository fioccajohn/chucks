#!/usr/bin/env python
from flask import Flask, request, redirect, jsonify
from oauth import OAuth2Auth
# import logging

app = Flask(__name__)
oauth2_auth = OAuth2Auth('./chucks/auth/config.json')

# # Setup logging
# logging.basicConfig(level=logging.DEBUG)

# TODO jf this may be unnecessary.
@app.route('/')
def index():
    auth_url = oauth2_auth.get_authorization_url()
    app.logger.debug(f"Redirecting to auth URL: {auth_url}")
    return redirect(auth_url)

@app.route('/callback')
def callback():
    authorization_response = request.url
    code = request.args.get('code')
    state = request.args.get('state')
    app.logger.debug(f"Authorization code: {code}")
    app.logger.debug(f"State: {state}")
    
    try:
        token = oauth2_auth.fetch_token(authorization_response)
        app.logger.debug(f"Fetched token: {token}")
        return jsonify({"Access Token": token['access_token']})
    except Exception as e:
        app.logger.error(f"Error fetching token: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8182, ssl_context=('./chucks/auth/cert.pem', './chucks/auth/key.pem'))
