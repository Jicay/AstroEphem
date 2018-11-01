from datetime import *

import ephem
import astroephem.model.day as day


def compute_planet(planet):
    if planet == 'mars':
        m = ephem.Mars()
        m.compute()
        return m
    pass


def get_current_days():

    days = []

    today = date.today()

    for i in range(7):
        current_date = today + timedelta(days=i)

        sun_info = get_day_info(ephem.Sun(), current_date)
        moon_info = get_day_info(ephem.Moon(), current_date)
        venus_info = get_day_info(ephem.Venus(), current_date)
        mars_info = get_day_info(ephem.Mars(), current_date)
        jupiter_info = get_day_info(ephem.Jupiter(), current_date)
        saturn_info = get_day_info(ephem.Saturn(), current_date)

        d = day.Day(sun=sun_info, moon=moon_info, venus=venus_info, mars=mars_info, jupiter=jupiter_info, saturn=saturn_info, date=current_date.isoformat())
        days.append(d)

    return days
    pass


def get_day_info(body, today):
    info = {'name': body.name}

    observer = ephem.Observer()
    observer.lat = '44:50:16.04'
    observer.lon = '-0:34:45.048'
    observer.date = today

    body.compute(observer)

    previous_rising_date = observer.previous_rising(body)
    next_rising_date = observer.next_rising(body)
    previous_setting_date = observer.previous_setting(body)
    next_setting_date = observer.next_setting(body)

    if ephem.localtime(previous_rising_date).date() == today:
        info['rising'] = ephem.localtime(previous_rising_date).isoformat()
    elif ephem.localtime(next_rising_date).date() == today:
        info['rising'] = ephem.localtime(next_rising_date).isoformat()
    else:
        info['rising'] = None

    if ephem.localtime(previous_setting_date).date() == today:
        info['setting'] = ephem.localtime(previous_setting_date).isoformat()
    elif ephem.localtime(next_setting_date).date() == today:
        info['setting'] = ephem.localtime(next_setting_date).isoformat()
    else:
        info['setting'] = None

    return info
