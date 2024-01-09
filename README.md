Sprachsteuerung

Dieses Skript ist ein Sprachassistent, ähnlich wie Siri oder Google Assistant. Es verwendet die Python-Bibliothek
speech_recognition für die Spracherkennung, gTTS für die Text-to-Speech-Funktionalität, playsound zum Abspielen 
von Audiodateien und os für Betriebssysteminteraktionen.
Die Funktion al_talk konvertiert übergebenen Text in gesprochene Sprache und spielt ihn ab. 
Die Funktion al_listen nimmt über das Mikrofon gesprochene Sprache auf und konvertiert sie in Text. 
Es gibt auch eine Variante für englische Sprachausgabe (al_talk_en). Die Funktion execute_assistant startet den Assistenten, 
begrüßt den Benutzer und fordert ihn auf, eine Anfrage zu stellen. Die Antworten des Assistenten hängen von den Funktionen 
in check_replays und der alina_reply-Funktion ab. Wenn das Wort "stop" erkannt wird, beendet das Skript die Ausführung.
