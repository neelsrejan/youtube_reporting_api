import os
import json
import requests
from datetime import date
from report_types import Report_Types
from create_jobs import Create_Jobs
from check_jobs import Check_Jobs
from get_reports import Get_Reports
from download_reports import Download_Reports
from delete_jobs import Delete_Jobs
from convert_csv_to_excel import Convert_Csv_To_Excel

class YT_REPORTING(Report_Types, Create_Jobs, Check_Jobs, Get_Reports, Download_Reports, Delete_Jobs, Convert_Csv_To_Excel):

    def __init__(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        self.SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly",
                "https://www.googleapis.com/auth/yt-analytics-monetary.readonly"
                ]
        self.API_SERVICE_NAME = 'youtubereporting'
        self.API_VERSION = 'v1'
        self.CLIENT_SECRETS_FILE = os.path.join(os.getcwd(), "secrets.json")
        self.youtube_reporting = None
        self.channel_name = None
        self.date = date.today()
        self.last_date = None
        self.report_types_list = []
        self.queued_jobs = []
        self.job_ids = []
        self.report_urls = []
        self.num_requests = 0

    def get_channel_name(self):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId={self.channel_id}&key={self.API_KEY}"
        self.channel_name = json.loads(requests.get(url).text)["items"][0]["snippet"]["channelTitle"].replace(" ", "_")
        return
