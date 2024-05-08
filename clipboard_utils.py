"""
clipboard_utils.py

This module provides utility functions for interacting with the system clipboard.

Functions:
    - get_clipboard(): Retrieves text content from the system clipboard.
    - copy_to_clipboard(text: str): Copies text content to the system clipboard.
"""
import sys
import subprocess
import pyperclip

# Detect platform and set clipboard method
platform = sys.platform
if platform == "darwin":
    method = "pyperclip"
elif platform.startswith("linux"):
    method = "xsel"
else:
    method = "unsupported"

# Define platform-specific clipboard functions
def get_clipboard_xsel():
    """
    Retrieve text content from the system clipboard using `xsel`.

    Returns:
        str: The text content retrieved from the clipboard.
    """
    result = subprocess.run(['xsel', '--clipboard', '--output'], stdout=subprocess.PIPE, check=True)
    return result.stdout.decode('utf-8')

def get_clipboard_pyperclip():
    """
    Retrieve text content from the system clipboard using `pyperclip`.

    Returns:
        str: The text content retrieved from the clipboard.
    """
    return pyperclip.paste()



# Define the `copy_to_clipboard` function
def copy_to_clipboard_xsel(text):
    """
    Copy text content to the system clipboard using `xsel`.

    Args:
        text (str): The text content to be copied to the clipboard.
    """
    with subprocess.Popen(['xsel', '--clipboard', '--input'], stdin=subprocess.PIPE) as process:
        process.communicate(input=text.encode('utf-8'))

def copy_to_clipboard_pyperclip(text):
    """
    Copy text content to the system clipboard using `pyperclip`.

    Args:
        text (str): The text content to be copied to the clipboard.
    """
    pyperclip.copy(text)


# Assign platform-specific functions
if method == "xsel":
    get_clipboard = get_clipboard_xsel
    copy_to_clipboard = copy_to_clipboard_xsel
    
elif method == "pyperclip":
    get_clipboard = get_clipboard_pyperclip
    copy_to_clipboard = copy_to_clipboard_pyperclip
    
else:
    def get_clipboard():
        print(f"Error: Clipboard management is not supported for platform: {platform}")
        return None
    def copy_to_clipboard(text):
        print(f"Error: Clipboard management is not supported for platform: {platform}")
        return None