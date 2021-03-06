# Welcome to the Youtube Reporting Api

## Abstract
This program is set for a user to use the youtube reporting api to get bulk data for their own youtube channel. In order to run this program the user must have a google colsole account and create a project with an OAuth2 secret file being made through the console. In addition an API Key for the youtube data api. Both API's the reporting and data api must be enabled for this program to work. Other than the authentication, the user just has to be able to use python to run the script from terminal. The progam files should be saved into a folder where the user is comfortable for files to be downloaded to as the program creates directories and subdirectories to save data into. 

## Methodology
To use the code, clone the repo, into the file of choice. Download and remane your OAuth secret file as secrets.json in the same folder as the main.py. Run the program, enter the Youtube Data API Key to get the channel name. The program then proceeds to ask for authentication where one copy and pastes the authorization code through a popup browser. Once authenticated the progam will check which reports can be generated for the youtube channel, check if previous reports have been made for the channel, create jobs for new reports that havent been made. If this is the first time running the program the program will end and ask to rerun in two days as youtube needs two days to first make reports for new jobs. Once the program is run again, the program then makes new folders for days missed by running and will make calls to get the data for the given 1 day time period of each daily report that is made. The program, since youtube only makes reports until the previous day will have data as recent as the day before. These files are saved into the corresponding folders as a csv/excel file for you to analysize and see.

## Warnings
The program does not store your API KEY, nor does it see the contents of your secrets.json file. The program does add folders to your local system in which data gathered will be stored. If you wish to use the program, just know that it is up to you to ensure the main.py file is in a location you wish to run it.

## Thank you for checking my project out!
