import os
from auth import Auth
from googleapiclient.http import MediaIoBaseDownload
from io import FileIO

class Download_Reports(Auth):

    def download_reports(self, day, job):
        
        local_file = os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{day}", "csv", f"{job[1]}",  f"{job[2].lower().replace(' ', '_')}.csv")
        
        for report_url in self.report_urls:
            request = self.youtube_reporting.media().download(
                        resourceName=' '
                          )
            request.uri = report_url
            fh = FileIO(local_file, mode='wb')
            downloader = MediaIoBaseDownload(fh, request, chunksize=-1)

            done = False
            while done is False:
                status, done = downloader.next_chunk()
