import datetime
import time

#=========コメントデータの前処理をします=======#

# 時間パラメータを
def reformat_time(t_str):
    try:
        x = time.strptime(t_str, '%H:%M:%S')
    except ValueError as e:
        x = time.strptime(t_str, '%M:%S')
#     t = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return time.strftime('%H:%M:%S', x)
