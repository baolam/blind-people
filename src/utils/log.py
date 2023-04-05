import datetime

def log(content):
    date = datetime.datetime.now()
    date = '{}:{}:{}'.format(date.hour, date.minute, date.second)
    con = '{} - {}'.format(date, content)
    print(con)