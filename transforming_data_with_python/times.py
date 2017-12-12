from read import load_data
from dateutil.parser import parse
from dateutil.parser import parserinfo

df = load_data() 

H = [('h', 'hour', 'hours')]
def hour_only(date_stamp):
    time = parse(date_stamp, parserinfo=parserinfo(H))
    hour = time.split(':')[0]
    hour = hour.spit(' ')[1]
    
    return(time)


print(hour_only(df.loc[0,'submission_time']))