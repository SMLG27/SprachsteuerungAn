from other_func import weekday_german
from all_questions_apis import get_news
#from apis_for_question import wikipedia_info
from all_questions_apis import get_weather
from all_questions_apis import get_time_now
from all_questions_apis import translator
from all_questions_apis import distance_info
from main import alina_talk, alina_listen
import yfinance as yf
import datetime
import requests
from toolss import write_new_replays


apple = yf.Ticker('AAPL')
tesla = yf.Ticker('TSLA')
facebook = yf.Ticker('FB')

# crypto API
crypto_api = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Csolana&vs_currencies=usd'



# Weekday Today
weekday_today = datetime.datetime.now().strftime("%A")




def alina_reply(text):
    # Smalltalk - Wie ist Dein Name?
    if 'wie' in text and 'name' in text:
        alina_talk('Ich bin die Alina und bin Deine persönliche Sprachassistentin.')

    # Smalltalk - Warum existiert du?
    elif 'warum' in text and 'existierst' in text:
        alina_talk('Ich wurde geschaffen um für Dich zu arbeiten. Ich brauche keine Pausen und keine Auszeit.')

    # Smalltalk - Wann schläfst du?
    elif 'wann' in text and 'schläfst' in text:
        alina_talk('Ich schlafe nie. Ich arbeite 24 Stunden')

    # Smalltalk - Bist du dumm?
    elif 'bist' in text and 'dumm' in text:
        alina_talk('Nein, ich bin nicht dumm. Meine Großmutter hat gesagt, dass es keine dummen Menschen gibt.'
                   + 'Ich gebe mein bestes, um jeden Tag etwas neues zu lernen.')

    # Smalltalk - Lieblingsfilm
    elif 'film' in text or 'lieblingsfilm' in text:
        alina_talk('Ich schaue am liebsten Titanic. Ich habe ihn mir bestimmt schon mehr als 20 mal angesehen.')

    # Kryptowährungen - Bitcoin
    elif 'bitcoin' in text:
        response = requests.get(crypto_api).json()
        price_bitcoin = response['bitcoin']['usd']
        print(price_bitcoin)
        alina_talk('Der aktuelle Preis für einen Bitcoin liegt bei ' + str(price_bitcoin) + ' US Dollar')

    # Kryptowährungen - Litecoin
    elif 'litecoin' in text:
        response = requests.get(crypto_api).json()
        price_litecoin = response['litecoin']['usd']
        print(price_litecoin)
        alina_talk('Der aktuelle Preis für einen Litecoin liegt bei ' + str(price_litecoin) + ' US Dollar')

    # Kryptowährungen - Solana
    elif 'solana' in text:
        response = requests.get(crypto_api).json()
        price_solana = response['solana']['usd']
        print(price_solana)
        alina_talk('Der aktuelle Preis für einen Solana Coin liegt bei ' + str(price_solana) + ' US Dollar')

    # Aktien - Apple
    elif 'apple' in text:
        apple_stock_price = apple.info['regularMarketPrice']
        print(apple_stock_price)
        alina_talk('Zu diesem Zeitpunkt kannst Du eine Aktie von Apple für ' + str(apple_stock_price).replace('.',
                                                                                                              ',') + ' US Dollar kaufen')

    # Aktien - Tesla
    elif 'tesla' in text:
        tesla_stock_price = tesla.info['regularMarketPrice']
        print(tesla_stock_price)
        alina_talk('Zu diesem Zeitpunkt kannst Du eine Aktie von Tesla für ' + str(tesla_stock_price).replace('.',
                                                                                                              ',') + ' US Dollar kaufen')

    # Aktien - Facebook
    elif 'facebook' in text:
        facebook_stock_price = facebook.info['regularMarketPrice']
        print(facebook_stock_price)
        alina_talk('Zu diesem Zeitpunkt kannst Du eine Aktie von Facebook für ' + str(facebook_stock_price).replace('.',
                                                                                                                    ',') + ' US Dollar kaufen')

        # Übersetzer (DE-EN)
    elif 'übersetzen' in text or 'übersetzer' in text:
        alina_talk('Klar, sag mir einfach was ich übersetzen soll.')

        while True:
            text_to_translate = alina_listen()
            print(text_to_translate)

            if text_to_translate != 'übersetzer ausschalten':
                translator(text_to_translate)

            else:
                alina_talk('Ich habe den Übersetzer ausgeschaltet. Kann ich sonst noch etwas für Dich tun?')
                break

    # News
    elif 'news' in text or 'nachrichten' in text:
        alina_talk('Kein Problem, hier sind die Top 3 Nachrichten von heute')
        get_news()

    # Wetter
    elif 'wetter' in text:
        get_weather()

    # Entfernung
    elif 'distanz' in text or 'entfernung' in text:
        distance_info()

    # Wikipedia
    #elif 'wikipedia' in text:
        #wikipedia_info()

    # Uhrzeit
    elif 'wie' in text and 'spät' in text:
        get_time_now()

    # Wochentag
    elif 'wochentag' in text:
        alina_talk('Heute ist ' + weekday_german(weekday_today))

    elif 'stop' in text or 'stopp' in text:
        alina_talk('Es war mir eine Freude Dir zu helfen. Ich wünsche Dir einen wundervollen Tag.')

    else:
        alina_talk('Entschuldige, ich habe Dich nicht verstanden. Könntest Du das bitte wiederholen?')
        write_new_replays(text)

