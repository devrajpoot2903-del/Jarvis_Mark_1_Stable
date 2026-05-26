import pygame
import os
import win32com.client
import datetime
import time
import webbrowser
import speech_recognition as sr
import threading
import subprocess
from difflib import get_close_matches

# =========================================
# VOICE FUNCTION
# =========================================

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)


# =========================================
# PYGAME INIT
# =========================================

pygame.init()

# =========================================
# COLORS
# =========================================

white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)
red = (255, 0, 0)

# =========================================
# SCREEN SETUP
# =========================================

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Jarvis AI Assistant")

font = pygame.font.SysFont(None, 45)

def text_screen(text, colour, x, y):

    screen_text = font.render(text, True, colour)

    screen.blit(screen_text, [x, y])


# =========================================
# VARIABLES
# =========================================

run = True 


response_displayed = "Starting Jarvis..."

is_listening = False
assistant_mode= "sleep"

# =========================================
# COMMANDS
# =========================================

web_commands = {

    "linkedin" : "https://www.linkedin.com/in/dev-rajput-98086a320?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" ,
    "gdg" : "https://gdg.community.dev/",
    "internshala": "https://internshala.com/jobs/",
    "insta" :   "https://www.instagram.com",
    "erp": "https://portal.vmedulife.com/public/auth/#/login/oist-bhopal",
    "oist" : "https://oriental.ac.in/",
    "youtube": "https://www.youtube.com",
    "spotify": "https://open.spotify.com",
    "google": "https://www.google.com",
    "wikipedia": "https://www.wikipedia.com",
    "whatsapp": "https://web.whatsapp.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "instagram": "https://www.instagram.com",
    "chatgpt": "https://chat.openai.com",
    "github" : "https://github.com/devrajpoot2903-del"
}

chatbot_responses = {
    
    "opretion you can perform":"i can  perform sever thngs , like opning  websites ,opning difrent desktopapps , etc,  how can i help you sir sir !",
    "how are you": "I am fine sir! How are you?",
    "Who am i":"You are Dev Rajpoot  , MY  master  sir !",
    "my name ":"You name is Dev Rajpoot  ,  sir ! , how can i help you !",
    "hello": "Hello sir! How can I help you today?",
    "hi": "Hello sir! How can I help you today?",
    "your name": "I am Jarvis AI, your personal assistant sir !",
    "thanks": "You are welcome sir!",
    "thank you": "You are welcome!"
}


# =========================================
# SMART MATCH
# =========================================

def smart_match(user_input, command_dict):

    user_lower = user_input.lower()

    keys = list(command_dict.keys())

    match = get_close_matches(user_lower, keys, n=1, cutoff=0.6)

    if match:
        return match[0]

    return None


# =========================================
# COMMAND PROCESSOR
# =========================================

def process_command(query):

    global response_displayed
    global run

    matched_web = smart_match(query, web_commands)

    matched_chat = smart_match(query, chatbot_responses)

    # ---------- Websites ----------

    if matched_web:

        say(f"Opening {matched_web}")

        webbrowser.open(web_commands[matched_web])

        response_displayed = f"Opening {matched_web}"

    # ---------- Chat ----------

    elif matched_chat:

        say(chatbot_responses[matched_chat])

        response_displayed = chatbot_responses[matched_chat]

    # ---------- Time ----------

    elif "time" in query:

        strfTime = datetime.datetime.now().strftime("%H:%M:%S")

        say(f"Sir, the time is {strfTime}")

        response_displayed = f"Time: {strfTime}"

    #--------- sleep - shutdown ----------


    elif "sleep laptop" in query or "sleep system" in query:

        say("Putting system to sleep sir")

        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    elif "shutdown laptop" in query or "shutdown system" in query or "shutdown the laptop" in query:

        say("Shutting down the system sir")

        os.system("shutdown /s /t 7")


    elif "cancel shutdown" in query or "cancel the shutdown" in query:

        say("Shutdown cancelled")

        os.system("shutdown /a")



    elif "restart laptop" in query or "restart pc" in query:

        say("Restarting system sir")

        os.system("shutdown /r /t 7")





    #--------camra----------

    elif "open camera" in query:

        say("Opening camera")

        os.system("start microsoft.windows.camera:")



    #--------powerpoint-------
    elif "open powerpoint" in query or "open ms powerpoint" in query or "open microsoft powerpoint" in query:

        say("Opening PowerPoint")

        os.system("start powerpnt")


    #------word-----
    elif "open word" in query or "open ms word" in query or  "open microsoft word" in query :

        say("Opening Microsoft Word")

        os.system("start winword")



    #-------git bash ------

    elif "open git bash" in query or "open git" in query or "bash" in query :

        say("Opening Git Bash")

        subprocess.Popen([
            r"C:\Program Files\Git\git-bash.exe"
        ])
        
    # ---------- VS CODE ----------

    elif "open vscode" in query or "open vs code" in query or "open vs" in query or "open Vscode" in query or "open Vs code" in query or "open visual studio code" in query:

        say("Opening VS Code")

        subprocess.Popen([
            r"C:\Users\devra\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        ])

        response_displayed = "Opening VS Code"



    elif "open idle" in query or  "open i d l e" in query:
        say("opning  IDlE sir !")
        subprocess.Popen([r"C:\Users\devra\AppData\Local\Python\pythoncore-3.14-64\Lib\idlelib\idle.bat"])

        response_displayed = "Opening idle"

    
    elif "open python" in query or  "python" in query  :
        say("opning  python sir !")
        subprocess.Popen(["python"])
        response_displayed = "Opening python"

    # ---------- CHROME ----------



    
    elif "open chrome" in query or "open web" in query :

        say("Opening Chrome")

        subprocess.Popen([
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        ])

        response_displayed = "Opening Chrome"

    # ---------- NOTEPAD ---------
    elif "open notepad" in query:

        say("Opening Notepad")

        subprocess.Popen(["notepad.exe"])

        response_displayed = "Opening Notepad"

    # ---------- CALCULATOR ----------

    elif "open calculator" in query:

        say("Opening Calculator")

        subprocess.Popen(["calc.exe"])

        response_displayed = "Opening Calculator"

    # ---------- CMD ----------

    elif "open command prompt" in query or  "open cmd" in query :

        say("Opening Command Prompt")

        subprocess.Popen(["cmd.exe"])

        response_displayed = "Opening Command Prompt"


    #-----------file manager-----------
    elif  "open this pc" in query or "open file explorer"in query or "open files" in query:
        say("opning file explorer sir ")
        subprocess.Popen(["explorer"])
        response_displayed = "Opening file explorer , sir! "            



 #-----------download-----------
    elif  "open downloads" in query or "open download"in query or "check downloads" in query:
        say("opning file explorer sir ")
        subprocess.Popen(["explorer", r"C:\Users\devra\Downloads"])
        response_displayed = "Opening file explorer , sir! "            






    # ---------- SETTINGS ----------

    elif "open settings" in query:

        say("Opening Settings")

        subprocess.Popen(["start", "ms-settings:"], shell=True)

        response_displayed = "Opening Settings"

    # ---------- EXIT ----------

    elif "exit" in query or "stop" in query:

        say("Goodbye sir")

        run = False

    # ---------- UNKNOWN ----------

    else:

        say("I did not understand")

        response_displayed = "Unknown Command"


# =========================================
# VOICE LISTENER
# =========================================

def take_command():
    global assistant_mode
    global response_displayed
    global is_listening
    global activation_time 


    r = sr.Recognizer()

    while run:

        try:

            with sr.Microphone() as source:

                is_listening = True

                response_displayed = "Listening..."

                print("Listening...")

        
                r.adjust_for_ambient_noise(source, duration=1)

                r.energy_threshold = 300

                r.dynamic_energy_threshold = True

                r.pause_threshold = 1

                audio = r.listen(source)




            print("Recognition started")

            query = r.recognize_google(audio, language="en-in")

            print("Recognition complete")
            query = query.lower()

            print("User said:", query)

            response_displayed = f"You said: {query}"

            if assistant_mode == "sleep":

                if "jarvis" in query or "hey jarvis" in query or "javis" in query:

                    say("Yes Sir")

                    response_displayed = "Jarvis Activated"

                    print("Waiting for command...")

                    # SECOND LISTENING
                    with sr.Microphone() as source:

                        r.adjust_for_ambient_noise(source, duration=0.5)

                        r.energy_threshold = 300

                        r.pause_threshold = 1

                        command_audio = r.listen(
                            source,
                            timeout=5,
                            phrase_time_limit=5
                        )

                    print("Command recognition started")

                    command_query = r.recognize_google(
                        command_audio,
                        language="en-in"
                    )

                    print("Command recognition complete")

                    command_query = command_query.lower()

                    print("Command:", command_query)

                    response_displayed = f"Command: {command_query}"

                    process_command(command_query)

                  
                      
        except sr.UnknownValueError:

            response_displayed = "Could not understand..."

        except sr.RequestError:

            response_displayed = "Internet connection issue..."

        except Exception as e:

            print(e)


# =========================================
# THREAD START
# =========================================

voice_thread = threading.Thread(target=take_command)

voice_thread.daemon = True

voice_thread.start()


# =========================================
# STARTUP
# =========================================

say("Hello sir, I am Jarvis AI")


# =========================================
# MAIN LOOP
# =========================================

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False


    # ---------- Background ----------

    screen.fill(black)

    # ---------- Title ----------

    text_screen("JARVIS AI ASSISTANT", cyan, 220, 80)

    # ---------- AI Orb ----------

    pygame.draw.circle(screen, cyan, (450, 350), 90)

    pygame.draw.circle(screen, black, (450, 350), 75)

    # ---------- Listening Text ----------

    if is_listening:

        text_screen("VOICE ACTIVE", cyan, 300, 500)

    # ---------- Response ----------

    text_screen(response_displayed, white, 100, 650)

    pygame.display.update()


pygame.quit()
