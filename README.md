# Python-AccuweatherScraper

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
