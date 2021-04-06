from datetime import datetime


def parse_date_string(string_to_parse):
    date_time_object = datetime.strptime(string_to_parse, '%B %d, %Y')
    return date_time_object.date()


