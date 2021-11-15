from auth import Auth
from datetime import date, timedelta

class Get_Reports(Auth):

    def get_reports(self, job, date_dir):
        
        year, month, day = [int (i) for i in date_dir.split("-")]
        date_dir = date(year, month, day)
        
        start_time_at_or_after = str(date_dir) + "T00:00:00.000000Z"
        end_time = str(date_dir + timedelta(days=1)) + "T00:00:00.0000001Z"
        
        results = self.youtube_reporting.jobs().reports().list(
                    jobId=f"{job[0]}",
                    startTimeAtOrAfter=f"{start_time_at_or_after}",
                    startTimeBefore=f"{end_time}"
                        ).execute()
        reports_per_day = []
        if results:
            for report in results["reports"]:
                reports_per_day.append(report)
            self.report_urls = [job_url["downloadUrl"] for job_url in reports_per_day]
