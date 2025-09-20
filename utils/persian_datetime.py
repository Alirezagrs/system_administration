from persiantools.jdatetime import JalaliDate


def persian_date():
    p_date = JalaliDate.today().strftime("%c", locale="fa")
    return p_date
