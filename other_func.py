
def weekday_german(weekday_today):
    if 'monday' in weekday_today.lower():
        return 'montag'
    elif 'tuesday' in weekday_today.lower():
        return 'dienstag'
    elif 'wednesday' in weekday_today.lower():
        return 'mittwoch'
    elif 'thursday' in weekday_today.lower():
        return 'donnerstag'
    elif 'friday' in weekday_today.lower():
        return 'freitag'
    elif 'saturday' in weekday_today.lower():
        return 'samstag'
    else:
        return 'sonntag'