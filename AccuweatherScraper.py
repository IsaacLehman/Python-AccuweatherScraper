'''
    Scrapes Accuweather for a given location URL
    and returns a formated overiview of today.
    and tommorows weather.

    Example:
    NY = 'https://www.accuweather.com/en/us/new-york/10007/weather-forecast/349727'
    print(get_weather(NY, outline = True))

    Output:
    -------------------------------
    |  Weather For: New York, Ny  |
    -------------------------------

    Current weather (9:30 am)
    ------------------------------------------------
    • 43°f and Wind gusts
    • Realfeel® 41°
    • Wind: Fair
    • Gusts Up To: Nnw 12 mph


    Today’s weather forecast (4/26)
    ------------------------------------------------
    • 63°hi and Sunny; breezy this afternoon
    • Realfeel® 61°


    Tonight’s weather forecast (4/26)
    ------------------------------------------------
    • 46°lo and Clear to partly cloudy
    • Realfeel® 47°


    Tomorrow’s weather forecast (4/27)
    ------------------------------------------------
    • 68°/ 57° and Partly sunny and pleasant
    • Realfeel® 76°

'''
import requests, bs4, re
NEW_LINE = '\n'

def get_location(location, outline=False):
    loc = 'Weather For: ' + ' '.join([value.capitalize() for value in location[0].split(' ')])
    if outline:
        loc_length = len(loc)
        loc_str = (6+loc_length)*'-'+ NEW_LINE
        loc_str += '|  ' + loc + '  |' + NEW_LINE
        loc_str += (6+loc_length)*'-' + NEW_LINE
        return loc_str
    else:
        return loc + NEW_LINE

def weather_current_text(current):
    w_str = ''
    w_str += current[0] + ' (' + current[1] + ')' + NEW_LINE
    w_str += '------------------------------------------------' + NEW_LINE
    w_str += '• ' + current[2] + ' and ' + current[11] + NEW_LINE
    w_str += '• Realfeel® ' + current[4] + NEW_LINE
    w_str += '• Wind: ' + current[8] + NEW_LINE
    w_str += '• Gusts Up To: ' + current[10] + NEW_LINE
    return w_str

def weather_card_text(card):
    w_str = ''
    w_str += card[0] + ' (' + card[1] + ')' + NEW_LINE
    w_str += '------------------------------------------------' + NEW_LINE
    w_str += '• ' + card[2] + ' and ' + card[4] + NEW_LINE
    w_str += '• ' + card[3] + NEW_LINE
    return w_str

def get_weather(url, outline=False):
    headers = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url,  headers=headers)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        return
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    selectors = ['.header-loc', '.cur-con-weather-card', 'div[data-qa="todayWeatherCard"]', 'div[data-qa="tonightWeatherCard"]', 'div[data-qa="tomorrowWeatherCard"]']
    weather = []
    for sel in selectors:
        data = soup.select(sel)
        for line in data:
            text = line.getText()
            weather.append( [value.capitalize() for value in re.split('\n|\t', text) if value not in [' ', '']] )

    w_str = NEW_LINE
    w_str += get_location(weather[0], outline) + NEW_LINE
    w_str += weather_current_text(weather[1])
    for i in range(2,len(weather)):
        w_str += NEW_LINE + NEW_LINE
        w_str += weather_card_text(weather[i])

    return w_str
