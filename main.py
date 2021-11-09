import os
import shutil
import time
from datetime import date, timedelta
from YT_REPORTING import YT_REPORTING
from urllib.error import HTTPError

def main():

    # Intro to program
    print("Welcome to the Youtube Reporting API!")
    print("\nThis program is intended for you to be able to get as much raw data from the youtube reporting api, to do so for various kinds of reports I will be asking for responses in order to properly get the information you wish to get.")

    # Get all information to filter on 
    API_KEY = input("Please enter your API KEY: ").strip()
    channel_id = "UCWPXl--e3JsJxRG64Of_msA" #input("Please enter your channel id: ").strip()

    YT = YT_REPORTING(API_KEY, channel_id)
    YT.get_channel_name()

    #Get list of all possible reports available
    YT.auth()
    YT.get_report_types()
    
    #Check if all possible report types have jobs made for them
    YT.check_jobs()
    
    to_create = []
    already_made = [report[1] for report in YT.queued_jobs]
    for i in range(len(YT.report_types_list)):
        if YT.report_types_list[i][0] not in already_made:
            to_create.apend(YT.report_types_list[i])
        
    #Create all jobs
    YT.create_jobs(to_create)

    #Create directoies for data when ready
    if not os.path.exists(os.path.join(os.getcwd(), f"{YT.channel_name}_data")):
        YT.last_date = YT.date
        data_categories = [report[0] for report in YT.report_types_list]
        for category in data_categories:
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}", "raw", f"{category}"))
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}", "clean", "csv", f"{category}"))
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}", "clean", "excel", f"{category}"))
        print("Since this is your first time creating jobs for your channel, the program will end now, please rerun program in 2 days from not to ensure youtube has your data ready for you!")
        quit()

    else:
        dates = os.listdir(os.path.join(os.getcwd(), f"{YT.channel_name}_data"))
        for day in dates:
            year, month, day = [int(i) for i in day.split("-")]
            new_date = date(year, month, day)
            if YT.last_date is None or YT.last_date < new_date:
                if new_date != YT.date:
                    YT.last_date = new_date
        delta = YT.date - YT.last_date
        data_categories = [report[0] for report in YT.report_types_list]

        data_for_dates = [str(YT.last_date)]
        for i in range(1, delta.days + 1):
            date_dir = str(YT.last_date + timedelta(days=i))
            data_for_dates.append(date_dir)
            for category in data_categories:
                os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date_dir}", "raw", f"{category}"))
                os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date_dir}", "clean", "csv", f"{category}"))
                os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date_dir}", "clean", "excel", f"{category}"))
        data_for_dates = data_for_dates[:-1]
        print(data_for_dates)
        for day in data_for_dates:
            for job in YT.queued_jobs:
                if YT.num_requests / 29 < 1:
                    YT.num_requests += 1
                    YT.get_reports(job, day)
                    YT.download_reports(day, job)
                else:
                    time.sleep(60)
                    YT.num_requests = 0
                    YT.num_requests += 1
                    YT.get_reports(job, day)
                    YT.download_reports(day, job)


if __name__ == "__main__":
    main()
