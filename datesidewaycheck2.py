# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:28:36 2022

@author: ramak
"""
import json
import math
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta
import streamlit as st
from math import sqrt
from pandas import Timestamp
import math
import sqlite3
import requests
from datetime import datetime,timedelta,date
import datetime
st.set_page_config(layout="wide")
col1, col2,col3 = st.columns(3)
with col1:
    selected_date = st.date_input('Select a Date',date.today())
with col2:
    input_days=st.number_input(label='Days For Calucation',value=30,min_value=1,max_value=30)
with col3:
    option1 = st.selectbox('Indian EXCHANGE',['NSE','MCX','Index','CDS'])
start_date=selected_date-timedelta(days=25)
end_date=selected_date-timedelta(days=1)
start_date1=start_date
start_date2=start_date
end_date1=end_date
end_date2=selected_date

if option1=='NSE':
    dr=pd.read_csv('sec_bhavdata_full_23082023.csv')
    symbol=list(dr['SYMBOL'])
    #dr=maindaydata1(start_date,end_date)
    option = st.selectbox('Symbol for Nse ',symbol)    
elif option1=='Index':
    dr=pd.DataFrame()
    symbol=['NIFTY CONSUMPTION',
                'NIFTY FMCG',                 'INDIA VIX',                 'NIFTY METAL','NIFTY50 PR 1X INV',
                'NIFTY50 DIV POINT',                'NIFTY100 LIQ 15',
                'NIFTY50 TR 1X INV',            'NIFTY FINSRV25 50',
                'NIFTY BANK',                 'NIFTY PSU BANK',
                'NIFTY SERV SECTOR',                 'NIFTY GS 10YR CLN',
                'NIFTY GS 11 15YR',                 'NIFTY50 PR 2X LEV',
                'NIFTY 100',                 'NIFTY SMLCAP 250',
                'NIFTY SMLCAP 100',                 'NIFTY 500',
                'NIFTY MID LIQ 15',                 'NIFTY IND DIGITAL',
                'NIFTY DIV OPPS 50',                 'NIFTY MEDIA',
                'NIFTY REALTY',                 'NIFTY HEALTHCARE',
                'NIFTY NEXT 50',                 'NIFTY IT',
                'NIFTY PSE',                 'NIFTY GS COMPSITE',
                'NIFTY COMMODITIES',                 'NIFTY100 LOWVOL30',
                'NIFTY GS 10YR',                 'NIFTY PVT BANK',
                'NIFTY100 ESG',                 'NIFTY MICROCAP250',
                'NIFTY M150 QLTY50',                 'NIFTY SMLCAP 50',                 'NIFTY CPSE',                 'NIFTY50 EQL WGT',                 'NIFTY INDIA MFG',                 'NIFTY 50',                 'NIFTY100 EQL WGT',                 'NIFTY200 QUALTY30',                 'NIFTY200MOMENTM30',                 'NIFTY100ESGSECLDR',                 'NIFTY50 VALUE 20',                 'NIFTY100 QUALTY30',                 'NIFTY MIDSML 400',                 'NIFTY ALPHALOWVOL',                 'NIFTY CONSR DURBL',                 'NIFTY GS 8 13YR',                 'NIFTY MIDCAP 50',                 'NIFTY OIL AND GAS',                 'NIFTY MNC',                 'NIFTY MIDCAP 100',                 'NIFTY50 TR 2X LEV',                 'NIFTY GS 15YRPLUS',                 'NIFTY 200',                 'NIFTY PHARMA',                 'NIFTY LARGEMID250',                 'NIFTY MIDCAP 150',                 'NIFTY GS 4 8YR',                 'NIFTY AUTO',                 'NIFTY GROWSECT 15',                 'NIFTY FIN SERVICE',                 'NIFTY INFRA',                 'NIFTY MID SELECT',                 'NIFTY TOTAL MKT',                 'NIFTY500 MULTICAP',                 'NIFTY ENERGY',                 'NIFTY ALPHA 50'
                ]
    option = st.selectbox('Symbol For Index',symbol)
elif option1=='MCX':
    symbol=['ALUMINI',
 'ALUMINIUM',
 'COPPER',
 'COTTONCNDY',
 'CRUDEOIL',
 'CRUDEOILM',
 'GOLD',
 'GOLDGUINEA',
 'GOLDM',
 'GOLDPETAL',
 'KAPAS',
 'LEAD',
 'LEADMINI',
 'MCXBULLDEX',
 'MCXENRGDEX',
 'MCXMETLDEX',
 'MENTHAOIL',
 'NATGASMINI',
 'NATURALGAS',
 'NICKEL',
 'SILVER',
 'SILVERM',
 'SILVERMIC',
 'ZINC',
 'ZINCMINI']
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox('Symbol ',symbol)
    date_str = selected_date.strftime('%Y%m%d')
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


    #response = requests.post('https://www.mcxindia.com/backpage.aspx/GetDateWiseBhavCopy',  headers=headers, data=data)

    df=pd.DataFrame()
    #df=(pd.DataFrame(response.json()['d']['Data']))
    
    base_url = 'https://www.mcxindia.com/'
    #start_date = datetime.date(2023, 5, 1)  # Modify this to your desired start date

    # Define a function to check if a date is a weekend (Saturday or Sunday)
    def is_weekend(date):
        return date.weekday() >= 5  # 5 represents Saturday, 6 represents Sunday

    # Initialize an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Loop through dates
    current_date = selected_date
    while True:
        # Check if the current date is a weekend, and if not, proceed with the request
        if not is_weekend(current_date):
            date_str = current_date.strftime('%Y%m%d')
            print(date_str)

            # Construct the URL for the current date
            url = base_url + date_str + '.csv'
            
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

            data = {
                'Date': date_str,
                'InstrumentName': 'ALL'
            }

            response = requests.post('https://www.mcxindia.com/backpage.aspx/GetDateWiseBhavCopy', headers=headers, json=data)

            if response.status_code == 200:
                # Process the response data and append it to result_df
                df = pd.DataFrame(response.json()['d']['Data'])
                #result_df = pd.concat([result_df, current_data], ignore_index=True)
            else:
                print(f"Failed to fetch data for date: {date_str}")

        # Move to the next day
        current_date -= datetime.timedelta(days=1)

        # Stop the loop if you have fetched enough data or reached a specific end date
        if len(df) >0:
            break



    #st.dataframe(df)
    if not df.empty:
        df=df[df['OptionType']=='-']
        df['Symbol'] = df['Symbol'].str.strip()
        df1=list(df[df['Symbol']==option]['ExpiryDate'])
        with col2:
            expiry = st.selectbox('Expiry ',df1)
        #st.write(expiry)
elif option1=='CDS':
    symbols=['USDINR',"EURINR",'EURUSD','GBPINR','GBPUSD','JPYINR','USDJPY']
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox('Symbol ',symbols)
        
    import requests
    from datetime import datetime
    cookies = {

    }

    headers = {
        'authority': 'www.nseindia.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
    }
    
    # initialize a session
    session = requests.Session()
    
    # send a get request to the server
    response = session.get('https://www.nseindia.com/',cookies=cookies,
    headers=headers,)
    # print the response dictionary
    maincookie=(session.cookies.get_dict())



    headers = {
        'authority': 'www.nseindia.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'defaultLang=en; nseQuoteSymbols=[{"symbol":"SADBHAV","identifier":null,"type":"equity"},{"symbol":"ADANIENT","identifier":null,"type":"equity"},{"symbol":"ADANIGREEN","identifier":null,"type":"equity"},{"symbol":"NIFTY","identifier":null,"type":"equity"}]; AKA_A2=A; ak_bmsc=E5C0511535D7E8AFFB3120903EFBC9E7~000000000000000000000000000000~YAAQXydzaNh9a0mKAQAARhuKghU41sMB1ys0vToJEVMDI5c/ASIxBXXPLVp/1juGYJCBL3AzpFcpxJpOuUJwySLHYu7CS5Zea5g5v7O3uj3DYyq42oat2sM07t8Vi0v3bZYbr9RNLs0zAOhMk+L5xKxVNAznxV95DT3wR8/H00AhUWpi1Agm3yVOidyqe1r588pG/NCuNxMNnoL7AUhxiWhyjA36ZXl4IS6BmkPnKTT1wtVTjyAsnmIfgzImSsHZt6+lfm6ViKNImTfvqwOElYdrIpP/Z1gcKVQEMFApDGQpJmUB11QDlY/Ng7XfOTSAFodORsoa4Wl3Sh/isqTcDzH4QB2qzr8pWoUIuiT0aEwPm0wYFPkaH4aSMw9WwcYRWjla8nWHjowVFa9cX9kfXc/0V1qSvLjn1sBxx6WtwX11Ku2eIvEaTOeKoP9++q8NmPFw5SE8y3rmsi6kycT2IG63aIjrtCpBKzELef7R/67EXewbzopTOSxL17FLCkCeLQVHSw==; _gid=GA1.2.412291923.1694407207; nsit=DcGVOBs5rFJNtXEK8lC3Xorm; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY5NDQwODU1NiwiZXhwIjoxNjk0NDE1NzU2fQ.ebT17XQgpxeSz7cyvBWOODnJbzEZzuS4Hnslf-TILFI; _ga=GA1.2.1632056446.1694146307; _ga_PJSKY6CFJH=GS1.1.1694407204.15.1.1694408663.2.0.0; bm_sv=727C08A8A2C36DC06D41C86326369542~YAAQJSEPF9t9p06KAQAA8sSjghWFr3CTe4AtbxCx91PDLY9HgwAvuacw2fxHpNbC8Yghjbc9Thr5HHVbyj9WYQ9DcZ59g78Y6GO8eH7tRmggidrTNCacWj+TI8LoaZik98EW+rwaBjdS8ExSN3xHtJkgd6ss8+CMM5hCbWWB3aZg2E8hHqsMrRtR9wivZSvmgfrigN6S31M2mTNlw0JPL/n95CAZd+0/7PA1TTfBwNpaS6CpIwV0tzibq+nV4IiCLeb8zg==~1',
        'referer': 'https://www.nseindia.com/report-detail/cd_eq_security',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
    }

    params = {
        'instrument': 'FUTCUR',
        'symbol': option,
        'year': str(selected_date.year),
    }

    response = requests.get(
        'https://www.nseindia.com/api/historical/cdCPV/expireDtsv2',
        params=params,
        cookies=maincookie,
        headers=headers,
    )


    selected_date1 = datetime.combine(selected_date, datetime.min.time())
    def custom_key(date_str):
        return datetime.strptime(date_str, '%d-%b-%Y')

    # Sort the list using the custom key function
    #sorted_dates = sorted(response.json()['expireDts'], key=custom_key)
    upcoming_dates = [date for date in response.json()['expireDts'] if custom_key(date) >= selected_date1]

    # Sort the upcoming dates
    sorted_upcoming_dates = sorted(upcoming_dates, key=custom_key)

    with col2:
        expiry = st.selectbox('Expiry ',sorted_upcoming_dates)



    
#with col1:
#    start_date = st.date_input('Select Start date',start_date)
#
#with col2:
#    end_date = st.date_input('Select End date',end_date)

tab1, tab2, tab3 = st.tabs(["Dates", "Fibo","Cycles"])

#d = date(2023, 8, 6)

def days1(selected_date,pricet=0):
    #df=pd.read_csv('BANKNIFTYD.csv')
    global df11
    df=df11
    df=df.drop_duplicates()
    
    df['date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)
    df = df.sort_values(by='date', ascending=True)
    #df = df[~df['date'].dt.dayofweek.isin([5, 6])]
    #df['date']=pd.to_datetime(df['DATE '],dayfirst=True,yearfirst=False)
    
    datetouse= selected_date#datetime.date(2023,5,12)
    
    #df=df.iloc[::-1]
    #print(df)
    #df=df.reset_index()
    #df=df.iloc[:,1:]
    df=df.reset_index()
    df=df.iloc[:,1:]
    df['Close']=df['Close'].astype(float)
    df['Open']=df['Open'].astype(float)
    df['High']=df['High'].astype(float)
    df['Low']=df['Low'].astype(float)

    df['month']=df['date'].dt.month
    df['day']=df['date'].dt.day
    df['date']=df['date'].dt.date

    df['ln']=np.log(df['Close']/df['Close'].shift(1))
    df['ln']=df['ln'].apply(lambda x: format(x, '.9f'))
    
    df=df[df['date']<=selected_date]
    df1=df.iloc[-10:]
    
    #df1['ln']=df1['ln'].apply(lambda x: format(x, '.8f'))
    khr=df1[['date','Close','ln']]
    khr['Close']=khr['Close']
    #st.dataframe(khr)
    baseprice=df['Close'].iloc[-1]
    baseprice=st.number_input(label='Current Cycles Input Price',value=baseprice,min_value=0.0,max_value=100000.0)
    
    lnsum=list(df1['ln'].apply(float))
    #dra=round(sum(lnsum)/len(lnsum),9)
    if len(lnsum) > 0:
        dra = round(sum(lnsum) / len(lnsum), 9)
    else:
        dra = 0
    jj=lnsum
    jj.append(dra)
    stdev_p = round(np.std(jj, ddof=0),9)
    ssstd=round(dra+stdev_p,9)
    cycles=[]
    cycles=[['1st cycle','3rd cycle','5th cycle','7th cycle','9th cycle','11th cycle','13th cycle','15th cycle','17th cycle'],
            [dra,dra*sqrt(3),dra*sqrt(5),dra*sqrt(7),dra*sqrt(9),dra*sqrt(11),dra*sqrt(13),dra*sqrt(15),dra*sqrt(17)],
            [stdev_p,stdev_p*sqrt(3),stdev_p*sqrt(5),stdev_p*sqrt(7),stdev_p*sqrt(9),stdev_p*sqrt(11),stdev_p*sqrt(13),stdev_p*sqrt(15),stdev_p*sqrt(17)]
            ]
    
    cycles.append([sum(x) for x in zip(cycles[1], cycles[2])])
    
    cycles.append([(baseprice*x) for x in cycles[3]])
    cycles.append([(baseprice+x) for x in cycles[4]])
    cycles.append([(baseprice-x) for x in cycles[4]])
    
    
    cycle=pd.DataFrame(cycles[1:],columns=cycles[0])
    #st.dataframe(cycle)
    tradecycle=cycle.iloc[-2:]
    tradecycle.index=['IntradayTop','IntradayDown']
    #tradecycle['IntradayTop'].iloc[0] 
    #st.dataframe(df1)
    st.header('Cycles Levels')
    st.table(tradecycle)

    high=df['High'].astype(float).iloc[-1]
    low=df['Low'].astype(float).iloc[-1]
    buys=[]
    sells=[]
    for i,r in cycle.T.iterrows():
        if high>r[4]:
            print('buy')
            print(r[4])
            print(i)
            buys.append(i)
        if r[5]>low:
            print('sell')
            print(r[5])
            print(i)
            sells.append(i)
    st.write(f'Buys {buys}')

    st.write(f'Sells {sells}')



    st.dataframe(df.iloc[-1])


    return buys,sells






def days(df):
        #df=pd.read_csv('BANKNIFTYD.csv')
        
        #df['date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)
        print('dayssssssssssssssssssss')
        print(df)
        df['date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
        #df = df[~df['date'].dt.dayofweek.isin([5, 6])]
        #datetouse= datetime.date(2023,3,10)
        #selected_date=datetouse
        #df=df.iloc[::-1]
        df=df.reset_index()
        df=df.iloc[:,1:]
        lastclose=df['Close'].iloc[-1]
        lastclose=st.number_input(label='Current Low Drift Input Price',value=lastclose,min_value=0.0,max_value=100000.0)
        df['Close'].iloc[-1]=lastclose
        df['normalizeClose']=np.log(df['Close'])-np.log(df['Open'])
        df['normalizeClose']=df['normalizeClose'].apply(lambda x: format(x, '.12f'))
        df['normalizeClose']=df['normalizeClose'].astype(float)

        df['normalizeHigh']=np.log(df['High'])-np.log(df['Open'])
        df['normalizeHigh']=df['normalizeHigh'].apply(lambda x: format(x, '.12f'))
        df['normalizeHigh']=df['normalizeHigh'].astype(float)


        df['normalizeLow']=np.log(df['Low'])-np.log(df['Open'])
        df['normalizeLow']=df['normalizeLow'].apply(lambda x: format(x, '.12f'))
        df['normalizeLow']=df['normalizeLow'].astype(float)

        df['normalizeOpen']=np.log(df['Open'])-np.log(df['Close'].shift(1))
        df['normalizeOpen']=df['normalizeOpen'].apply(lambda x: format(x, '.12f'))
        df['normalizeOpen']=df['normalizeOpen'].astype(float)
        df=df.dropna()
        df['o+c']=df['normalizeOpen']+df['normalizeClose']
        df=df.iloc[-9:]
        #st.dataframe(df)
        o_pl_c=df['o+c'].mean()
        df['ooo_o+c']=(df['o+c']-o_pl_c)**2

        
        sqs=df['ooo_o+c'].mean()
        volality=math.sqrt(sqs)
        volality_100=math.sqrt(sqs)*100
        volality_365=volality_100*math.sqrt(365)

        hpricerange=(lastclose*volality_365/100*(math.sqrt(input_days)))/math.sqrt(365)


        df['H(h-c)+L(L-C)']=df['normalizeHigh']*(df['normalizeHigh']-df['normalizeClose'])+df['normalizeLow']*(df['normalizeLow']-df['normalizeClose'])
        hhcllc=df['H(h-c)+L(L-C)'].mean()
        hhcllc_avg=math.sqrt(hhcllc)
        hhcllc_avg_100=hhcllc_avg*100
        hhcllc_avg_100_365=hhcllc_avg_100*math.sqrt(365)
        lpricerange=(lastclose*hhcllc_avg_100_365/100*(math.sqrt(input_days)))/math.sqrt(365)
        #st.dataframe(df)
        fibs=[0.236,0.382,0.5,0.618,0.786,0.888,1,1.236,1.618]
        ldf=pd.DataFrame()
        ldf['ratios']=fibs
        ldf.index=ldf['ratios']
        ldf['Drift']=ldf['ratios']*lpricerange
        ldf['Buy']=ldf['Drift']+lastclose
        ldf['Sell']=lastclose-ldf['Drift']

        hdf=pd.DataFrame()
        hdf['ratios']=fibs
        hdf.index=hdf['ratios']
        hdf['Drift']=hdf['ratios']*hpricerange

        hdf['Buy']=hdf['Drift']+lastclose
        hdf['Sell']=lastclose-hdf['Drift']

        #st.dataframe(df1)
        col1,col2=st.columns(2)
        lowpricerange=round(lpricerange)
        with col1:
            st.header('Low Drift Method')
        with col2:
            st.header(f'Price Range ( {lowpricerange} )')
        st.dataframe(ldf)
    
with tab1:

    
    d1f=selected_date
    d= selected_date - relativedelta(months=1)
    # Find the start date of the month
    start_date = d.replace(day=1)

    # Calculate the number of days in the month
    days_in_month = (start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(days=1)).day

    # Find the end date of the month
    end_date = start_date.replace(day=days_in_month)

    print("Start date:", start_date)
    print("End date:", end_date)
    #st.write(start_date)
    
    #st.write(end_date)
    #st.write(days_in_month)
    #t = investpy.get_index_historical_data(index='Nifty Bank',country="India", from_date=str(todate), to_date=str(d))
    



        
    if option1=='NSE':
               
        import requests

        cookies = {

        }

        headers = {
            'authority': 'www.nseindia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }
        
        # initialize a session
        session = requests.Session()
        
        # send a get request to the server
        response = session.get('https://www.nseindia.com/',cookies=cookies,
        headers=headers,)
        # print the response dictionary
        maincookie=(session.cookies.get_dict())

        import requests

        cookies = {
            
        }

        headers = {
            'authority': 'www.nseindia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }
        start=start_date.strftime('%d-%m-%Y')
        end=end_date.strftime('%d-%m-%Y')
        response = requests.get(f'https://www.nseindia.com/api/historical/cm/equity?symbol={option}&series=[%22EQ%22]&from={start}&to={end}',
            cookies=maincookie,
            headers=headers,
        )


        d=(response.json())
        df=(pd.DataFrame(d['data']))
                
        df['Date']=df['mTIMESTAMP']
        df['Date']=pd.to_datetime(df['Date'])
        df['High']=df['CH_TRADE_HIGH_PRICE'].astype(float)
        df['Low']=df['CH_TRADE_LOW_PRICE'].astype(float)
        df['Close']=df['CH_CLOSING_PRICE'].astype(float)
        df['Open']=df['CH_OPENING_PRICE'].astype(float)
        df['Symbol']=df['CH_SYMBOL']
        df=df[['Date','Open','High','Low','Close','Symbol']]
        df=df.iloc[::-1]

        #st.dataframe(df)


    elif option1=='Index':
        dr=pd.DataFrame()
        
        import requests

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://www.niftyindices.com',
            'Referer': 'https://www.niftyindices.com/reports/historical-data',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data_dict = {
            'name': option,
            'startDate': start_date.strftime('%d-%b-%Y'),
            'endDate': end_date.strftime('%d-%b-%Y')
        }

        data = json.dumps(data_dict)
        response = requests.post(
            'https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString',
            headers=headers,
            data=data,
        )
        f=response.json()

        df=pd.DataFrame(eval(f['d'])[::-1])
        #st.dataframe(df)
        #df=dr[dr['Name']==option]
        df['Date']=pd.to_datetime(df['HistoricalDate'],dayfirst=True,yearfirst=False)
        #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
        df['Close']=df['CLOSE'].astype(float)
        df['Open']=df['OPEN'].astype(float)
        df['High']=df['HIGH'].astype(float)
        df['Low']=df['LOW'].astype(float)
        df['Name']=df['INDEX_NAME']
        df=df[['Date','Open','High','Low','Close','Name']]
    elif option1=='MCX':
                
        import requests


        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            # 'Cookie': 'ASP.NET_SessionId=r1ozyozkyooxunf0tibiw222; device-referrer=https://www.google.com/; _gid=GA1.2.311038694.1694363277; device-source=https://www.mcxindia.com/#; _ga_8BQ43G0902=GS1.1.1694363277.2.1.1694365410.0.0.0; _ga=GA1.2.485484035.1694175674; _gat_gtag_UA_121835541_1=1',
            'Origin': 'https://www.mcxindia.com',
            'Referer': 'https://www.mcxindia.com/market-data/bhavcopy',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {'Symbol':option,'Expiry':expiry,'FromDate':start_date.strftime('%Y%m%d'),'ToDate':end_date.strftime('%Y%m%d'),'InstrumentName':'ALL'}

        response = requests.post(
            'https://www.mcxindia.com/backpage.aspx/GetCommoditywiseBhavCopy',
            cookies={},
            headers=headers,
            data=json.dumps(data),
        )

        df=pd.DataFrame(response.json()['d']['Data'])
        df['Date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)#.dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        df['Symbol'] = df['Symbol'].str.strip()
        df['Name']=df['Symbol']+df['ExpiryDate']
        df['Open']=df['Open'].astype(float)
        df['High']=df['High'].apply(float)
        df['Low']=df['Low'].apply(float)
        df['Close']=df['Close'].apply(float)
        df=df[['Date','Open','High','Low','Close','Name','Symbol']]
        df=df.iloc[::-1]
    elif option1=='CDS':
        headers = {
            'authority': 'www.nseindia.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'defaultLang=en; ak_bmsc=E5C0511535D7E8AFFB3120903EFBC9E7~000000000000000000000000000000~YAAQXydzaNh9a0mKAQAARhuKghU41sMB1ys0vToJEVMDI5c/ASIxBXXPLVp/1juGYJCBL3AzpFcpxJpOuUJwySLHYu7CS5Zea5g5v7O3uj3DYyq42oat2sM07t8Vi0v3bZYbr9RNLs0zAOhMk+L5xKxVNAznxV95DT3wR8/H00AhUWpi1Agm3yVOidyqe1r588pG/NCuNxMNnoL7AUhxiWhyjA36ZXl4IS6BmkPnKTT1wtVTjyAsnmIfgzImSsHZt6+lfm6ViKNImTfvqwOElYdrIpP/Z1gcKVQEMFApDGQpJmUB11QDlY/Ng7XfOTSAFodORsoa4Wl3Sh/isqTcDzH4QB2qzr8pWoUIuiT0aEwPm0wYFPkaH4aSMw9WwcYRWjla8nWHjowVFa9cX9kfXc/0V1qSvLjn1sBxx6WtwX11Ku2eIvEaTOeKoP9++q8NmPFw5SE8y3rmsi6kycT2IG63aIjrtCpBKzELef7R/67EXewbzopTOSxL17FLCkCeLQVHSw==; _gid=GA1.2.412291923.1694407207; nsit=DcGVOBs5rFJNtXEK8lC3Xorm; _ga=GA1.1.1632056446.1694146307; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY5NDQxMzA3MSwiZXhwIjoxNjk0NDIwMjcxfQ.JOM8PC7cwUVZXqdV5AoWhoY6GYJeahOjP_MXXQZ_Z3s; AKA_A2=A; _ga_PJSKY6CFJH=GS1.1.1694412311.16.1.1694413071.59.0.0; bm_sv=727C08A8A2C36DC06D41C86326369542~YAAQZSdzaKHgM0uKAQAAkezjghVD7q8MmpuNfVKCm1OChebtjPo3+xJ4QhMJzLXU5tbI138YGsGnE58h+/C/YVd4/iM4d1xMdbtfj7xMQPlmXI7PErPNQRgugwK79JYkHdW0cZjiFtGvn9YxTTr2AIv3XxAReCS8xJJjsZoaot7BEo191/HldmreN4W59We/U9nM6+210CC4XxKuq/th6fLdAEAsmju8zZX+bGsY00g7N4LvZEd7hUDy/macfuDB+o/0FA==~1',
            'referer': 'https://www.nseindia.com/report-detail/cd_eq_security',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }

        params = {
            'from': start_date.strftime('%d-%m-%Y'),
            'to': end_date.strftime('%d-%m-%Y'),
            'instrumentType': 'FUTCUR',
            'symbol': option,
            'year': str(selected_date.year),
            'expiryDate': expiry,
        }
        print(params)
        response = requests.get('https://www.nseindia.com/api/historical/cdCPV', params=params, cookies=maincookie, headers=headers)
        d=response.json()
        df=(pd.DataFrame(d['data']))
                
        df['Date']=df['CD_TIMESTAMP']
        df['Date']=pd.to_datetime(df['Date'])
        df['High']=df['CD_TRADE_HIGH_PRICE'].astype(float)*1000
        df['Low']=df['CD_TRADE_LOW_PRICE'].astype(float)*1000
        df['Close']=df['CD_CLOSING_PRICE'].astype(float)*1000
        df['Open']=df['CD_OPENING_PRICE'].astype(float)*1000
        df['Symbol']=df['CD_SYMBOL']
        df=df[['Date','Open','High','Low','Close','Symbol']]
        df=df.iloc[::-1]





    df['Date']=pd.to_datetime(df['Date'])#,dayfirst=False,yearfirst=False)
    #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
    df['Open']=df['Open'].astype(float)
    df['High']=df['High'].apply(float)
    df['Low']=df['Low'].apply(float)
    df['Close']=df['Close'].apply(float)

    
    #t=niftybank
    t=df
    t=t.drop_duplicates()
    t=t.set_index(['Date'])
    t = t.sort_values(by='Date')
    #st.dataframe(t)
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
    print('calenderdate')
    print(calenderdate)
    maxmod=((math.sqrt(maxh))*180-225)%360
    minmod=((math.sqrt(minh))*180-225)%360
    calenderdatemod=((math.sqrt(calenderdate))*180-225)%360
    tradedaymod=((math.sqrt(tradeday))*180-225)%360
    print('calenderdatemod')
    print(calenderdatemod)
    print('tradedaymod')
    print(tradedaymod)

    maxdeg=max([maxmod,minmod,calenderdatemod,tradedaymod])#.max()
    mindeg=min([maxmod,minmod,calenderdatemod,tradedaymod])#.min()

    max1=round((2+((2*maxdeg)/360)+1.25)**2,6)
    max2=(4+((2*maxdeg)/360)+1.25)**2
    max3=(6+((2*maxdeg)/360)+1.25)**2
    print('max1,max2,max3')
    print(max1,max2,max3)




    min1=(2+(2*mindeg)/360+1.25)**2
    min2=(4+(2*mindeg)/360+1.25)**2
    min3=(6+(2*mindeg)/360+1.25)**2
    print('min1,min2,min3')
    print(min1,min2,min3)

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

    h1=[maxdate1.date(),maxdate2.date(),maxdate3.date(),maxdate_1.date(),maxdate_2.date(),maxdate_3.date(),
     mindate1.date(),mindate2.date(),mindate3.date(),mindate_1.date(),mindate_2.date(),mindate_3.date()]
    print('1st method')
    print(h1)
    print('1st end method')
    ##############technique 1 ##h1###################


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

    min1=round((2*1+(2*mindeg)/360+1.25)**2,6)
    min2=(2*2+(2*mindeg)/360+1.25)**2
    min3=(2*3+(2*mindeg)/360+1.25)**2
    print('technique2')

    print('max1,max2,max3')
    print(max1,max2,max3)
    print('min1,min2,min3')
    print(min1,min2,min3)


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
    print('technique2')
    print('min1,min2,min3,min4,min5')
    print(min1,min2,min3,min4,min5)

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


    h3=[maxdate1.date(),maxdate2.date(),maxdate3.date(),maxdate4.date(),maxdate5.date(),
     mindate1.date(),mindate2.date(),mindate3.date(),mindate4.date(),mindate5.date()]

    ##############technique 3 #####################

    print(h1)
    print(h2)
    print(h3)
    h5=[]
    h5.extend(h1)
    h5.extend(h2)
    h5.extend(h3)
    h4 = []

    h11=[]
    h21=[]
    h31=[]
    for i in h1:
        
        if i.month==d1f.month:
            print('')
            print(True)
            print(i)
            h11.append(i)
    #st.write(h1)
    #st.write(h2)
    #st.write(h3)
    #st.write(h4)
    #print(h4)

    from collections import Counter
    date_counter = Counter(h11)

    # Sort dates by initial date
    sorted_dates = sorted(date_counter.items(), key=lambda x: x[0])
    #st.write(sorted_dates)
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
        #st.write([f"{date.strftime('%d-%B-%Y')}" ,count,f"{date.strftime('%A')}"])
        if int(count)==1:
           weak.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        elif int(count) > 1:
           strong.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        
    #print(strong)
    #print(len(strong))
    strong1=pd.DataFrame(strong,columns=['Major Trend Change Date','Major Trend','Major Weekday'])
    #print(weak)
    #print(len(weak))
    #st.dataframe(strong1)

    weak1=pd.DataFrame(weak,columns=['Minor Trend Change Date','Minor Trend','Minor Weekday'])
    #st.dataframe(weak1)
    #st.write(len(weak1))
    #st.write(len(strong1))
    st.write('1st Method')
    if len(weak1) > len(strong1):
        strong2=weak1
        strong2['Major Trend Change Date']=strong1['Major Trend Change Date']
        strong2['Major Trend']=strong1['Major Trend']
        strong2['Major Weekday']=strong1['Major Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        st.dataframe(strong2)
    else:
        strong2=strong1
        strong2['Minor Trend Change Date']=weak1['Minor Trend Change Date']
        strong2['Minor Trend']=weak1['Minor Trend']
        strong2['Minor Weekday']=weak1['Minor Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        
        st.dataframe(strong2)
        #st.write(h5)     
    for i in h2:
        
        if i.month==d1f.month:
            print('')
            print(True)
            print(i)
            h21.append(i)
    #st.write(h1)
    #st.write(h2)
    #st.write(h3)
    #st.write(h4)
    #print(h4)

    from collections import Counter
    date_counter = Counter(h21)

    # Sort dates by initial date
    sorted_dates = sorted(date_counter.items(), key=lambda x: x[0])
    #st.write(sorted_dates)
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
        #st.write([f"{date.strftime('%d-%B-%Y')}" ,count,f"{date.strftime('%A')}"])
        if int(count)==1:
           weak.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        elif int(count) > 1:
           strong.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        
    #print(strong)
    #print(len(strong))
    strong1=pd.DataFrame(strong,columns=['Major Trend Change Date','Major Trend','Major Weekday'])
    #print(weak)
    #print(len(weak))
    #st.dataframe(strong1)

    weak1=pd.DataFrame(weak,columns=['Minor Trend Change Date','Minor Trend','Minor Weekday'])
    #st.dataframe(weak1)
    #st.write(len(weak1))
    #st.write(len(strong1))
    
    st.write('2nd Method')
    if len(weak1) > len(strong1):
        strong2=weak1
        strong2['Major Trend Change Date']=strong1['Major Trend Change Date']
        strong2['Major Trend']=strong1['Major Trend']
        strong2['Major Weekday']=strong1['Major Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        st.dataframe(strong2)
    else:
        strong2=strong1
        strong2['Minor Trend Change Date']=weak1['Minor Trend Change Date']
        strong2['Minor Trend']=weak1['Minor Trend']
        strong2['Minor Weekday']=weak1['Minor Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        
        st.dataframe(strong2)
        #st.write(h5)     
    for i in h3:
        
        if i.month==d1f.month:
            print('')
            print(True)
            print(i)
            h31.append(i)
    #st.write(h1)
    #st.write(h2)
    #st.write(h3)
    #st.write(h4)
    #print(h4)

    from collections import Counter
    date_counter = Counter(h31)

    # Sort dates by initial date
    sorted_dates = sorted(date_counter.items(), key=lambda x: x[0])
    #st.write(sorted_dates)
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
        #st.write([f"{date.strftime('%d-%B-%Y')}" ,count,f"{date.strftime('%A')}"])
        if int(count)==1:
           weak.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        elif int(count) > 1:
           strong.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        
    #print(strong)
    #print(len(strong))
    strong1=pd.DataFrame(strong,columns=['Major Trend Change Date','Major Trend','Major Weekday'])
    #print(weak)
    #print(len(weak))
    #st.dataframe(strong1)

    weak1=pd.DataFrame(weak,columns=['Minor Trend Change Date','Minor Trend','Minor Weekday'])
    #st.dataframe(weak1)
    #st.write(len(weak1))
    #st.write(len(strong1))
    
    st.write('3rd Method')
    if len(weak1) > len(strong1):
        strong2=weak1
        strong2['Major Trend Change Date']=strong1['Major Trend Change Date']
        strong2['Major Trend']=strong1['Major Trend']
        strong2['Major Weekday']=strong1['Major Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        st.dataframe(strong2)
    else:
        strong2=strong1
        strong2['Minor Trend Change Date']=weak1['Minor Trend Change Date']
        strong2['Minor Trend']=weak1['Minor Trend']
        strong2['Minor Weekday']=weak1['Minor Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        
        st.dataframe(strong2)
        #st.write(h5)     
    for i in h5:
        
        if i.month==d1f.month:
            print('')
            print(True)
            print(i)
            h4.append(i)
    #st.write(h1)
    #st.write(h2)
    #st.write(h3)
    #st.write(h4)
    #print(h4)

    from collections import Counter
    date_counter = Counter(h4)

    # Sort dates by initial date
    sorted_dates = sorted(date_counter.items(), key=lambda x: x[0])
    #st.write(sorted_dates)
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
        #st.write([f"{date.strftime('%d-%B-%Y')}" ,count,f"{date.strftime('%A')}"])
        if int(count)==1:
           weak.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        elif int(count) > 1:
           strong.append([f"{date.strftime('%d-%B-%Y')}" ,f"{count}",f"{date.strftime('%A')}"]) 
        
    #print(strong)
    #print(len(strong))
    strong1=pd.DataFrame(strong,columns=['Major Trend Change Date','Major Trend','Major Weekday'])
    #print(weak)
    #print(len(weak))
    #st.dataframe(strong1)

    weak1=pd.DataFrame(weak,columns=['Minor Trend Change Date','Minor Trend','Minor Weekday'])
    #st.dataframe(weak1)
    #st.write(len(weak1))
    #st.write(len(strong1))
    if len(weak1) > len(strong1):
        strong2=weak1
        strong2['Major Trend Change Date']=strong1['Major Trend Change Date']
        strong2['Major Trend']=strong1['Major Trend']
        strong2['Major Weekday']=strong1['Major Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        st.dataframe(strong2)
    else:
        strong2=strong1
        strong2['Minor Trend Change Date']=weak1['Minor Trend Change Date']
        strong2['Minor Trend']=weak1['Minor Trend']
        strong2['Minor Weekday']=weak1['Minor Weekday']
        #print(strong2)
        strong2=strong2[['Major Trend Change Date','Major Trend','Major Weekday','Minor Trend Change Date','Minor Trend','Minor Weekday']]
        
        st.dataframe(strong2)
        #st.write(h5)     


with tab2:

    syms=['BANKNIFTY','NIFTY']
    #o=st.selectbox('Select Symbol :',syms)
    #st.write('Display Symbol is:', o)
    
        
    # create a date picker to select a date
    
    # create a list of specific valid dates
        
    #nf,bnf,mdf=maindaydata()


        
    print('tabs 2 222222222222222222222')
    if option1=='NSE':
        
                
        import requests

        cookies = {

        }

        headers = {
            'authority': 'www.nseindia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }
        
        # initialize a session
        session = requests.Session()
        
        # send a get request to the server
        response = session.get('https://www.nseindia.com/',cookies=cookies,
        headers=headers,)
        # print the response dictionary
        maincookie=(session.cookies.get_dict())

        import requests

        cookies = {
            
        }

        headers = {
            'authority': 'www.nseindia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }
        start=start_date1.strftime('%d-%m-%Y')
        end=end_date1.strftime('%d-%m-%Y')
        response = requests.get(f'https://www.nseindia.com/api/historical/cm/equity?symbol={option}&series=[%22EQ%22]&from={start}&to={end}',
            cookies=maincookie,
            headers=headers,
        )


        d=(response.json())
        df=(pd.DataFrame(d['data']))
                
        df['Date']=df['mTIMESTAMP']
        df['Date']=pd.to_datetime(df['Date'])
        df['High']=df['CH_TRADE_HIGH_PRICE'].astype(float)
        df['Low']=df['CH_TRADE_LOW_PRICE'].astype(float)
        df['Close']=df['CH_CLOSING_PRICE'].astype(float)
        df['Open']=df['CH_OPENING_PRICE'].astype(float)
        df['Symbol']=df['CH_SYMBOL']
        df=df[['Date','Open','High','Low','Close','Symbol']]
        df=df.iloc[::-1]
        df1=df
        #st.dataframe(df)

        df=df.drop_duplicates()

        df['Date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)
        df = df.sort_values(by='Date', ascending=True)
        #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
        #df=df.iloc[::-1]
        df11=df
        df['DailyRange']=df['High']-df['Low']
        df['avg']=(df['Open']+df['Close'])/2
        df=df.iloc[-10:]
        #st.dataframe(df)
        #st.write(f'dailyavg mean is {df['DailyRange'].mean()}')

        #st.write(f'avg mean is {df['avg'].mean()}')
        vola=(df['DailyRange'].mean()/df['avg'].mean())
        vola100=vola*100
        vola365=vola100*math.sqrt(365)
        lastclose=df['Close'].iloc[-1]
        lastclose=st.number_input(label='Current Ohlcv Drift Input Price',value=lastclose,min_value=0.0,max_value=100000.0)
        multiday=(lastclose*vola365/100*(math.sqrt(input_days)))/math.sqrt(365)
        multiday=st.number_input(label='Price Range',value=multiday,min_value=0.0,max_value=100000.0)
    
        fibs=[0.236,0.382,0.5,0.618,0.786,0.888,1,1.236,1.618]
        ldf=pd.DataFrame()
        ldf['ratios']=fibs
        ldf.index=ldf['ratios']
        ldf['w']=ldf['ratios']*multiday

        ldf['Buy']=ldf['w']+lastclose
        ldf['Sell']=lastclose-ldf['w']
        col1,col2=st.columns(2)
        multiday=round(multiday,2)
        with col1:
            st.header('OHLC Method')
        with col2:
            st.header(f'Price Range ( {multiday} )')
        
        st.dataframe(ldf)
    elif option1=='Index':
        #dr=maindaydata()
        
        import requests

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://www.niftyindices.com',
            'Referer': 'https://www.niftyindices.com/reports/historical-data',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data_dict = {
            'name': option,
            'startDate': start_date1.strftime('%d-%b-%Y'),
            'endDate': end_date1.strftime('%d-%b-%Y')
        }

        data = json.dumps(data_dict)
        response = requests.post(
            'https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString',
            headers=headers,
            data=data,
        )
        f=response.json()

        df=pd.DataFrame(eval(f['d'])[::-1])
        #df=dr[dr['Name']==option]
        #st.dataframe(df)
        df['Date']=pd.to_datetime(df['HistoricalDate'],dayfirst=True,yearfirst=False)
        #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
        df = df.sort_values(by='Date', ascending=True)
        df['Close']=df['CLOSE'].astype(float)
        df['Open']=df['OPEN'].astype(float)
        df['High']=df['HIGH'].astype(float)
        df['Low']=df['LOW'].astype(float)
        df['Name']=df['INDEX_NAME']
        df=df[['Date','Open','High','Low','Close','Name']]
        days(df)
    elif option1=='MCX':
        #dr=maindaydata2(start_date,end_date)
        import requests


        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            # 'Cookie': 'ASP.NET_SessionId=r1ozyozkyooxunf0tibiw222; device-referrer=https://www.google.com/; _gid=GA1.2.311038694.1694363277; device-source=https://www.mcxindia.com/#; _ga_8BQ43G0902=GS1.1.1694363277.2.1.1694365410.0.0.0; _ga=GA1.2.485484035.1694175674; _gat_gtag_UA_121835541_1=1',
            'Origin': 'https://www.mcxindia.com',
            'Referer': 'https://www.mcxindia.com/market-data/bhavcopy',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {'Symbol':option,'Expiry':expiry,'FromDate':start_date1.strftime('%Y%m%d'),'ToDate':end_date1.strftime('%Y%m%d'),'InstrumentName':'ALL'}

        response = requests.post(
            'https://www.mcxindia.com/backpage.aspx/GetCommoditywiseBhavCopy',
            cookies={},
            headers=headers,
            data=json.dumps(data),
        )

        df=pd.DataFrame(response.json()['d']['Data'])
        df['Date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)#.dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        df['Symbol'] = df['Symbol'].str.strip()
        df['Name']=df['Symbol']+df['ExpiryDate']
        df['Open']=df['Open'].astype(float)
        df['High']=df['High'].apply(float)
        df['Low']=df['Low'].apply(float)
        df['Close']=df['Close'].apply(float)
        df=df[['Date','Open','High','Low','Close','Name','Symbol']]
        df=df.iloc[::-1]
        df=df.drop_duplicates()

        
        df['Date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)
        #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
        df = df.sort_values(by='Date', ascending=True)
        df11=df
        df['DailyRange']=df['High']-df['Low']
        df['avg']=(df['Open']+df['Close'])/2
        df=df.iloc[-10:]
        #st.write(f'dailyavg mean is {df['DailyRange'].mean()}')
        #st.dataframe(df)
        #st.write(f'avg mean is {df['avg'].mean()}')
        vola=(df['DailyRange'].mean()/df['avg'].mean())
        vola100=vola*100
        vola365=vola100*math.sqrt(365)
        lastclose=df['Close'].iloc[-1]
        
        lastclose=st.number_input(label='Current Ohlcv Drift Input Price',value=lastclose,min_value=0.0,max_value=100000.0)
        multiday=(lastclose*vola365/100*(math.sqrt(input_days)))/math.sqrt(365)
        multiday=st.number_input(label='Price Range',value=multiday,min_value=0.0,max_value=100000.0)
    
        fibs=[0.236,0.382,0.5,0.618,0.786,0.888,1,1.236,1.618]
        ldf=pd.DataFrame()
        ldf['ratios']=fibs
        ldf.index=ldf['ratios']
        ldf['w']=ldf['ratios']*multiday

        ldf['Buy']=ldf['w']+lastclose
        ldf['Sell']=lastclose-ldf['w']
        col1,col2=st.columns(2)
        multiday=round(multiday,2)
        with col1:
            st.header('OHLC Method')
        with col2:
            st.header(f'Price Range ( {multiday} )')
        
        st.dataframe(ldf)

    

    #st.dataframe(df)
    #
    elif option1=='CDS':
        headers = {
            'authority': 'www.nseindia.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'defaultLang=en; ak_bmsc=E5C0511535D7E8AFFB3120903EFBC9E7~000000000000000000000000000000~YAAQXydzaNh9a0mKAQAARhuKghU41sMB1ys0vToJEVMDI5c/ASIxBXXPLVp/1juGYJCBL3AzpFcpxJpOuUJwySLHYu7CS5Zea5g5v7O3uj3DYyq42oat2sM07t8Vi0v3bZYbr9RNLs0zAOhMk+L5xKxVNAznxV95DT3wR8/H00AhUWpi1Agm3yVOidyqe1r588pG/NCuNxMNnoL7AUhxiWhyjA36ZXl4IS6BmkPnKTT1wtVTjyAsnmIfgzImSsHZt6+lfm6ViKNImTfvqwOElYdrIpP/Z1gcKVQEMFApDGQpJmUB11QDlY/Ng7XfOTSAFodORsoa4Wl3Sh/isqTcDzH4QB2qzr8pWoUIuiT0aEwPm0wYFPkaH4aSMw9WwcYRWjla8nWHjowVFa9cX9kfXc/0V1qSvLjn1sBxx6WtwX11Ku2eIvEaTOeKoP9++q8NmPFw5SE8y3rmsi6kycT2IG63aIjrtCpBKzELef7R/67EXewbzopTOSxL17FLCkCeLQVHSw==; _gid=GA1.2.412291923.1694407207; nsit=DcGVOBs5rFJNtXEK8lC3Xorm; _ga=GA1.1.1632056446.1694146307; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY5NDQxMzA3MSwiZXhwIjoxNjk0NDIwMjcxfQ.JOM8PC7cwUVZXqdV5AoWhoY6GYJeahOjP_MXXQZ_Z3s; AKA_A2=A; _ga_PJSKY6CFJH=GS1.1.1694412311.16.1.1694413071.59.0.0; bm_sv=727C08A8A2C36DC06D41C86326369542~YAAQZSdzaKHgM0uKAQAAkezjghVD7q8MmpuNfVKCm1OChebtjPo3+xJ4QhMJzLXU5tbI138YGsGnE58h+/C/YVd4/iM4d1xMdbtfj7xMQPlmXI7PErPNQRgugwK79JYkHdW0cZjiFtGvn9YxTTr2AIv3XxAReCS8xJJjsZoaot7BEo191/HldmreN4W59We/U9nM6+210CC4XxKuq/th6fLdAEAsmju8zZX+bGsY00g7N4LvZEd7hUDy/macfuDB+o/0FA==~1',
            'referer': 'https://www.nseindia.com/report-detail/cd_eq_security',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }

        params = {
            'from': start_date.strftime('%d-%m-%Y'),
            'to': end_date.strftime('%d-%m-%Y'),
            'instrumentType': 'FUTCUR',
            'symbol': option,
            'year': str(selected_date.year),
            'expiryDate': expiry,
        }

        response = requests.get('https://www.nseindia.com/api/historical/cdCPV', params=params, cookies=maincookie, headers=headers)
        d=response.json()
        df=(pd.DataFrame(d['data']))
                
        df['Date']=df['CD_TIMESTAMP']
        df['Date']=pd.to_datetime(df['Date'])
        df['High']=df['CD_TRADE_HIGH_PRICE'].astype(float)*1000
        df['Low']=df['CD_TRADE_LOW_PRICE'].astype(float)*1000
        df['Close']=df['CD_CLOSING_PRICE'].astype(float)*1000
        df['Open']=df['CD_OPENING_PRICE'].astype(float)*1000
        df['Symbol']=df['CD_SYMBOL']
        df=df[['Date','Open','High','Low','Close','Symbol']]
        df=df.iloc[::-1]

        df=df.drop_duplicates()

        
        df['Date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)
        #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
        df = df.sort_values(by='Date', ascending=True)
        df11=df
        df['DailyRange']=df['High']-df['Low']
        df['avg']=(df['Open']+df['Close'])/2
        df=df.iloc[-10:]
        #st.write(f'dailyavg mean is {df['DailyRange'].mean()}')
        #st.dataframe(df)
        #st.write(f'avg mean is {df['avg'].mean()}')
        vola=(df['DailyRange'].mean()/df['avg'].mean())
        vola100=vola*100
        vola365=vola100*math.sqrt(365)
        lastclose=df['Close'].iloc[-1]
        
        lastclose=st.number_input(label='Current Ohlcv Drift Input Price',value=lastclose,min_value=0.0,max_value=100000.0)
        multiday=(lastclose*vola365/100*(math.sqrt(input_days)))/math.sqrt(365)
        multiday=st.number_input(label='Price Range',value=multiday,min_value=0.0,max_value=100000.0)
    
        fibs=[0.236,0.382,0.5,0.618,0.786,0.888,1,1.236,1.618]
        ldf=pd.DataFrame()
        ldf['ratios']=fibs
        ldf.index=ldf['ratios']
        ldf['w']=ldf['ratios']*multiday

        ldf['Buy']=ldf['w']+lastclose
        ldf['Sell']=lastclose-ldf['w']
        col1,col2=st.columns(2)
        multiday=round(multiday,2)
        with col1:
            st.header('OHLC Method')
        with col2:
            st.header(f'Price Range ( {multiday} )')
        
        st.dataframe(ldf)


     



with tab3:
    
    
    #buys,sells=days1(end_date)
    if option1=='NSE':
        
                
        import requests

        cookies = {

        }

        headers = {
            'authority': 'www.nseindia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }
        
        # initialize a session
        session = requests.Session()
        
        # send a get request to the server
        response = session.get('https://www.nseindia.com/',cookies=cookies,
        headers=headers,)
        # print the response dictionary
        maincookie=(session.cookies.get_dict())

        import requests

        cookies = {
            
        }

        headers = {
            'authority': 'www.nseindia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
        }
        start=start_date.strftime('%d-%m-%Y')
        end=end_date.strftime('%d-%m-%Y')
        response = requests.get(f'https://www.nseindia.com/api/historical/cm/equity?symbol={option}&series=[%22EQ%22]&from={start}&to={end}',
            cookies=maincookie,
            headers=headers,
        )


        d=(response.json())
        df=(pd.DataFrame(d['data']))
                
        df['Date']=df['mTIMESTAMP']
        df['Date']=pd.to_datetime(df['Date'])
        df['High']=df['CH_TRADE_HIGH_PRICE'].astype(float)
        df['Low']=df['CH_TRADE_LOW_PRICE'].astype(float)
        df['Close']=df['CH_CLOSING_PRICE'].astype(float)
        df['Open']=df['CH_OPENING_PRICE'].astype(float)
        df['Symbol']=df['CH_SYMBOL']
        df=df[['Date','Open','High','Low','Close','Symbol']]
        df=df.iloc[::-1]

        #st.dataframe(df)

        
    elif option1=='Index':
        dr=pd.DataFrame()
        
        import requests

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://www.niftyindices.com',
            'Referer': 'https://www.niftyindices.com/reports/historical-data',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data_dict = {
            'name': option,
            'startDate': start_date2.strftime('%d-%b-%Y'),
            'endDate': end_date2.strftime('%d-%b-%Y')
        }

        data = json.dumps(data_dict)
        response = requests.post(
            'https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString',
            headers=headers,
            data=data,
        )
        f=response.json()

        df=pd.DataFrame(eval(f['d'])[::-1])
        #df=dr[dr['Name']==option]
        #st.dataframe(df)
        df['Date']=pd.to_datetime(df['HistoricalDate'],dayfirst=True,yearfirst=False)
        df = df.sort_values(by='Date', ascending=True)
        #df = df[~df['Date'].dt.dayofweek.isin([5, 6])]
        df['Close']=df['CLOSE'].astype(float)
        df['Open']=df['OPEN'].astype(float)
        df['High']=df['HIGH'].astype(float)
        df['Low']=df['LOW'].astype(float)
        df['Name']=df['INDEX_NAME']
        df=df[['Date','Open','High','Low','Close','Name']]
        #days(df)
        
    elif option1=='MCX':
        #dr=maindaydata2(start_date2,end_date2)
        import requests


        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            # 'Cookie': 'ASP.NET_SessionId=r1ozyozkyooxunf0tibiw222; device-referrer=https://www.google.com/; _gid=GA1.2.311038694.1694363277; device-source=https://www.mcxindia.com/#; _ga_8BQ43G0902=GS1.1.1694363277.2.1.1694365410.0.0.0; _ga=GA1.2.485484035.1694175674; _gat_gtag_UA_121835541_1=1',
            'Origin': 'https://www.mcxindia.com',
            'Referer': 'https://www.mcxindia.com/market-data/bhavcopy',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {'Symbol':option,'Expiry':expiry,'FromDate':start_date2.strftime('%Y%m%d'),'ToDate':end_date2.strftime('%Y%m%d'),'InstrumentName':'ALL'}

        response = requests.post(
            'https://www.mcxindia.com/backpage.aspx/GetCommoditywiseBhavCopy',
            cookies={},
            headers=headers,
            data=json.dumps(data),
        )

        df=pd.DataFrame(response.json()['d']['Data'])
        df['Date']=pd.to_datetime(df['Date'],dayfirst=False,yearfirst=False)#.dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        df['Symbol'] = df['Symbol'].str.strip()
        df['Name']=df['Symbol']+df['ExpiryDate']
        df['Open']=df['Open'].astype(float)
        df['High']=df['High'].apply(float)
        df['Low']=df['Low'].apply(float)
        df['Close']=df['Close'].apply(float)
        df=df[['Date','Open','High','Low','Close','Name','Symbol']]
        df=df.iloc[::-1]
    df = df.sort_values(by='Date', ascending=True)
    df11=df
    days1(selected_date)



