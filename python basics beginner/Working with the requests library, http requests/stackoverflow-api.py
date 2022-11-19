import datetime

import requests

url = 'https://api.stackexchange.com/2.3/questions'

today = datetime.date.today()
from_day = today - datetime.timedelta(2)


def get_questions(todate, fromdate, tag: str):
    params = {
        'site': 'Stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'fromdate': f'{fromdate}',
        'todate': f'{todate}',
        'tagged': tag
    }
    response = requests.get(url=url, params=params).json()
    questions = {}
    for items in response['items']:
        unix_date = items['last_activity_date']
        date = datetime.datetime.utcfromtimestamp(unix_date).strftime('%Y-%m-%d')
        questions.setdefault(items['question_id'], {date: items['link']})

    return questions

print(get_questions(today, from_day, tag='python'))