# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:56:27 2020

@author: KarlN
"""
class tickers:
    def __init__(self, tkr0):
        self.tkr0 = tkr0

    def ticker_data(self):
        """ This function is a data handler for producing clean dataframes from
        the tkr_data.csv (the main data that is scraped form Yahoo! Finance). 
        It opens the data file provided by the data scraper,
        pulls the ticker, sets a datetime column and makes a datetime index. It 
        does not integrate the covid data"""
        
        import pandas as pd
        df = pd.read_csv('    ')
        #print(list(df))
        #['high', 'low', 'open', 'close', 'volume', 'adjustedclose', 'ticker', 'DateStamp', 
        # 'Industry', 'Sector', 'Country', 'Commodity']

        # Create a column from the datetime variable
        df = df[df['ticker'] == self.tkr0 ]
        df['Date_reported'] = df['DateStamp']
        df['DateStamp'] = pd.to_datetime(df['DateStamp'])
        df.index = df['DateStamp']

        return df



class row_data:

    def __init__(self, tkr1, cov):
        self.tkr1 = tkr1
        self.cov = cov
                
    def row_cov_data(self): 
        import pandas as pd
        """This function is a data handler for producing clean dataframes from
        the tkr_data.csv (the main data that is scraped form Yahoo! Finance) 
        and the CoVid data.
        
        It opens the data file provided by the data scraper,
        pulls the ticker, sets a datetime column and makes a datetime index.         

        It opens up the covid data file, and sums the daily by country data 
        to daily world data. 
        
        it zips the tkr data and the CoVid data and sets the DateStamp as index"""

        ##################
        # Tickers
        ##################

        df = pd.read_csv('tkr_data.csv')
        #print(list(df))
        #['high', 'low', 'open', 'close', 'volume', 'adjustedclose', 'ticker', 'DateStamp', 
        # 'Industry', 'Sector', 'Country', 'Commodity']

        # Create a column from the datetime variable
        df = df[df['ticker'] == self.tkr1 ]
        print('tkr from class',  self.tkr1)
        df['Date_reported'] = df['DateStamp']
        df['DateStamp'] = pd.to_datetime(df['DateStamp'])
        df.index = df['DateStamp']
        
    
        ##################
        # COVID
        ##################
    
        df_cov = pd.read_csv('WHO-COVID-19-global-data.csv')
        df_cov['DateStamp'] = df_cov['Date_reported']
        df_cov['DateStamp'] = pd.to_datetime(df_cov['DateStamp'])
        df_cov.index = df_cov['DateStamp']
    
        #cols = list(df_cov)
        #'Date_reported', 'Country_code', 'Country', 'WHO_region', 'New_cases', 
        #'Cumulative_cases', 'New_deaths', 'Cumulative_deaths'
        #print(cols)
    
        df_cov_agg = df_cov.resample('d').sum()
    
        x = df_cov_agg.index
        y = df_cov_agg[self.cov]
    
        df = df[df.index >= df_cov_agg.index.min() ]
        print('df shape:',df.shape)
        df = df[df.index <= df_cov_agg.index.max() ]
        print('df shape:',df.shape)
    
        x = df['close']
        y = df_cov_agg[self.cov]
        x = df['close']. values. tolist()
    
        #print('x', max(x))
        y = df_cov_agg['New_cases']. values. tolist()
        df_cross = pd.DataFrame(zip(x,y), columns = [self.tkr1+'_Close', self.cov]) 
        dates = df.index.tolist()
        df_cross['DateStamp'] = dates
        df_cross['DateStamp'] = pd.to_datetime(df_cross['DateStamp'])
        df_cross = df_cross.set_index(pd.DatetimeIndex(df_cross['DateStamp']))
        df_cross['WeekNum'] = df.index.week
        #df_cross.to_csv('cross_data.csv', index=True)
        print('Done')
        #print(type(df_cross))
        #print(df_cross)
        return df_cross
