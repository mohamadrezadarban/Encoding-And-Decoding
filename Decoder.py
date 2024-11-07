import base64
import binascii
import urllib.parse
import codecs

def decode_base64(encoded_text):
    try:
        return base64.b64decode(encoded_text).decode()
    except Exception as e:
        return f"Base64 Decoding Failed: {e}"

def decode_hex(encoded_text):
    try:
        return binascii.unhexlify(encoded_text).decode()
    except Exception as e:
        return f"Hex Decoding Failed: {e}"

def decode_binary(encoded_text):
    try:
        clean_binary = encoded_text.replace(" ", "")
        if len(clean_binary) % 8 != 0:
            raise ValueError("Binary string length is not a multiple of 8")
        return ''.join([chr(int(clean_binary[i:i+8], 2)) for i in range(0, len(clean_binary), 8)])
    except Exception as e:
        return f"Binary Decoding Failed: {e}"

def decode_url(encoded_text):
    try:
        return urllib.parse.unquote(encoded_text)
    except Exception as e:
        return f"URL Decoding Failed: {e}"

def decode_rot13(encoded_text):
    try:
        return codecs.decode(encoded_text, 'rot_13')
    except Exception as e:
        return f"ROT13 Decoding Failed: {e}"

def decode_caesar(encoded_text, shift=3):
    try:
        return ''.join(
            chr((ord(char) - 65 - shift) % 26 + 65) if 'A' <= char <= 'Z' else
            chr((ord(char) - 97 - shift) % 26 + 97) if 'a' <= char <= 'z' else char
            for char in encoded_text
        )
    except Exception as e:
        return f"Caesar Cipher Decoding Failed: {e}"

def decode_base32(encoded_text):
    try:
        return base64.b32decode(encoded_text).decode()
    except Exception as e:
        return f"Base32 Decoding Failed: {e}"

def decode_morse(encoded_text):
    try:
        morse_dict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', 
            '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', 
            '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', 
            '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
            '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', 
            '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '
        }
        return ''.join(morse_dict.get(code, '?') for code in encoded_text.split())
    except Exception as e:
        return f"Morse Code Decoding Failed: {e}"

def decode_ascii85(encoded_text):
    if not encoded_text.startswith('<~') and not encoded_text.endswith('~>'):
        encoded_text = f"<~{encoded_text}~>"
    try:
        return base64.a85decode(encoded_text, adobe=True).decode()
    except Exception as e:
        return f"ASCII85 Decoding Failed: {e}"

def decode_methods(encoded_text):
    methods = [
        ("Base64 Decoding", decode_base64),
        ("Hex Decoding", decode_hex),
        ("Binary Decoding", decode_binary),
        ("URL Decoding", decode_url),
        ("ROT13 Decoding", decode_rot13),
        ("Caesar Cipher Decoding", decode_caesar),
        ("Base32 Decoding", decode_base32),
        ("Morse Code Decoding", decode_morse),
        ("ASCII85 Decoding", decode_ascii85)
    ]
    
    for method_name, method_func in methods:
        print(f"\n{method_name}:")
        result = method_func(encoded_text)
        print(result)
        print("-" * 80)

# Example usage:
encoded_input = input("Enter encoded text to attempt decoding with various methods: ")
decode_methods(encoded_input)
