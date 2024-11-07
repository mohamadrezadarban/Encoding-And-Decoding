import base64
import binascii
import urllib.parse
import codecs

def encode_base64(text):
    try:
        return base64.b64encode(text.encode()).decode()
    except Exception as e:
        return f"Base64 Encoding Failed: {e}"

def encode_hex(text):
    try:
        return binascii.hexlify(text.encode()).decode()
    except Exception as e:
        return f"Hex Encoding Failed: {e}"

def encode_binary(text):
    try:
        return ''.join(format(ord(char), '08b') for char in text)
    except Exception as e:
        return f"Binary Encoding Failed: {e}"

def encode_url(text):
    try:
        return urllib.parse.quote(text)
    except Exception as e:
        return f"URL Encoding Failed: {e}"

def encode_rot13(text):
    try:
        return codecs.encode(text, 'rot_13')
    except Exception as e:
        return f"ROT13 Encoding Failed: {e}"

def encode_caesar(text, shift=3):
    try:
        return ''.join(
            chr((ord(char) - 65 + shift) % 26 + 65) if 'A' <= char <= 'Z' else
            chr((ord(char) - 97 + shift) % 26 + 97) if 'a' <= char <= 'z' else char
            for char in text
        )
    except Exception as e:
        return f"Caesar Cipher Encoding Failed: {e}"

def encode_base32(text):
    try:
        return base64.b32encode(text.encode()).decode()
    except Exception as e:
        return f"Base32 Encoding Failed: {e}"

def encode_morse(text):
    try:
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
            '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
        }
        return ' '.join(morse_dict.get(char.upper(), '?') for char in text)
    except Exception as e:
        return f"Morse Code Encoding Failed: {e}"

def encode_ascii85(text):
    try:
        return base64.a85encode(text.encode()).decode()
    except Exception as e:
        return f"ASCII85 Encoding Failed: {e}"

def encode_methods(text):
    methods = [
        ("Base64 Encoding", encode_base64),
        ("Hex Encoding", encode_hex),
        ("Binary Encoding", encode_binary),
        ("URL Encoding", encode_url),
        ("ROT13 Encoding", encode_rot13),
        ("Caesar Cipher Encoding", encode_caesar),
        ("Base32 Encoding", encode_base32),
        ("Morse Code Encoding", encode_morse),
        ("ASCII85 Encoding", encode_ascii85)
    ]
    
    for method_name, method_func in methods:
        print(f"\n{method_name}:")
        result = method_func(text)
        print(result)
        print("-" * 80)

# Example usage:
text_input = input("Enter text to attempt encoding with various methods: ")
encode_methods(text_input)

# ------------------------------
# Developer Information
# ------------------------------
# Script Name: Encoding & Decoding Tool
# Author: Mohammadreza Darban
# GitHub: https://github.com/mohamadrezadarban
# Version: 1.0.0
# Date Created: 2024-11-07
# Description: A Python script to decode strings in various formats like Base64, Hex, URL, and more.
# ------------------------------
# "Coding is like magic, the more you learn, the more powerful you become."
# ------------------------------
# I LOVE YOU ALL
