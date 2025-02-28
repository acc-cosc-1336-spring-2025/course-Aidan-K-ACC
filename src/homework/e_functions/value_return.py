def get_hours(epoch_sec):
    hours= int((epoch_sec/3600)%24)
    return hours

def get_minutes(epoch_sec):
    mins= int((epoch_sec/60)%60)
    return mins

def get_seconds(epoch_sec):
    secs= int(epoch_sec%60)
    return secs