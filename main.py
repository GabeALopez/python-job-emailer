from api.api_client import APIClient
import pandas as pd
from dateutil import parser
from datetime import datetime, timedelta

def process_data(key, value_data):
    match key:
            case 'devitjobs':
                print("devitjobs")
                for value in value_data:
                    tech_category = value.get('techCategory','')
                    active_from = value.get('activeFrom','')
                    parsed_timestamp = parser.isoparse(active_from)

                    current_time = datetime.now(parsed_timestamp.tzinfo)

                    time_difference = current_time - parsed_timestamp

                    if time_difference >= timedelta(days=30):
                        continue

                    if 'IT' in tech_category:
                        print(value.get('_id',''))
                        print(value.get('jobUrl',''))
                        print(value.get('name',''))
                        print(tech_category)
                        print("")
                    if 'Python' in tech_category:
                        print(value.get('_id',''))
                        print(value.get('jobUrl',''))
                        print(value.get('name',''))
                        print(tech_category)
                        print("")
                    if 'C++' in tech_category:
                        print(value.get('_id',''))
                        print(value.get('jobUrl',''))
                        print(value.get('name',''))
                        print(tech_category)
                        print("")
                    if 'Security' in tech_category:
                        print(value.get('_id',''))
                        print(value.get('jobUrl',''))
                        print(value.get('name',''))
                        print(tech_category)
                        print("")
                    if 'DevOps' in tech_category:
                        print(value.get('_id',''))
                        print(value.get('jobUrl',''))
                        print(value.get('name',''))
                        print(tech_category)
                        print("")
                    
                
            case _:
                print("Nothing")

def main():
    api_dict = {}

    df = pd.read_csv('config/api_info.csv')

    for row in df.itertuples(index=False):
        api_dict[row.website] = APIClient(row.url, row.api_key, row.header)

    for key, value in api_dict.items():
        value_data = value.get_data()
        process_data(key, value_data)

if __name__ == "__main__":
    main()