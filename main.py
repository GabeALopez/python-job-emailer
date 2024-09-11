from api.api_client import APIClient
import pandas as pd
from dateutil import parser
from datetime import datetime, timedelta

#TODO: Refactor function to fit somewhere else. This is too cluttering
#Function to process api data
def process_data(key, value_data):
    match key:
            case 'devitjobs':
                for value in value_data:
                    tech_category = value.get('techCategory','')
                    active_from = value.get('activeFrom','')
                    parsed_timestamp = parser.isoparse(active_from)

                    current_time = datetime.now(parsed_timestamp.tzinfo)

                    time_difference = current_time - parsed_timestamp

                    if time_difference >= timedelta(days=30):
                        continue

                    if 'Senior' in value.get('expLevel',''):
                        continue
                    
                    if 'Senior' in value.get('name','') or 'Sr' in value.get('name',''):
                        continue

                    categories = ['IT', 'Security', 'DevOps']

                    #TODO: Figure out what to do with data
                    for category in categories:
                        if category in tech_category:
                            print(value.get('jobUrl', ''))
                            print(value.get('name', ''))
                            print(tech_category)
                            print("")
                                        
            case _:
                print("Nothing")

def main():
    api_dict = {}

    #Read csv file of APIs
    df = pd.read_csv('config/api_info.csv')

    #Create APIClient object for each API
    for row in df.itertuples(index=False):
        api_dict[row.website] = APIClient(row.url, row.api_key, row.header)

    #Get data from each API and process it
    for key, value in api_dict.items():
        value_data = value.get_data()
        process_data(key, value_data)

if __name__ == "__main__":
    main()