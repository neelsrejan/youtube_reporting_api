from auth import Auth

class Report_Types(Auth):

    def get_report_types(self):
        results = self.youtube_reporting.reportTypes().list().execute()
        if len(results["reportTypes"]) != 0:
            self.report_types_list = [[report["id"], report["name"]] for report in results["reportTypes"]]
