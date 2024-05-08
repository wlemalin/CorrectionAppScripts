"""
clipboard_utils.py

This module provides utility functions for interacting with the system clipboard.

Functions:
    - get_clipboard(): Retrieves text content from the system clipboard.
    - copy_to_clipboard(text: str): Copies text content to the system clipboard.
"""

import subprocess

def get_clipboard():
    """
    Retrieve text content from the system clipboard using `xsel`.

    Returns:
        str: The text content retrieved from the clipboard.
    """
    result = subprocess.run(['xsel', '--clipboard', '--output'], stdout=subprocess.PIPE, check=True)
    return result.stdout.decode('utf-8')

def copy_to_clipboard(text: str):
    """
    Copy text content to the system clipboard using `xsel`.

    Args:
        text (str): The text content to be copied to the clipboard.
    """
    with subprocess.Popen(['xsel', '--clipboard', '--input'], stdin=subprocess.PIPE) as process:
        process.communicate(input=text.encode('utf-8'))
