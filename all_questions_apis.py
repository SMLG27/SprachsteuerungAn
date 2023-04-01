import requests
import translators as ts
import time
#import wikipedia
import datetime
from main import al_talk, al_talk_en, al_listen



# news api key
news_api_key = 'b56c37f508ba406bbb8dfb58c9ef67cd'
# weather api key
weather_api_key = 'f5624a4b08f77d74576ef4211efe8dae'


def translator(text):
    al_talk_en(ts.google(text, from_language='de', to_language='en'))


def get_news():
    news = 'https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=' + news_api_key
    news_json = requests.get(news).json()
    articles = news_json['articles']

    news_headlines = []
    for x in articles:
        news_headlines.append(x['title'])

    for i in range(3):
        print(news_headlines[i])
        al_talk(news_headlines[i])


def get_weather():
    al_talk('Kein Problem, für welche Stadt soll ich das Wetter nachsehen?')
    weather_input = al_listen()

    weather_url = 'https://api.weatherbit.io/v2.0/current?city=' + weather_input + '&key=' + weather_api_key
    weather_json = requests.get(weather_url).json()
    print(weather_json)
    temperature = weather_json['data'][0]['temp']
    print(temperature)
    al_talk('Die Temperatur in ' + weather_input + ' beträgt ' + str(temperature) + ' Grad')


def distance_info():
    # Distance API Key
    distance_api_key = '5QZwAHClpfw57RBpsynefNaQtKxUomLG'

    al_talk('Klar, was ist der Startpunkt?')
    location_one = al_listen()
    print(location_one)
    time.sleep(1)
    al_talk('Okay, und der Endpunkt?')
    location_two = al_listen()
    print(location_two)
    al_talk('Gib mir einen Moment. Ich nutze mein schlaues Köpfchen um es für Dich zu berechnen.')

    dist_url = 'http://www.mapquestapi.com/directions/v2/route?key=dQSkftNrwKqZ9Xt4vcoYGQu3ORKHSGrs&from=' + location_one + '&to=' + location_two + '&unit=k'
    dist_request = requests.get(dist_url).json()
    distance_km = round(dist_request['route']['distance'], 2)
    distance_result = 'Die Entfernung zwischen ' + location_one + ' und ' + location_two + ' beträgt ' + str(
        distance_km) + ' Kilometer'
    print(distance_result)
    al_talk(distance_result)


#def wikipedia_info():
    #alina_talk('Ich schaue gerne für Dich nach. Wonach soll ich suchen?')
    #wikipedia.set_lang('de')
    #wiki_listen = alina_listen()
    #wiki_result = wikipedia.summary(wiki_listen, sentences=1)
    #print(wiki_result)
    #alina_talk(wiki_result)


def get_time_now():
    today_date = datetime.datetime.now()
    hour = today_date.strftime("%H")
    minute = today_date.strftime("%M")
    time_now = 'Es ist ' + hour + ':' + minute
    print(time_now)
    al_talk(time_now)