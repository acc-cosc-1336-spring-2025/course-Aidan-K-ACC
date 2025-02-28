from value_return import get_hours
from value_return import get_minutes
from value_return import get_seconds

def display_human_clock(epoch_sec):
    hours= get_hours(epoch_sec)
    mins= get_minutes(epoch_sec)
    secs= get_seconds(epoch_sec)
    print(str(time_to_txt(hours))+":"+str(time_to_txt(mins))+":"+str(time_to_txt(secs)))

def time_to_txt(mhs):
    timetxt= ""
    if mhs < 10:
        timetxt= "0"+str(mhs)
    else:
        timetxt= str(mhs)
    return timetxt

