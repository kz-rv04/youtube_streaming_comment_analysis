import pandas as pd

def calc_macd(time, freq, f=26, s=12, t=9):
    macd = pd.DataFrame(index=time)
    macd['freq'] = freq
    macd['ema_12'] = macd['freq'].ewm(span=s).mean()
    macd['ema_26'] = macd['freq'].ewm(span=f).mean()
    macd['macd'] = macd['ema_12'] - macd['ema_26']
    macd['signal'] = macd['macd'].ewm(span=t).mean()
    macd['hist'] = macd['macd'] - macd['signal'] 
    
    return macd