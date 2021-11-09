from auth import Auth

class Check_Jobs(Auth):

    def check_jobs(self):
        results = self.youtube_reporting.jobs().list().execute()
        if len(results["jobs"]) != 0:
            self.queued_jobs = [[job["id"], job["reportTypeId"], job["name"], job["createTime"]] for job in results["jobs"]]
