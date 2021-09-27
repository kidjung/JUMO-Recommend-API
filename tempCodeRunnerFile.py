import pandas as pd
import datetime
import DBconnector as db

def EMA(data, period=20, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()

def MACD(data, period_long=26, period_short=12, period_signal=9, column='Close'):
    ShortEMA = EMA(data, period_short, column=column)
    LongEMA = EMA(data, period_long, column=column)
    data['MACD'] = ShortEMA - LongEMA
    # print(data['MACD'])
    data['Signal_Line'] = EMA(data, period_signal, column='MACD')
    # print(data['Signal_Line'])
    return data

result = db.throwQuery("""SELECT code,name,time,Close FROM price WHERE name="호전실업";""")
print(result[0])
df = pd.DataFrame(result)
# df['EMA'] = EMA(df)
# df['MACD'] = MACD(df)['MACD']
# df['Signal_line'] = MACD(df)['Signal_Line']
# df[[pd.DataFrame(EMA(df))]]
print(df)


# def makeDataFrame():
