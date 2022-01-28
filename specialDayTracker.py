
def specialDayCalculator():

    global specialDay
    specialDay = float(0.0)

    from datetime import date

    dayToday = date.today()

    month = dayToday.month
    day = dayToday.day

    day1Jan = ()
    day8Jan = ()
    day6Jan = ()
    day4Jan = ()
    day2Jan = ()

    day1Feb = (14,)
    day8Feb = (13, 15)
    day6Feb = (11, 12)
    day4Feb = (9, 10)
    day2Feb = ()

    day1Mar = ()
    day8Mar = ()
    day6Mar = ()
    day4Mar = ()
    day2Mar = ()

    day1Apr = ()
    day8Apr = ()
    day6Apr = ()
    day4Apr = ()
    day2Apr = (30,)

    day1May = (8,)
    day8May = (7, 9)
    day6May = (3, 4, 5)
    day4May = (1, 2)

    day1Jun = ()
    day8Jun = ()
    day6Jun = ()
    day4Jun = ()
    day2Jun = ()

    day1Jul = ()
    day8Jul = ()
    day6Jul = ()
    day4Jul = ()
    day2Jul = ()

    day1Aug = (
    1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31)
    day8Aug = ()
    day6Aug = ()
    day4Aug = ()
    day2Aug = ()

    day1Sept = (1, 2, 3, 4, 5)
    day8Sept = ()
    day6Sept = (6, 7, 8, 9, 10)
    day4Sept = ()
    day2Sept = (11, 12, 13, 14)

    day1Oct = (24, 30, 31)
    day8Oct = (22, 23, 28, 29)
    day6Oct = (19, 20, 21)
    day4Oct = (17, 18)
    day2Oct = (16,)

    day1Nov = (11, 20, 21, 22, 23, 24, 25, 26)
    day8Nov = ()
    day6Nov = (10,)
    day4Nov = (9,)
    day2Nov = (7, 8)

    day1Dec = (24, 25, 26)
    day8Dec = (21, 22, 23)
    day6Dec = (19, 20, 27, 28)
    day4Dec = (17, 18, 29)
    day2Dec = (14, 15, 16, 30, 31)

    if month == 1:
        if day in day1Jan:
            specialDay = 1.0
        elif day in day8Jan:
            specialDay = 0.8
        elif day in day6Jan:
            specialDay = 0.6
        elif day in day4Jan:
            specialDay = 0.4
        elif day in day2Jan:
            specialDay = 0.2
    elif month == 2:
        if day in day1Feb:
            specialDay = 1.0
        elif day in day8Feb:
            specialDay = 0.8
        elif day in day6Feb:
            specialDay = 0.6
        elif day in day4Feb:
            specialDay = 0.4
        elif day in day2Feb:
            specialDay = 0.2
    elif month == 3:
        if day in day1Mar:
            specialDay = 1.0
        elif day in day8Mar:
            specialDay = 0.8
        elif day in day6Mar:
            specialDay = 0.6
        elif day in day4Mar:
            specialDay = 0.4
        elif day in day2Mar:
            specialDay = 0.2
    elif month == 4:
        if day in day1Apr:
            specialDay = 1.0
        elif day in day8Apr:
            specialDay = 0.8
        elif day in day6Apr:
            specialDay = 0.6
        elif day in day4Apr:
            specialDay = 0.4
        elif day in day2Apr:
            specialDay = 0.2
    elif month == 5:
        if day in day1May:
            specialDay = 1.0
        elif day in day8May:
            specialDay = 0.8
        elif day in day6May:
            specialDay = 0.6
        elif day in day4May:
            specialDay = 0.4
        elif day in day2May:
            specialDay = 0.2
    elif month == 6:
        if day in day1Jun:
            specialDay = 1.0
        elif day in day8Jun:
            specialDay = 0.8
        elif day in day6Jun:
            specialDay = 0.6
        elif day in day4Jun:
            specialDay = 0.4
        elif day in day2Jun:
            specialDay = 0.2
    elif month == 7:
        if day in day1Jul:
            specialDay = 1.0
        elif day in day8Jul:
            specialDay = 0.8
        elif day in day6Jul:
            specialDay = 0.6
        elif day in day4Jul:
            specialDay = 0.4
        elif day in day2Jul:
            specialDay = 0.2
    elif month == 8:
        if day in day1Aug:
            specialDay = 1.0
        elif day in day8Aug:
            specialDay = 0.8
        elif day in day6Aug:
            specialDay = 0.6
        elif day in day4Aug:
            specialDay = 0.4
        elif day in day2Aug:
            specialDay = 0.2
    elif month == 9:
        if day in day1Sept:
            specialDay = 1.0
        elif day in day8Sept:
            specialDay = 0.8
        elif day in day6Sept:
            specialDay = 0.6
        elif day in day4Sept:
            specialDay = 0.4
        elif day in day2Sept:
            specialDay = 0.2
    elif month == 10:
        if day in day1Oct:
            specialDay = 1.0
        elif day in day8Oct:
            specialDay = 0.8
        elif day in day6Oct:
            specialDay = 0.6
        elif day in day4Oct:
            specialDay = 0.4
        elif day in day2Oct:
            specialDay = 0.2
    elif month == 11:
        if day in day1Nov:
            specialDay = 1.0
        elif day in day8Nov:
            specialDay = 0.8
        elif day in day6Nov:
            specialDay = 0.6
        elif day in day4Nov:
            specialDay = 0.4
        elif day in day2Nov:
            specialDay = 0.2
    elif month == 12:
        if day in day1Dec:
            specialDay = 1.0
        elif day in day8Dec:
            specialDay = 0.8
        elif day in day6Dec:
            specialDay = 0.6
        elif day in day4Dec:
            specialDay = 0.4
        elif day in day2Dec:
            specialDay = 0.2

    return specialDay





