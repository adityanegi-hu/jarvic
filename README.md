# 🤖 Enhanced Voice Assistant

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/enhanced-voice-assistant?style=social)](https://github.com/yourusername/enhanced-voice-assistant)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/enhanced-voice-assistant?style=social)](https://github.com/yourusername/enhanced-voice-assistant)

A powerful, intelligent voice-controlled assistant built with Python. Control your computer, search the web, launch applications, and much more—all hands-free using natural voice commands.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Commands](#-available-commands) • [Contributing](#-contributing)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Available Commands](#-available-commands)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Overview

**Enhanced Voice Assistant** is a sophisticated voice-controlled desktop application that transforms your computer into an intelligent assistant. Powered by Google's Speech Recognition API and Python's text-to-speech engine, it allows you to interact with your computer entirely through voice commands.

Whether you want to open applications, search the web, play videos, check the time, or perform system operations—simply speak, and the assistant will handle it.

### Why Choose This?

✅ **Easy to Use** - Natural voice commands  
✅ **Highly Customizable** - Add your own commands and applications  
✅ **Cross-Platform** - Windows, macOS, and Linux support  
✅ **Open Source** - MIT licensed, community-driven  
✅ **Well-Documented** - Comprehensive guides and examples  
✅ **Production-Ready** - Robust error handling and edge case management  

---

## ✨ Features

### Core Functionality
- 🎤 **Voice Recognition** - Google Speech-to-Text API integration
- 🔊 **Text-to-Speech** - Natural voice responses with adjustable speech rate
- 🌐 **Web Browsing** - Open websites and search engines seamlessly
- 🎵 **YouTube Integration** - Search and play videos on YouTube
- 📱 **Application Control** - Launch installed desktop applications
- ⏰ **Time & Date** - Get current time and date information
- 🔍 **Web Search** - Search Google directly via voice
- 💬 **Ambient Noise Filtering** - Automatically adjusts to background noise
- ❌ **Error Handling** - Comprehensive error management with user-friendly messages
- 📚 **Help System** - Built-in command reference

### Supported Integrations
- YouTube (search and play)
- Google Search
- Browser automation (Chrome, Firefox, Edge)
- Messaging apps (WhatsApp, Telegram, Discord)
- Music apps (Spotify)
- Gmail and web mail
- Wikipedia, GitHub, and more...

---

## 📋 Requirements

- **Python 3.7+**
- **Microphone** (for voice input)
- **Speakers** (for voice output)
- **Internet Connection** (for API calls and web browsing)
- **Operating System**: Windows, macOS, or Linux

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/enhanced-voice-assistant.git
cd enhanced-voice-assistant
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Platform-Specific Setup

#### 🪟 Windows
```bash
# Using pipwin (recommended)
pip install pipwin
pipwin install pyaudio

# Alternative: Download wheel from
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Then: pip install path/to/pyaudio.whl
```

#### 🍎 macOS
```bash
# Install PortAudio
brew install portaudio

# Install PyAudio
pip install pyaudio
```

#### 🐧 Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3-dev portaudio19-dev

# Install PyAudio
pip install pyaudio
```

### Step 5: Verify Installation

```bash
python -c "import speech_recognition; import pyttsx3; print('✓ All dependencies installed successfully!')"
```

---

## 🎯 Quick Start

Run the voice assistant:

```bash
python enhanced_voice_assistant.py
```

You should see:
```
==================================================
🤖 ENHANCED VOICE ASSISTANT STARTED
==================================================
🤖 Assistant: Welcome! I'm your voice assistant. Say help for available commands.
🎤 Listening...
```

Now simply speak a command! Try:
- "What time is it?"
- "Open YouTube"
- "Search Python tutorials"
- "Open Discord"

---

## 📢 Available Commands

### 🌐 Website Commands

| Command | Action |
|---------|--------|
| `Open YouTube` | Opens YouTube in default browser |
| `Open Google` | Opens Google search |
| `Open Gmail` | Opens Gmail |
| `Open GitHub` | Opens GitHub |
| `Open Wikipedia` | Opens Wikipedia |
| `Open Twitter` | Opens Twitter |
| `Open Facebook` | Opens Facebook |

### 📱 Application Commands

| Command | Action |
|---------|--------|
| `Open WhatsApp` | Launches WhatsApp |
| `Open Discord` | Launches Discord |
| `Open Spotify` | Launches Spotify |
| `Open Telegram` | Launches Telegram |
| `Open Chrome` | Launches Chrome browser |
| `Open Firefox` | Launches Firefox browser |
| `Open Edge` | Launches Edge browser |

### 🔍 Search & Media Commands

| Command | Action |
|---------|--------|
| `Search [query]` | Searches Google |
| `Play [song/video]` | Searches and plays on YouTube |
| `Search YouTube [query]` | Searches YouTube specifically |

### ⏰ Information Commands

| Command | Action |
|---------|--------|
| `What time is it?` | Tells current time |
| `What's the date?` | Tells current date |
| `Today` | Tells current date |
| `Who am I?` | Shows system information |

### ℹ️ Control Commands

| Command | Action |
|---------|--------|
| `Help` | Shows all available commands |
| `Stop` / `Exit` / `Goodbye` | Stops the assistant |
| `Quit` | Stops the assistant |

### 💡 Example Command Sequences

```
"Play Never Gonna Give You Up"
→ Opens YouTube and plays Rick Astley

"Search machine learning tutorials"
→ Searches Google for machine learning tutorials

"What time is it?"
→ Tells you the current time

"Open Discord and search Python"
→ Opens Discord, then searches Google for Python
```

---

## ⚙️ Configuration

### Customize Speech Rate

Edit the `__init__` method in `VoiceAssistant` class:

```python
# 170 is default (words per minute), adjust 50-300 for slower/faster
self.engine.setProperty('rate', 170)
```

### Add Custom Applications

Add to the `app_paths` dictionary:

```python
self.app_paths = {
    'myapp': 'C:\\Program Files\\MyApp\\myapp.exe',  # Windows
    'myapp': '/Applications/MyApp.app',  # macOS
    'myapp': '/usr/bin/myapp',  # Linux
}
```

### Add Custom Websites

Add to the `websites` dictionary:

```python
self.websites = {
    'mysite': 'https://www.example.com',
    'docs': 'https://docs.example.com',
}
```

### Adjust Microphone Sensitivity

```python
# Lower = more sensitive (catches more), Higher = less sensitive
self.recognizer.energy_threshold = 4000
```

### Enable/Disable Ambient Noise Detection

```python
# In take_command() method
self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
```

---

## 🏗️ Architecture

### Project Structure

```
enhanced-voice-assistant/
├── enhanced_voice_assistant.py    # Main application
├── requirements.txt                # Dependencies
├── README.md                        # Documentation
├── LICENSE                          # MIT License
└── .gitignore                       # Git ignore file
```

### Class Design

```
VoiceAssistant
├── __init__()                    # Initialize settings
├── speak()                       # Text-to-speech
├── take_command()                # Voice recognition
├── process_command()             # Command dispatcher
├── open_website()                # Website launcher
├── open_application()            # App launcher
├── search_youtube()              # YouTube search
├── search_google()               # Google search
├── tell_time()                   # Time information
├── tell_date()                   # Date information
├── get_system_info()             # System information
├── show_help()                   # Help menu
└── start()                       # Main loop
```

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### ❌ "No module named 'pyaudio'"

**Solution:**
```bash
# Windows (using pipwin)
pip install pipwin
pipwin install pyaudio

# macOS
brew install portaudio
pip install pyaudio

# Linux
sudo apt-get install python3-dev portaudio19-dev
pip install pyaudio
```

---

#### ❌ "Could not request results"

**Causes & Solutions:**
- Check internet connection: `ping google.com`
- Verify API access isn't blocked by firewall
- Try using a VPN if API is region-restricted

```bash
# Test internet connectivity
python -c "import urllib.request; urllib.request.urlopen('https://google.com'); print('✓ Connected')"
```

---

#### ❌ "I didn't hear anything"

**Solutions:**
- Increase microphone volume on your system
- Reduce background noise
- Adjust energy threshold (lower value = more sensitive):
  ```python
  self.recognizer.energy_threshold = 3000  # Lower value
  ```
- Speak louder and clearer
- Check microphone is properly connected

---

#### ❌ Application won't open

**Solutions:**
- Verify application is installed on your system
- Check the exact application name matches installation:
  ```bash
  # Windows: Check Program Files
  # macOS: Check Applications folder
  # Linux: which app_name
  ```
- Add full path to `app_paths`:
  ```python
  self.app_paths['myapp'] = '/full/path/to/application'
  ```

---

#### ❌ "Sorry, I didn't understand that"

**Solutions:**
- Speak more clearly and at normal pace
- Minimize background noise
- Increase microphone volume
- Reduce echo (use directional microphone if possible)

---

#### ❌ Speech Recognition Timeout

**Solution:**
```python
# In take_command() method, adjust timeout
audio = self.recognizer.listen(source, timeout=15)  # Increase from 10
```

---

## 🔒 Security & Privacy

- Voice data is sent to Google's Speech-to-Text API
- No data is stored locally by default
- Consider running on a local network only if privacy is critical
- For offline speech recognition, consider alternatives like PocketSphinx

---

## 📊 Performance Tips

1. **Use a USB microphone** for better voice recognition
2. **Minimize background noise** for faster recognition
3. **Use a wired internet connection** for faster API responses
4. **Close unnecessary applications** to free up system resources
5. **Update Python** to the latest stable version for better performance

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Report Bugs

Found a bug? Please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Your system information (OS, Python version)
- Error messages or logs

### Suggest Features

Have an idea? Open an issue with the `[FEATURE]` tag:
- Clear description of the feature
- Use cases and benefits
- Possible implementation approach

### Submit Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/enhanced-voice-assistant.git
   cd enhanced-voice-assistant
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Include type hints where applicable

4. **Commit with clear messages**
   ```bash
   git commit -m "Add: amazing feature that does X"
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Clear title and description
   - Link related issues
   - Include any relevant screenshots

### Code Style

```python
# Use type hints
def open_website(self, website: str) -> None:
    """Open a website in the default browser"""
    pass

# Use docstrings
def take_command(self) -> str:
    """
    Listen to user's voice command and return text.
    
    Returns:
        str: The recognized command in lowercase
    """
    pass

# Follow PEP 8
# - 4 spaces for indentation
# - Max 79 characters per line
# - 2 blank lines between class/function definitions
```

---

## 📈 Roadmap

### Upcoming Features

- [ ] **Email Support** - Send emails via voice command
- [ ] **Weather Updates** - Get weather information
- [ ] **News Briefing** - Daily news updates
- [ ] **Reminders & Alarms** - Set reminders and alarms
- [ ] **Smart Home Integration** - Control IoT devices
- [ ] **Machine Learning** - Context-aware responses
- [ ] **Offline Mode** - Work without internet
- [ ] **GUI Interface** - Visual interface option
- [ ] **Plugin System** - Load custom modules
- [ ] **Cloud Sync** - Save preferences to cloud

---

## 📚 Resources

- [Python Documentation](https://docs.python.org/)
- [SpeechRecognition Library](https://github.com/Uberi/speech_recognition)
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
- [PyWhatKit Documentation](https://github.com/Ananto30/pywhatkit)
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)

---

## 🙏 Acknowledgments

- **SpeechRecognition** - Jarvis Lea and contributors
- **pyttsx3** - Nateshmbhat and contributors
- **PyWhatKit** - Ananto30 and contributors
- **Community** - All contributors and bug reporters

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name/Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Support

Having issues? Here are some ways to get help:

1. **Check Documentation** - Read the [README.md](README.md)
2. **Search Issues** - Check [GitHub Issues](https://github.com/yourusername/enhanced-voice-assistant/issues)
3. **Create New Issue** - Describe your problem in detail
4. **Email** - yourname@example.com
5. **Discussions** - GitHub Discussions tab

---

## 🌟 Show Your Support

If you find this project helpful, please:
- ⭐ **Star the repository** on GitHub
- 🍴 **Fork the repository** for your own use
- 📢 **Share with friends** who might benefit
- 💬 **Leave feedback** on what you like or what could improve

---

<div align="center">

**Made with ❤️ by [Your Name]**

[⬆ Back to Top](#-enhanced-voice-assistant)

</div>
