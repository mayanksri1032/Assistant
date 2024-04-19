import pyttsx3  # Text-to-Speech library
import speech_recognition as sr  # Speech recognition library
import webbrowser  # Web browser control
import datetime  # Date and time functions
import os  # Operating system functions

class Ana:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize text-to-speech engine
        self.recognizer = sr.Recognizer()  # Initialize speech recognizer
        self.microphone = sr.Microphone()  # Initialize microphone
        self.stop_command = False  # Flag to stop the assistant

    def say(self, text):
        """Function to speak the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Function to listen to the user's voice command."""
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            command = self.recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you repeat?")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")
            return ""

    def open_website(self, website):
        """Function to open a website in the default web browser."""
        webbrowser.open(website)

    def close_browser_tabs(self):
        """Function to close all browser tabs."""
        os.system("taskkill /im chrome.exe /f")  # Change 'chrome.exe' to your browser's process name

    def open_application(self, application_name):
        """Function to open an application."""
        # Replace 'path_to_application' with the actual path to the application
        # You can also use the application name directly if it's in the system PATH
        os.system(f'start "" "{application_name}"')

    def welcome_message(self):
        """Function to generate a welcome message based on the current time."""
        current_time = datetime.datetime.now()
        if 5 <= current_time.hour < 12:
            return "Good morning! Welcome back."
        elif 12 <= current_time.hour < 18:
            return "Good afternoon! Welcome back."
        else:
            return "Good evening! Welcome back."

    def run(self):
        """Function to run the personal assistant."""
        self.say("Hello! I'm Ana, your personal assistant.")
        self.say("How can I assist you today?")

        while not self.stop_command:
            command = self.listen()

            if "open" in command and "website" in command:
                website = input("Which website would you like to open? ")
                self.open_website(website)
            elif "close" in command and "tabs" in command:
                self.close_browser_tabs()
                self.say("All browser tabs have been closed.")
            elif "remind" in command:
                pass
            elif "weather" in command:
                pass
            elif "play" in command and "music" in command:
                pass
            elif "search" in command:
                query = command.replace("search for", "").strip()
                search_url = f"https://www.google.com/search?q={query}"
                self.open_website(search_url)
            elif "open" in command and "application" in command:
                application_name = input("Which application would you like to open? ")
                self.open_application(application_name)
            elif "stop" in command or "exit" in command:
                self.say("Goodbye!")
                self.stop_command = True
            else:
                self.say("Sorry, I couldn't understand that command. Can you repeat?")

if __name__ == "__main__":
    assistant = Ana()
    assistant.run()
