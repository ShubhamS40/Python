# import os as os
# import speech_recognition as sr
# import pyttsx3 as pyttx
# import musicLibrary as musiclibrary
# import webbrowser as webbrowser
# import requests
# engine =pyttx.init()

# recongnizer=sr.Recognizer()


# def aiProcess(command):
#     """Send a question to the API and get the response"""
#     url = "https://chat-gtp-free.p.rapidapi.com/v1/chat/completions"

#     payload = {
#         "chatId": "92d97036-3e25-442b-9a25-096ab45b0525",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": "You are a virtual assistant. Your name is Karen and you would like to be a firefighter."
#             },
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     }
#     headers = {
#         "x-rapidapi-key": "f7eaba5953msh17aea7db0d26924p10a024jsn0a900b09ebd4",
#         "x-rapidapi-host": "chat-gtp-free.p.rapidapi.com",
#         "Content-Type": "application/json"
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     response_data = response.json()
#     answer = response_data.get('choices', [{}])[0].get('message', {}).get('content', 'Sorry, I could not get a response.')
#     return answer
    


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processcommand(c):
#     print(c)
#     if(c.lower()=="open google"):
#         speak("I Open The  Google Sir")
#         webbrowser.open("https://google.com")
#     elif(c.lower()=="open youtube"):
#         speak("I Open The  Youtube Sir")
#         webbrowser.open("https://youtube.com")
#     elif(c.lower()=="check t20 score"):
#         webbrowser.open("https://https://www.google.com/search?q=t20&oq=t20&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQLhhA0gEIMTQyNmowajGoAgCwAgA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11h9kdbjq6;5;/m/026y268;mt;fp;1;;;")        
#     elif c.lower().startswith("play"):
#         print(c.lower())
#         song=c.lower().spilt(" ")[1]
#         link=musiclibrary.music[song]
#         webbrowser.open(link)
#     else:
#         answer = aiProcess(c)
#         speak(answer)        
# if True:
#     speak("Initalizing Jarvas")
#     while True:
#         # Listen for The Wake Word Jarvas
#         # Obtain Audio From the Microphone
       
#         print("Recongnizing")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening!!")
#                 audio=recongnizer.listen(source,timeout=5,phrase_time_limit=1)
#             command=recongnizer.recognize_google(audio)
#             if (command.lower()=="jarvis"):
#                 speak("ya")
#                 with sr.Microphone() as source:
#                     print("Jarvis Active")
#                     audio=recongnizer.listen(source,timeout=2,phrase_time_limit=1)
#                     command=recongnizer.recognize_google(audio)
#                     print("ok")
#                     processcommand(command)

#         except:
#             print("sphinx could not recongnize audio")    
    
import os
import speech_recognition as sr
import pyttsx3 as pyttx
import webbrowser
import requests

# Initialize text-to-speech engine
engine = pyttx.init()
# Initialize speech recognizer
recognizer = sr.Recognizer()

def aiProcess(command):
    """Send a question to the API and get the response"""
    url = "https://chat-gtp-free.p.rapidapi.com/v1/chat/completions"

    payload = {
        "chatId": "92d97036-3e25-442b-9a25-096ab45b0525",
        "messages": [
            {
                "role": "system",
                "content": "You are a virtual assistant"
            },
            {
                "role": "user",
                "content": command
            }
        ]
    }
    headers = {
        "x-rapidapi-key": "f7eaba5953msh17aea7db0d26924p10a024jsn0a900b09ebd4",
        "x-rapidapi-host": "chat-gtp-free.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        response_data = response.json()
        print(response_data)
        answer = response_data["text"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching response from API: {e}")
        answer = "Sorry, I could not get a response from the server."

    return answer

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    """Process recognized commands"""
    print(c)
    if c.lower() == "open google":
        speak("I'm opening Google, Sir.")
        webbrowser.open("https://google.com")
    elif c.lower() == "open youtube":
        speak("I'm opening YouTube, Sir.")
        webbrowser.open("https://youtube.com")
    elif c.lower() == "check t20 score":
        webbrowser.open("https://www.google.com/search?q=t20")
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ")[1]
            # Mocking music library dictionary for example
            music_library = {
                "song": "https://www.youtube.com/watch?v=Fxoxd0ovKn4",
                "song2": "https://example.com/song2.mp3"
            }
            link = music_library.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song}.")
        except IndexError:
            speak("Please specify a song to play.")
    else:
        answer = aiProcess(c)
        speak(answer)

if True:
    speak("Initializing Jarvis")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            if command.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print("Processing command...")
                processcommand(command)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Error with SpeechRecognition service: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
                