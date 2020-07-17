''' This file will be for classes that we use to extract and clean the data from turnstiles '''
import pandas as pd

# This class can later be changed or augmented to retrieve from realtime or a different database
class TurnstileExtractor(object):
    table = None
    
    # private var that we will use to keep track of point in time data to load
    __times_retrieved = None


    def __init__(self, table_file):
        self.table = pd.read_csv(table_file)
        self.__times_retrieved = 0


    # get the simulated next minute of data (would be db later)
    def  retrieve_next_minute(self):
        # need to get the data into a json object array
        df = self.table
        # DB in this case will be formatted so that we have the times starting at 0
        # and going up in minute increment
        mask = df['retrieve_time'] == self.__times_retrieved
        df = df[mask]
        
        # let's drop the unnecessary columns and get our df with columns turnstile_id, group_id, turn_count, tunr_rate
        df = self._post_process(df)

        self.__times_retrieved += 1

        return df.to_json(orient='records')

    # method that formats into the table format html expects
    def _post_process(self, df):
        return df.drop(columns=['Unit', 'SCP', 'retrieve_time'])

