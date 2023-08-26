# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:28:36 2022

@author: ramak
"""

import math
import pandas as pd
from datetime import datetime, timedelta,date
import numpy as np
from dateutil.relativedelta import relativedelta

import streamlit as st
st.set_page_config(layout="wide")

#d = date(2023, 8, 6)

d = st.date_input("Current Date", date.today())
d1f=d
d= d - relativedelta(months=1)
# Find the start date of the month
start_date = d.replace(day=1)

# Calculate the number of days in the month
days_in_month = (start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(days=1)).day

# Find the end date of the month
end_date = start_date.replace(day=days_in_month)

print("Start date:", start_date)
print("End date:", end_date)
#t = investpy.get_index_historical_data(index='Nifty Bank',country="India", from_date=str(todate), to_date=str(d))
option1 = st.selectbox('EXCHANGE',['NSE','MCX'])




def maindaydata2():
    import pandas as pd
    import requests
    global start_date,end_date
    
    # Define the base URL
    base_url = 'https://archives.nseindia.com/products/content/sec_bhavdata_full_'
    today = end_date
    pastdate=start_date
    # Format today's date as 'YYYY-MM-DD'
    formatted_date = today.strftime('%Y-%m-%d')

    formatted_date1 = pastdate.strftime('%Y-%m-%d')
    # Define the start and end dates for the loop
    start_date = pd.Timestamp(formatted_date1)
    end_date = pd.Timestamp(formatted_date)
    
    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()
    
    # Loop through the dates
    current_date = start_date
    while current_date <= end_date:
        # Format the date into the desired string format
        date_str = current_date.strftime('%Y%m%d')
        print(date_str)
    
        # Construct the URL for the current date
        #url = base_url + date_str + '.csv'
    
        # Send a GET request to the URL
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.mcxindia.com',
            'Referer': 'https://www.mcxindia.com/market-data/bhavcopy',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        a="{'Date':'"
        b="','InstrumentName':'ALL'}"
        c=a+date_str+b
        #print(c)
        data=c
        #data = "{'Date':'20230524','InstrumentName':'ALL'}"
        

        response = requests.post('https://www.mcxindia.com/backpage.aspx/GetDateWiseBhavCopy',  headers=headers, data=data)

        # Check the status code
        print(response.status_code)
        if response.status_code == 200:
            # Read the CSV data into a DataFrame
            print('done')
            j=response.json()

            df=pd.DataFrame(j['d']['Data'])

            # Merge the current DataFrame with the merged DataFrame
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    
        # Increase the current date by one day
        current_date += pd.DateOffset(days=1)
        print(current_date)
    
    # Print the merged DataFrame
    #print(merged_df.columns)
    merged_df=merged_df[merged_df['OptionType']=='-']
    
    merged_df['Date']=pd.to_datetime(merged_df['Date'],dayfirst=False,yearfirst=False)
    merged_df['Name']=merged_df['Symbol']+merged_df['ExpiryDate']
    merged_df['Open']=merged_df['Open'].astype(float)
    merged_df['High']=merged_df['High'].apply(float)
    merged_df['Low']=merged_df['Low'].apply(float)
    merged_df['Close']=merged_df['Close'].apply(float)
    merged_df=merged_df[['Date','Open','High','Low','Close','Name','Symbol']]
    #df=merged_df[merged_df['Name']==sym]
    return merged_df

if option1=='NSE':
    dr=pd.read_csv('sec_bhavdata_full_23082023.csv')
    symbol=list(dr['SYMBOL'])
    symbol.extend(['NIFTY BANK','NIFTY 50'])
    option = st.selectbox('Symbol',symbol)
else:
    dr=maindaydata2()
    symbol=list(dr['Name'].unique())[::-1]
    option = st.selectbox('Symbol',symbol)
    df=dr[dr['Name']==option]
    
def maindaydata():
    import pandas as pd
    import requests
    global start_date,end_date
    
    # Define the base URL
    base_url = 'https://archives.nseindia.com/content/indices/ind_close_all_'
    today = end_date
    pastdate=start_date
    # Format today's date as 'YYYY-MM-DD'
    formatted_date = today.strftime('%Y-%m-%d')

    formatted_date1 = pastdate.strftime('%Y-%m-%d')
    # Define the start and end dates for the loop
    start_date = pd.Timestamp(formatted_date1)
    end_date = pd.Timestamp(formatted_date)
    
    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()
    
    # Loop through the dates
    current_date = start_date
    while current_date <= end_date:
        # Format the date into the desired string format
        date_str = current_date.strftime('%d%m%Y')
        print(date_str)
    
        # Construct the URL for the current date
        url = base_url + date_str + '.csv'
    
        # Send a GET request to the URL
        response = requests.get(url, allow_redirects=False)
    
        # Check the status code
        if response.status_code == 200:
            # Read the CSV data into a DataFrame
            print('done')
            df = pd.read_csv(url)
    
            # Merge the current DataFrame with the merged DataFrame
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    
        # Increase the current date by one day
        current_date += pd.DateOffset(days=1)
        print(current_date)
    
    # Print the merged DataFrame
    merged_df=merged_df[merged_df['Open Index Value']!='-']
    merged_df['Date']=pd.to_datetime(merged_df['Index Date'],dayfirst=True)
    merged_df['Open']=merged_df['Open Index Value'].astype(float)
    merged_df['High']=merged_df['High Index Value'].apply(float)
    merged_df['Low']=merged_df['Low Index Value'].apply(float)
    merged_df['Close']=merged_df['Closing Index Value'].apply(float)
    merged_df['Name']=merged_df['Index Name']
    merged_df=merged_df[['Date','Open','High','Low','Close','Name']]
    nifty50=merged_df[merged_df['Name']=='Nifty 50']
    niftybank=merged_df[merged_df['Name']=='Nifty Bank']
    return nifty50,niftybank


def maindaydata1(sym):
    import pandas as pd
    import requests
    global start_date,end_date
    
    # Define the base URL
    base_url = 'https://archives.nseindia.com/products/content/sec_bhavdata_full_'
    today = end_date
    pastdate=start_date
    # Format today's date as 'YYYY-MM-DD'
    formatted_date = today.strftime('%Y-%m-%d')

    formatted_date1 = pastdate.strftime('%Y-%m-%d')
    # Define the start and end dates for the loop
    start_date = pd.Timestamp(formatted_date1)
    end_date = pd.Timestamp(formatted_date)
    
    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()
    
    # Loop through the dates
    current_date = start_date
    while current_date <= end_date:
        # Format the date into the desired string format
        date_str = current_date.strftime('%d%m%Y')
        print(date_str)
    
        # Construct the URL for the current date
        url = base_url + date_str + '.csv'
    
        # Send a GET request to the URL
        response = requests.get(url, allow_redirects=False)
    
        # Check the status code
        if response.status_code == 200:
            # Read the CSV data into a DataFrame
            print('done')
            df = pd.read_csv(url)
    
            # Merge the current DataFrame with the merged DataFrame
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    
        # Increase the current date by one day
        current_date += pd.DateOffset(days=1)
        print(current_date)
    
    # Print the merged DataFrame
    #print(merged_df.columns)
    merged_df=merged_df[merged_df[' OPEN_PRICE']!='-']
    merged_df['Date']=pd.to_datetime(merged_df[' DATE1'],dayfirst=True)
    merged_df['Open']=merged_df[' OPEN_PRICE'].astype(float)
    merged_df['High']=merged_df[' HIGH_PRICE'].apply(float)
    merged_df['Low']=merged_df[' LOW_PRICE'].apply(float)
    merged_df['Close']=merged_df[' CLOSE_PRICE'].apply(float)
    merged_df['Name']=merged_df['SYMBOL']
    merged_df=merged_df[['Date','Open','High','Low','Close','Name']]
    df=merged_df[merged_df['Name']==sym]
    return df

if option1=='NSE':
    if option in ['NIFTY BANK','NIFTY 50']:
        nifty,banknifty=maindaydata()
        if option =='NIFTY BANK':
            df=banknifty
        else:
            df=nifty
            
    else:
        df=maindaydata1(option)

#t=niftybank
t=df
t=t.set_index(['Date'])
print(t)


maxh=t['High'].max()
minh=t['Low'].min()


maxhdate=t.index[t['High']==maxh].to_list()[0]

minhdate=t.index[t['Low']==minh].to_list()[0]
t=t.reset_index()
maxhindex=t.index[t['High']==maxh].to_list()[0]

minhindex=t.index[t['Low']==minh].to_list()[0]

tradeday=abs(minhindex-maxhindex)+1

calenderdate=abs(maxhdate.day-minhdate.day)+1
#print(calenderdate)
maxmod=((math.sqrt(maxh))*180-225)%360
minmod=((math.sqrt(minh))*180-225)%360
calenderdatemod=((math.sqrt(calenderdate))*180-225)%360
tradedaymod=((math.sqrt(tradeday))*180-225)%360

maxdeg=max([maxmod,minmod,calenderdatemod,tradedaymod])#.max()
mindeg=min([maxmod,minmod,calenderdatemod,tradedaymod])#.min()

max1=round((2+((2*maxdeg)/360)+1.25)**2,6)
max2=(4+((2*maxdeg)/360)+1.25)**2
max3=(6+((2*maxdeg)/360)+1.25)**2


min1=(2+(2*mindeg)/360+1.25)**2
min2=(4+(2*mindeg)/360+1.25)**2
min3=(6+(2*mindeg)/360+1.25)**2

maxdate1=max([maxhdate,minhdate])+timedelta(days=round(max1))
maxdate2=max([maxhdate,minhdate])+timedelta(days=round(max2))
maxdate3=max([maxhdate,minhdate])+timedelta(days=round(max3))
mindate1=min([maxhdate,minhdate])+timedelta(days=round(max1))
mindate2=min([maxhdate,minhdate])+timedelta(days=round(max2))
mindate3=min([maxhdate,minhdate])+timedelta(days=round(max3))

maxdate_1=max([maxhdate,minhdate])+timedelta(days=round(min1))
maxdate_2=max([maxhdate,minhdate])+timedelta(days=round(min2))
maxdate_3=max([maxhdate,minhdate])+timedelta(days=round(min3))
mindate_1=min([maxhdate,minhdate])+timedelta(days=round(min1))
mindate_2=min([maxhdate,minhdate])+timedelta(days=round(min2))
mindate_3=min([maxhdate,minhdate])+timedelta(days=round(min3))

h1=[maxdate1.date(),maxdate2.date(),maxdate3.date(),maxdate_1.date(),maxdate_2.date(),maxdate_3.date(),
 mindate1.date(),mindate2.date(),mindate3.date(),mindate_1.date(),mindate_2.date(),mindate_3.date()]

##############technique 1 #####################


maxdeg=max([(math.sqrt((maxh-minh))*180-225)%360
,
tradedaymod
,calenderdatemod])

mindeg=min([(math.sqrt((maxh-minh))*180-225)%360
,
tradedaymod
,calenderdatemod])

max1=(2*1+(2*maxdeg)/360+1.25)**2
max2=(2*2+(2*maxdeg)/360+1.25)**2
max3=(2*3+(2*maxdeg)/360+1.25)**2

min1=(2*1+(2*mindeg)/360+1.25)**2
min2=(2*2+(2*mindeg)/360+1.25)**2
min3=(2*3+(2*mindeg)/360+1.25)**2


maxdate1=max([maxhdate,minhdate])+timedelta(days=(max1))
maxdate2=max([maxhdate,minhdate])+timedelta(days=(max2))
maxdate3=max([maxhdate,minhdate])+timedelta(days=(max3))
mindate1=min([maxhdate,minhdate])+timedelta(days=(max1))
mindate2=min([maxhdate,minhdate])+timedelta(days=(max2))
mindate3=min([maxhdate,minhdate])+timedelta(days=(max3))

maxdate_1=max([maxhdate,minhdate])+timedelta(days=(min1))
maxdate_2=max([maxhdate,minhdate])+timedelta(days=(min2))
maxdate_3=max([maxhdate,minhdate])+timedelta(days=(min3))
mindate_1=min([maxhdate,minhdate])+timedelta(days=(min1))
mindate_2=min([maxhdate,minhdate])+timedelta(days=(min2))
mindate_3=min([maxhdate,minhdate])+timedelta(days=(min3))

h2=[maxdate1.date(),maxdate2.date(),maxdate3.date(),maxdate_1.date(),maxdate_2.date(),maxdate_3.date(),
 mindate1.date(),mindate2.date(),mindate3.date(),mindate_1.date(),mindate_2.date(),mindate_3.date()]

##############technique 2 #####################

deg=((maxh/minh)*180)-180
min1=(2*1+(2*deg)/360+1.25)**2
min2=(2*2+(2*deg)/360+1.25)**2
min3=(2*3+(2*deg)/360+1.25)**2
min4=(2*4+(2*deg)/360+1.25)**2
min5=(2*5+(2*deg)/360+1.25)**2

maxdate1=max([maxhdate,minhdate])+timedelta(days=(min1))
maxdate2=max([maxhdate,minhdate])+timedelta(days=(min2))
maxdate3=max([maxhdate,minhdate])+timedelta(days=(min3))
maxdate4=max([maxhdate,minhdate])+timedelta(days=(min4))
maxdate5=max([maxhdate,minhdate])+timedelta(days=(min5))


mindate1=min([maxhdate,minhdate])+timedelta(days=(min1))
mindate2=min([maxhdate,minhdate])+timedelta(days=(min2))
mindate3=min([maxhdate,minhdate])+timedelta(days=(min3))
mindate4=min([maxhdate,minhdate])+timedelta(days=(min4))
mindate5=min([maxhdate,minhdate])+timedelta(days=(min5))


h3=[maxdate1.date(),maxdate2.date(),maxdate3.date(),maxdate_1.date(),maxdate_2.date(),maxdate_3.date(),
 mindate1.date(),mindate2.date(),mindate3.date(),mindate_1.date(),mindate_2.date(),mindate_3.date()]

##############technique 3 #####################

print(h1)
print(h2)
print(h3)
h5=[]
h5.extend(h1)
h5.extend(h2)
h5.extend(h3)
h4 = []
for i in h5:
    
    if i.month==d1f.month:
        print(True)
        print(i)
        h4.append(i)
#st.write(h1)
#st.write(h2)
#st.write(h3)
#st.write(h4)
print(h4)

from collections import Counter
date_counter = Counter(h4)

# Sort dates by initial date
sorted_dates = sorted(date_counter.items(), key=lambda x: x[0])

# Format and print the result
print("Date\t\tCount")
print("--------------------")
#st.write('Alert Level')
#st.error('Highest Level')
#st.warning('High Level')
#st.info('Medium Level')
#st.success('Low Level')
#st.write('All Dates for This Month')
strong=[]
weak=[]
for date, count in sorted_dates:
    #st.write(f"{date.strftime('%d-%B-%Y')}\t{count}")
    #if count >=4:
    #    st.error(f"{date.strftime('%d-%B-%Y')}")
    
    #if count ==3:
    #    st.warning(f"{date.strftime('%d-%B-%Y')}")
    #if count==2:
    #    st.info(f"{date.strftime('%d-%B-%Y')}")
    #if count==1:
    #    st.success(f"{date.strftime('%d-%B-%Y')}")
    if count==1:
       weak.append([f"{date.strftime('%d-%B-%Y')}" ,"1",f"{date.strftime('%A')}"]) 
    
    if count>1:
       strong.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
    
print(strong)
print(len(strong))
strong1=pd.DataFrame(strong,columns=['Major Trend Change Date','Major Trend','Major Weekday'])
print(weak)
print(len(weak))

weak1=pd.DataFrame(weak,columns=['Minor Date','Minor Trend','Minor Weekday'])
strong2=strong1
strong2['Minor Trend Change Date']=weak1['Minor Date']
strong2['Minor Trend']=weak1['Minor Trend']
strong2['Minor Weekday']=weak1['Minor Weekday']
print(strong2)
st.dataframe(strong2)       
        
