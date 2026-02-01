import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import webbrowser
import datetime
import subprocess
import sys
import shutil
from typing import Optional

class VoiceAssistant:
    """Enhanced voice assistant with improved features and error handling"""
    
    def __init__(self):
        """Initialize the voice assistant"""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        self.recognizer = sr.Recognizer()
        self.is_running = True
        
        # Configure recognizer
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        
        self.app_paths = {
            'chrome': 'chrome',
            'firefox': 'firefox',
            'edge': 'msedge',
            'whatsapp': 'WhatsApp',
            'spotify': 'Spotify',
            'telegram': 'Telegram',
            'discord': 'Discord'
        }
        
        self.websites = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'gmail': 'https://mail.google.com',
            'github': 'https://www.github.com',
            'stackoverflow': 'https://www.stackoverflow.com',
            'wikipedia': 'https://www.wikipedia.com',
            'twitter': 'https://www.twitter.com',
            'facebook': 'https://www.facebook.com'
        }
    
    def speak(self, text: str, show_text: bool = True) -> None:
        """Speak the given text"""
        if show_text:
            print(f"🤖 Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def take_command(self) -> str:
        """Listen to user's voice command and return text"""
        try:
            with sr.Microphone() as source:
                print("\n🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10)
            
            print("🔄 Recognizing...")
            command = self.recognizer.recognize_google(audio)
            print(f"👤 User: {command}")
            return command.lower()
        
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that. Could you please repeat?")
            return ""
        except sr.RequestError as e:
            self.speak(f"Could not request results. Please check your internet connection.")
            print(f"Error: {e}")
            return ""
        except sr.WaitTimeoutError:
            self.speak("I didn't hear anything. Please try again.")
            return ""
        except Exception as e:
            self.speak(f"An error occurred: {str(e)}")
            print(f"Error: {e}")
            return ""
    
    def open_website(self, website: str) -> None:
        """Open a website in the default browser"""
        try:
            if website in self.websites:
                url = self.websites[website]
                webbrowser.open(url)
                self.speak(f"Opening {website}")
            else:
                webbrowser.open(f"https://www.{website}.com")
                self.speak(f"Opening {website}")
        except Exception as e:
            self.speak(f"Could not open {website}. {str(e)}")
            print(f"Error: {e}")
    
    def open_application(self, app_name: str) -> None:
        """Open an application (robust across platforms)."""
        try:
            app = self.app_paths.get(app_name.lower(), app_name)

            if sys.platform == 'win32':
                # Try os.startfile for installed applications; fallback to start command
                try:
                    os.startfile(app)
                except Exception:
                    # Use start via shell which can launch by app name
                    subprocess.Popen(f'start "" "{app}"', shell=True)
            elif sys.platform == 'darwin':  # macOS
                subprocess.Popen(['open', '-a', app])
            else:  # Linux
                # Prefer full path if available in PATH
                exe = shutil.which(app)
                if exe:
                    subprocess.Popen([exe])
                else:
                    # Try launching as provided (may be desktop shortcut name)
                    subprocess.Popen([app])

            self.speak(f"Opening {app_name}")
        except Exception as e:
            self.speak(f"Could not open {app_name}. Make sure it's installed.")
            print(f"Error: {e}")
    
    def search_youtube(self, query: str) -> None:
        """Search and play a video on YouTube"""
        try:
            self.speak(f"Searching for {query} on YouTube")
            pywhatkit.playonyt(query)
        except Exception as e:
            self.speak("Could not search YouTube")
            print(f"Error: {e}")
    
    def search_google(self, query: str) -> None:
        """Search on Google"""
        try:
            self.speak(f"Searching for {query} on Google")
            pywhatkit.search(query)
        except Exception as e:
            self.speak("Could not search Google")
            print(f"Error: {e}")
    
    def tell_time(self) -> None:
        """Tell the current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def tell_date(self) -> None:
        """Tell the current date"""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")
    
    def get_system_info(self) -> None:
        """Get and speak system information"""
        try:
            if sys.platform == 'win32':
                username = os.getenv('USERNAME')
                self.speak(f"You are logged in as {username}")
            else:
                username = os.getenv('USER')
                self.speak(f"You are logged in as {username}")
        except Exception as e:
            print(f"Error: {e}")
    
    def show_help(self) -> None:
        """Show available commands"""
        help_text = """
        🎯 Available Commands:
        - Open [app name] - Opens an application
        - Open [website] - Opens a website
        - Search [query] - Searches Google
        - Play [song/video] - Plays on YouTube
        - What time is it - Tells current time
        - What's the date - Tells current date
        - Help - Shows this message
        - Stop/Exit/Goodbye - Stops the assistant
        """
        print(help_text)
        self.speak("Here are the available commands")
    
    def process_command(self, command: str) -> None:
        """Process the voice command and execute appropriate action"""
        if not command:
            return
        
        # Website commands
        if any(word in command for word in ["open youtube", "youtube"]):
            self.open_website("youtube")
        
        elif any(word in command for word in ["open google", "search google"]):
            self.open_website("google")
        
        elif any(word in command for word in ["open gmail", "gmail"]):
            self.open_website("gmail")
        
        elif any(word in command for word in ["open github", "github"]):
            self.open_website("github")
        
        elif any(word in command for word in ["open wikipedia", "wikipedia"]):
            self.open_website("wikipedia")
        
        # Application commands
        elif any(word in command for word in ["open whatsapp", "whatsapp"]):
            self.open_application("WhatsApp")
        
        elif any(word in command for word in ["open discord", "discord"]):
            self.open_application("Discord")
        
        elif any(word in command for word in ["open spotify", "spotify"]):
            self.open_application("Spotify")
        
        elif any(word in command for word in ["open telegram", "telegram"]):
            self.open_application("Telegram")
        
        elif any(word in command for word in ["open chrome", "chrome"]):
            self.open_application("chrome")
        
        elif any(word in command for word in ["open firefox", "firefox"]):
            self.open_application("firefox")
        
        # YouTube search
        elif "play" in command or "search youtube" in command:
            query = command.replace("play", "").replace("search youtube", "").strip()
            if query:
                self.search_youtube(query)
            else:
                self.speak("What would you like to search?")
        
        # Google search
        elif "search" in command and "youtube" not in command:
            query = command.replace("search", "").strip()
            if query:
                self.search_google(query)
            else:
                self.speak("What would you like to search?")
        
        # Time and date
        elif any(word in command for word in ["time", "what time", "current time"]):
            self.tell_time()
        
        elif any(word in command for word in ["date", "what's the date", "today"]):
            self.tell_date()
        
        # System info
        elif "who am i" in command or "system info" in command:
            self.get_system_info()
        
        # Help
        elif any(word in command for word in ["help", "command", "what can you do"]):
            self.show_help()
        
        # Exit
        elif any(word in command for word in ["stop", "exit", "bye", "goodbye", "quit"]):
            self.speak("Goodbye! Have a great day!")
            self.is_running = False
        
        else:
            self.speak("I'm not sure how to help with that. Say help for available commands.")
    
    def start(self) -> None:
        """Start the voice assistant"""
        print("\n" + "="*50)
        print("🤖 ENHANCED VOICE ASSISTANT STARTED")
        print("="*50)
        self.speak("Welcome! I'm your voice assistant. Say help for available commands.")
        
        while self.is_running:
            command = self.take_command()
            if command:
                self.process_command(command)

def main():
    """Main function"""
    try:
        assistant = VoiceAssistant()
        assistant.start()
    except KeyboardInterrupt:
        print("\n\nAssistant stopped by user.")
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    main()