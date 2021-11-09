import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

class Auth():

    def get_authenticated_service(self):
        flow = InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRETS_FILE, self.SCOPES)
        credentials = flow.run_console()
        return build(self.API_SERVICE_NAME, self.API_VERSION, credentials = credentials)

    def auth(self):
        self.youtube_reporting = self.get_authenticated_service()

