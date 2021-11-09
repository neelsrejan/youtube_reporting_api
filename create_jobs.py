from auth import Auth

class Create_Jobs(Auth):

    def create_jobs(self, to_create):
        if len(to_create) == 0:
            return
        else:
            for job in to_create:
                reporting_job = self.youtube_reporting.jobs().create(
                    body=dict(
                      reportTypeId=job[0],
                      name=job[1]
                    )
                  ).execute()
