from datetime import date, datetime, timedelta

def mondays(date1, date2):
    months_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    month1, day1, year1 = date1.split(" ")
    day1 = day1[:-1]
    month2, day2, year2 = date2.split(" ")
    day2 = day2[:-1]

    d1 = date(int(year1), months_dict[month1], int(day1))
    d2 = date(int(year2), months_dict[month2], int(day2))
    index = 0
    week = timedelta(days = +7)
    day = timedelta(days = +1)

    if d1.weekday() == 0:
        while d1 <= d2:
            d1 = d1 + week
            index += 1
        return index
    else:
        while d1.weekday() != 0:
            d1 = d1 + day
        while d1 <= d2:
            d1 = d1 + week
            index += 1
        return index

        

assert mondays('July 2, 2024', 'August 16, 2024') == 6, mondays('July 2, 2024', 'August 16, 2024')
assert mondays('July 1, 2024', 'August 16, 2024') == 7, mondays('July 2, 2024', 'August 16, 2024')