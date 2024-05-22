"""
This module contains unit tests for the `assistance_gui` class in the `main` module.

The `TestAssistanceGUI` class inherits from `unittest.TestCase` and provides several test methods to verify the behavior of the `assistance_gui` class:

- `test_start_option`: Tests the `start_option` method by mocking the `sr.Recognizer` and `pyttsx3.init` functions, and verifying that the appropriate methods are called on the mocked objects.
- `test_take_command`: Tests the `take_command` method by mocking the `sr.Recognizer`, `sr.Microphone`, and `pyttsx3.init` functions, and verifying that the appropriate methods are called on the mocked objects and that the returned instruction matches the expected value.
- `test_run_command`: Tests the `run_command` method by mocking the `sr.Recognizer`, `pyttsx3.init`, and `webbrowser.open` functions, and verifying that the appropriate methods are called on the mocked objects and that the returned result is `True`.
- `test_close_window`: Tests the `close_window` method by verifying that the `Tk` root window is destroyed.
"""
import unittest
from unittest.mock import patch, MagicMock
import main

class TestAssistanceGUI(unittest.TestCase):
    def setUp(self):
        self.root = main.Tk()
        self.obj = main.assistance_gui(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('main.sr.Recognizer')
    @patch('main.pyttsx3.init')
    def test_start_option(self, mock_pyttsx3, mock_recognizer):
        mock_engine = MagicMock()
        mock_pyttsx3.return_value = mock_engine
        mock_listener = MagicMock()
        mock_recognizer.return_value = mock_listener

        self.obj.start_option()

        mock_pyttsx3.assert_called_once()
        mock_recognizer.assert_called_once()
        mock_engine.say.assert_called()
        mock_engine.runAndWait.assert_called()

    @patch('main.sr.Recognizer')
    @patch('main.pyttsx3.init')
    def test_take_command(self, mock_pyttsx3, mock_recognizer):
        mock_engine = MagicMock()
        mock_pyttsx3.return_value = mock_engine
        mock_listener = MagicMock()
        mock_recognizer.return_value = mock_listener

        with patch('main.sr.Microphone') as mock_microphone:
            mock_microphone.return_value.__enter__ = lambda x: mock_microphone
            mock_microphone.return_value.__exit__ = lambda x, y, z, a: None
            mock_listener.listen.return_value = 'test audio'
            mock_listener.recognize_google.return_value = 'test command'

            instruction = self.obj.take_command()

            self.assertEqual(instruction, 'test command')
            mock_listener.listen.assert_called_once_with(mock_microphone)
            mock_listener.recognize_google.assert_called_once_with('test audio')

    @patch('main.webbrowser.open')
    @patch('main.sr.Recognizer')
    @patch('main.pyttsx3.init')
    def test_run_command(self, mock_pyttsx3, mock_recognizer, mock_webbrowser):
        mock_engine = MagicMock()
        mock_pyttsx3.return_value = mock_engine
        mock_listener = MagicMock()
        mock_recognizer.return_value = mock_listener

        mock_listener.recognize_google.return_value = 'open google'
        self.obj.take_command = MagicMock(return_value='open google')

        result = self.obj.run_command()

        self.assertTrue(result)
        mock_engine.say.assert_called_once_with('Opening Google')
        mock_webbrowser.open.assert_called_once_with('google.com')

    def test_close_window(self):
        self.obj.close_window()
        self.assertFalse(self.root.winfo_exists())

if __name__ == '__main__':
    unittest.main()
