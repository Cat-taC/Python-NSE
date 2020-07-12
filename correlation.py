import nsepy
import datetime
import pandas as pd

excel = pd.read_csv("G:/Stock/Symbols.csv")

symbol = excel[["Symbol"]]

for each_symbol in symbol['Symbol']:    
    stock = nsepy.get_history(each_symbol,
                start=datetime.date(2019,1,1), 
                end=datetime.date(2019,12,31))
    for symbol2 in symbol['Symbol']:
        if(each_symbol > symbol2 ):
            stock2 = nsepy.get_history(symbol2,
                            start=datetime.date(2019,1,1), 
                            end=datetime.date(2019,12,31))
            corel = stock['Close'].corr(stock2['Close'])
            if(corel > 0.5 or corel < -0.5):
                print(each_symbol + " " + symbol2 + " " + str(corel))

    
print('End of Program')