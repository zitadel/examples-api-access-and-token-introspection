from os import environ as env
import os
import time
from typing import Dict

from authlib.oauth2.rfc7662 import IntrospectTokenValidator
import requests
from dotenv import load_dotenv, find_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

ZITADEL_DOMAIN = os.getenv("ZITADEL_DOMAIN")
ZITADEL_INTROSPECTION_URL = os.getenv("ZITADEL_INTROSPECTION_URL")
API_CLIENT_ID = os.getenv("API_CLIENT_ID")
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")


class ValidatorError(Exception):

    def __init__(self, error: Dict[str, str], status_code: int):
        super().__init__()
        self.error = error
        self.status_code = status_code

class ZitadelIntrospectTokenValidator(IntrospectTokenValidator):
    def introspect_token(self, token_string):
        url =  ZITADEL_INTROSPECTION_URL
        data = {'token': token_string, 'token_type_hint': 'access_token', 'scope': 'openid'}
        auth = HTTPBasicAuth(API_CLIENT_ID, API_CLIENT_SECRET)
        resp = requests.post(url, data=data, auth=auth)
        resp.raise_for_status()
        return resp.json()
    
    # def match_token_scopes(self, token, or_scopes):
    #     if or_scopes is None: 
    #         return True
    #     roles = token["urn:zitadel:iam:org:project:roles"].keys()
    #     for and_scopes in or_scopes:
    #         scopes = and_scopes.split()
    #         """print(f"Check if all {scopes} are in {roles}")"""
    #         if all(key in roles for key in scopes):
    #             return True
    #     return False

    def match_token_scopes(self, token, or_scopes):
        if or_scopes is None:
            return True
        scopes = token.get("scope", "").split()
        for and_scopes in or_scopes:
            if all(key in scopes for key in and_scopes.split()):
                return True
        return False       

    def validate_token(self, token, scopes, request):
        print(f"Token: {token}\n")
        now = int(time.time())
        if not token:
            raise ValidatorError({
                "code": "invalid_token_revoked",
                "description": "Token was revoked."
            }, 401)
        if token["exp"] < now:
            raise ValidatorError({
                "code": "invalid_token_expired",
                "description": "Token has expired."
            }, 401)
        if not token.get("active"):
            raise ValidatorError({
                "code": "invalid_token_inactive",
                "description": "Token is inactive."
            }, 401)
        if not self.match_token_scopes(token, scopes):
            raise ValidatorError({
                "code": "insufficient_scope",
                "description": f"Token has insufficient scope. Route requires: {scopes}"
            }, 401)


    def __call__(self, *args, **kwargs):
        res = self.introspect_token(*args, **kwargs)
        return res