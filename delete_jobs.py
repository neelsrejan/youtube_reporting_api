from auth import Auth

class Delete_Jobs(Auth):

    def delete_jobs(self):
        for job_id in self.job_ids:
            self.youtube_reporting.jobs().delete(
                jobId=f"{job_id}"
                    ).execute()
