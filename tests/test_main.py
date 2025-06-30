import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)  # noqa: E402

import main
from unittest import mock
from pynput.keyboard import KeyCode


def test_toggle_spamming():
    main.spamming = False
    main.on_press(KeyCode(char='`'))
    assert main.spamming is True
    main.on_press(KeyCode(char='`'))
    assert main.spamming is False


def test_bow_spam_loop_spamming_true():
    main.spamming = True
    with mock.patch('pyautogui.mouseDown') as md, \
         mock.patch('pyautogui.mouseUp') as mu, \
         mock.patch('time.sleep'):
        main.bow_spam_loop(iterations=3)
        assert md.call_count == 3
        assert mu.call_count == 3


def test_bow_spam_loop_spamming_false():
    main.spamming = False
    with mock.patch('time.sleep') as ts:
        main.bow_spam_loop(iterations=2)
        ts.assert_called_with(0.1)
