import ephem

def compute_planet(planet):
    if planet == 'mars':
        m = ephem.Mars()
        m.compute()
        return m
    pass

def get_current_days():
    sunInfo = get_day_info(ephem.Sun())

    pass

def get_day_info(body):
    info = {}

    now = ephem.now()

    observer = ephem.Observer()



    return info