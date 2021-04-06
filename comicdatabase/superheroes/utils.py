import datetime


def parse_date_string(string_to_parse):
    date_time_object = datetime.datetime.strptime(string_to_parse, '%b %d %Y')
    return date_time_object
