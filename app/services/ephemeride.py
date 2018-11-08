from datetime import *

import ephem
import app.model.day as day


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


def get_times_by_observer(observer, date, body):
    previous_rising_date = observer.previous_rising(body)
    next_rising_date = observer.next_rising(body)
    previous_setting_date = observer.previous_setting(body)
    next_setting_date = observer.next_setting(body)

    rising_time = None
    setting_time = None

    if ephem.localtime(previous_rising_date).date() == date:
        rising_time = ephem.localtime(previous_rising_date).isoformat()
    elif ephem.localtime(next_rising_date).date() == date:
        rising_time = ephem.localtime(next_rising_date).isoformat()

    if ephem.localtime(previous_setting_date).date() == date:
        setting_time = ephem.localtime(previous_setting_date).isoformat()
    elif ephem.localtime(next_setting_date).date() == date:
        setting_time = ephem.localtime(next_setting_date).isoformat()

    return rising_time, setting_time


def create_observer(lon, lat, horizon, date):
    observer = ephem.Observer()
    observer.lat = lon
    observer.lon = lat
    observer.horizon = horizon
    observer.pressure = 0
    observer.date = date

    return observer


def get_day_info(body, today):
    info = {'name': body.name}

    lon = '-0:34:48'
    lat = '44:50:24'

    observer = create_observer(lon, lat, '-0:34', today)

    body.compute(observer)

    info['rising'], info['setting'] = get_times_by_observer(observer, today, body)

    if body.name == 'Sun':
        civil_observer = create_observer(lon, lat, str(ephem.degrees(ephem.degrees("-6") + body.radius / 2)), today)
        nautical_observer = create_observer(lon, lat, str(ephem.degrees(ephem.degrees("-12") + body.radius / 2)), today)
        astronomical_observer = create_observer(lon, lat, str(ephem.degrees(ephem.degrees("-18") + body.radius / 2)), today)

        info['rising_civil'], info['setting_civil'] = get_times_by_observer(civil_observer, today, body)
        info['rising_naval'], info['setting_naval'] = get_times_by_observer(nautical_observer, today, body)
        info['rising_astronomical'], info['setting_astronomical'] = get_times_by_observer(astronomical_observer, today, body)

    return info
