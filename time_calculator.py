def add_time(start, duration, day='null'):
    hour1 = start.split()
    hour1[0] = (hour1[0].split(':'))
    hour2 = duration.split(':')
    new_hour = int(hour1[0][0]) + int(hour2[0])
    new_minutes = int(hour1[0][1]) + int(hour2[1])
    if new_minutes >= 60:
        new_minutes -= 60
        new_hour += 1
    counter = 0
    while new_hour >= 12:
        new_hour -= 12
        counter += 1
    days = 0
    if new_hour == 0:
        new_hour = 12
    while counter > 0:
        if hour1[1].upper() == 'PM':
            hour1[1] = 'AM'
            days += 1
        elif hour1[1].upper() == 'AM':
            hour1[1] = 'PM'
        counter -= 1
    if day == 'null':
        if days == 0:
            new_time = f'{new_hour}:{new_minutes:02d} {hour1[1]}'
        elif days == 1:
            new_time = f'{new_hour}:{new_minutes:02d} {hour1[1]} (next day)'        
        else:
            new_time = f'{new_hour}:{new_minutes:02d} {hour1[1]} ({days} days later)'
    else:
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        counter = week.index(day.capitalize())
        counter = (counter + days) % 7
        new_day = week[counter]
        if days == 0:
            new_time = f'{new_hour}:{new_minutes:02d} {hour1[1]}, {new_day}'
        elif days == 1:
            new_time = f'{new_hour}:{new_minutes:02d} {hour1[1]}, {new_day} (next day)'
        else:
            new_time = f'{new_hour}:{new_minutes:02d} {hour1[1]}, {new_day} ({days} days later)'       
    return new_time
