import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from toolss import timeit


#  if you have problem with playsound use this pip install playsound==1.2.2
# pip install pipwin
# pipwin install pyaudio





# text zur sprache konvertieren, sodass der übergebene text im audioformat ausgegeben werden kann
@timeit
def alina_talk(text):
    # erzeuge audio datei
    file_name = 'audio_data.mp3'
    # konvertiere text zu sprache
    tts = gTTS(text=text, lang='de')
    # speichern
    tts.save(file_name)
    # abspielen
    playsound.playsound(file_name)
    # löschen
    os.remove(file_name)

# sprache zu text konovertieren - sodass wir den text im nächsten schritt verwenden können
@timeit
def alina_listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        audio = r.listen(source)
        text = ''

        try:
            text = r.recognize_google(audio, language='de-DE')

        except sr.RequestError as re:
            print(re)

        except sr.UnknownValueError as uve:
            print(uve)

        except sr.WaitTimeoutError as wte:
            print(wte)

    text = text.lower()
    return text

# englisch
@timeit
def alina_talk_en(text):
    # erzeuge audio datei
    file_name = 'audio_data.mp3'
    # konvertiere text zu sprache
    tts = gTTS(text=text, lang='en')
    # speichern
    tts.save(file_name)
    # abspielen
    playsound.playsound(file_name)
    # löschen
    os.remove(file_name)

@timeit
def execute_assistant():
    from check_replays import alina_reply
    # personalisieren
    alina_talk('Hi, ich bin Alina und möchte Dich unterstützen. Wie ist Dein Name?')
    listen_name = alina_listen()
    alina_talk('Hi   ' + listen_name + ' Was kann ich für Dich tun?')

    while True:
        listen_alina = alina_listen()
        print(listen_alina)
        alina_reply(listen_alina)

        if 'stop' in listen_alina or 'stopp' in listen_alina:
            break



if __name__ == '__main__':
    execute_assistant()
