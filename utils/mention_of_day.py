import re

from utils.persian_datetime import persian_date

mentions = {
    "شنبه": "یا رب العالمین",
    "یکشنبه": "یا ذاالجلال و الاکرام",
    "دوشنبه": "یا قاضی الحاجات",
    "سه‌شنبه": "یا ارحم الراحمین",
    "چهارشنبه": "یا حی یا قیوم",
    "پنجشنبه": "لا اله الا الله الملک الحق المبین",
    "جمعه": "اللهم صل علی محمد و آل محمد",
}

def find_mention_of_the_day():
    days_of_the_week = mentions.keys()
    for day in days_of_the_week:
        pattern = re.match(day, persian_date())
        if pattern:
            return mentions[pattern.group()]
