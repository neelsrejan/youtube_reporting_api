import os
import pandas as pd

class Convert_Csv_To_Excel():

    def convert_csv_to_excel(self, day, job):

        csv_file = pd.read_csv(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{day}", "csv", f"{job[1]}", f"{job[2].lower().replace(' ', '_')}.csv"))
        csv_file.to_excel(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{day}", "excel", f"{job[1]}", f"{job[2].lower().replace(' ', '_')}.xlsx"), index=False)
