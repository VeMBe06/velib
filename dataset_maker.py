"""
The goal of this script is to call the Velib API periodically to get the real time information of the stations.
The goal is to create a dataset of velib information spanning one week, from monday 00h00 to sunday 23h59 with information
of stations every 15-30mn (average trip should be about 15mn so maybe going for 15 could be smart).
"""

# Imports
import os
import requests
import time
from schedule import every, repeat, run_pending
import pandas as pd



def get_current_stations_status() -> dict:
    """
    Sends get request to velib api and rerceives station data.
    Returns the correct info from the api call
    """

    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"

    response = requests.get(url).json()
    result = response['data']['stations']


    return result


def add_to_dataset(data:dict) -> None:
    """
    Processes the data received by get_current_sations_status() and appends it to csv file.
    If no csv file exists yet, creates the csv file and writes the new data to it.
    """

    # Put data into df
    df = pd.DataFrame(data)

    # Extract bike info from num_bikes_available_types and put into separate columns
    df[['num_bikes_available_mechanical', 'num_bikes_available_ebike']] = pd.DataFrame(df['num_bikes_available_types'].tolist(),
                                                                                   columns = ['num_bikes_available_mechanical', 'num_bikes_available_ebike'])
    df['num_bikes_available_mechanical'] = df['num_bikes_available_mechanical'].apply( lambda x: x.get('mechanical'))
    df['num_bikes_available_ebike'] = df['num_bikes_available_ebike'].apply( lambda x: x.get('ebike'))

    # Drop unnecessary columns
    df.drop(columns=['num_bikes_available_types', 'numBikesAvailable', 'numDocksAvailable'], inplace=True)

    # Replace timestamp with a unique value to make it easy later on
    df['last_reported'] =  df['last_reported'].median().astype(int)

    # change column order
    df_final = df[['stationCode', 'station_id', 'num_bikes_available',
               'num_bikes_available_mechanical', 'num_bikes_available_ebike',
               'num_docks_available', 'is_installed', 'is_returning', 'is_renting',
               'last_reported']]

    # Write to csv
    if not os.path.isfile("data/velib_data.csv"):
        # If csv file doesn't exist, create it
        df_final.to_csv("data/velib_data.csv", mode='w', index=False, header=True)
    else:
        # If csv file alreay exists then append to it
        df_final.to_csv("data/velib_data.csv", mode='a', index=False, header=False)

    return None

# @repeat(every(15).seconds)
def scrape():
    """
    Puts everything together. Calls functions to get api response and write to csv.
    """
    # Print current time for logs
    t = time.localtime()
    current_time = time.strftime("%b-%d; %H:%M:%S", t)
    print(f"Starting scraping. TIMESTAMP-> {current_time}")
    # Send api request
    data = get_current_stations_status()
    # Process data and write to csv
    add_to_dataset(data)
    print('DONE')

    return None


# Schedule at every quarter hour
every().hour.at(":00").do(scrape)
every().hour.at(":15").do(scrape)
every().hour.at(":30").do(scrape)
every().hour.at(":45").do(scrape)


if __name__ == '__main__':

    # # For tests purposes
    # tmp = get_current_stations_status()
    # print(type(tmp))
    # print(tmp)
    print("Starting script")

    while True:
        run_pending()
        time.sleep(1)
        pass
