from persiantools.jdatetime import JalaliDate
from persiantools.digits import fa_to_en

def persian_date():
    p_date = JalaliDate.today().strftime("%c", locale="fa")
    return p_date

def convert_calender_to_persian():
    today_jalali = JalaliDate.today()
    return today_jalali
    
def convert_slash_to_dash(date: str):
    dashed = date.replace("/","-")
    to_en = fa_to_en(dashed)
    return to_en
