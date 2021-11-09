from auth import Auth
from datetime import date, timedelta

class Get_Reports(Auth):

    def get_reports(self, job, date_dir):
        year, month, day = [int (i) for i in date_dir.split("-")]
        date_dir = date(year, month, day)
        created_after = str(date_dir - timedelta(days=1)) + "T00:00:00.000000Z"
        results = self.youtube_reporting.jobs().reports().list(
                    jobId=f"{job[0]}",
                    createdAfter=f"{created_after}"
                        ).execute()
        year, month, day = [int(i) for i in created_after[:10].split("-")]
        created_after = date(year, month, day)
        reports_per_day = []
        for report in results["reports"]:
            start_time = report["startTime"]
            year, month, day = [int(i) for i in start_time[:10].split("-")]
            start_time = date(year, month, day)
            if created_after <= start_time and start_time < date_dir:
                reports_per_day.append(report)
        print(reports_per_day)
        self.report_urls = [job_url["downloadUrl"] for job_url in reports_per_day]
