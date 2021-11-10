from datetime import datetime


def convert_timestamp_to_day(timestamp):
    if type(timestamp) not in {int, float}:
        raise TypeError("Timestamp must be integer or float")

    dt_obj = datetime.fromtimestamp(timestamp/1000).strftime('%d')
    return dt_obj