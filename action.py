import webbrowser
import text_to_speech
import spech_to_text
import datetime
import weather

def Action(data):
    user_data =data.lower()
    
    if"what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return"My name is Virtual Assistant"
    
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hey, sir How i can help you")
        return"hey, sir How i can help you"

    elif"good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return"good morning sir"


    elif"time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time)+ "Hour:", (str)(current_time.minute)+ "Minute"
        text_to_speech.text_to_speech(Time)
        return Time


    elif"shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return"ok sir"


    elif"open youtube" in user_data:
        webbrowser.open("https://youtube.com")
        text_to_speech.text_to_speech("youtube.com is ready for you")
        return"youtube.com is ready for you"

    elif"play music" in user_data:
        webbrowser.open("https://ganna.com")
        text_to_speech.text_to_speech("ganna.com is ready for you")
        return"ganna.com is ready for you"

    elif"open google" in user_data:
        webbrowser.open("https://google.com")
        text_to_speech.text_to_speech("google.com is ready for you")
        return"google.com is ready for you"

    elif"weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)


    else:
        text_to_speech.text_to_speech("I'am not able to understand")