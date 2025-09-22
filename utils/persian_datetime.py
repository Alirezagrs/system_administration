import jdatetime
from persiantools.jdatetime import JalaliDate


def persian_date():
    p_date = JalaliDate.today().strftime("%c", locale="fa")
    return p_date

def convert_calender_to_persian():
    today_jalali = jdatetime.date.today()
    return today_jalali
    