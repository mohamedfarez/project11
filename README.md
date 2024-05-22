# project11
Voice Assistant using Python
by: mohamed fares
This is the main entry point for the voice assistant GUI application. It sets up the Tkinter window, loads the necessary images, and defines the functionality for the start and close buttons.

The `assistance_gui` class is responsible for managing the GUI and the voice assistant functionality. It includes methods for starting the voice assistant, handling voice commands, and closing the application window.

The `start_option` method initializes the speech recognition and text-to-speech engines, and defines the main logic for the voice assistant. It includes functions for greeting the user, taking voice commands, and executing various commands such as opening web pages, checking the current time, and shutting down the application.

The `close_window` method is responsible for destroying the Tkinter window and closing the application.

Project Rrerequisites
To implement a voice assistant in python requires you to have a basic knowledge of the python programming and speech_recognition library.

tkinter – for use Interface(UI)
speech_recognition – to recognize the speech
datetime – to get date and time
pyttsx3 – is a text-to-speech conversion library
webbrowser – is a convenient web browser controller
