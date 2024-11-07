This script implements multiple encoding techniques commonly used in data transformation. Each method transforms a given input string into a different encoded format, which can be useful for tasks such as obfuscation, encoding in URL-safe formats, or cryptographic purposes. Below is a description of each encoding method implemented:

1.Base64 Encoding:
Description: Converts binary data into ASCII characters using the base64 encoding scheme. It is widely used for encoding binary data such as images or file contents in a text format.
Use Case: Used in email systems (MIME encoding), data URL schemes, and when transferring data over protocols that only support text, like HTTP.

2.Hex Encoding:
Description: Converts a string into hexadecimal format. Each character of the string is represented by its hexadecimal equivalent.
Use Case: Often used for debugging and inspecting binary data in a human-readable format. It is also used in various cryptographic algorithms.

3.Binary Encoding:
Description: Converts the input string into its binary form (8-bit representation for each character).
Use Case: Useful for understanding how data is represented in binary form. Often used in low-level programming and debugging.

4.URL Encoding (Percent Encoding):
Description: Converts special characters in a string into their URL-encoded format, which uses percent (%) symbols followed by two hexadecimal digits to represent special characters.
Use Case: Used in web development to safely transmit special characters as part of a URL. Essential when sending data over HTTP where certain characters need to be escaped.

5.ROT13 Encoding:
Description: A simple letter substitution cipher that replaces each letter in the input with the letter 13 positions after it in the alphabet. It is its own inverse, meaning applying ROT13 twice returns the original text.
Use Case: Often used for obfuscating spoilers or sensitive information in online forums. It's a simple method for encoding and decoding text.
Caesar Cipher Encoding (Shift of 3):

6.Description: A classical cipher technique where each letter in the plaintext is shifted by a fixed number (3 in this case). It is one of the earliest and simplest forms of encryption.
Use Case: Commonly used in basic encryption and puzzle solving, particularly for educational purposes.

7.Base32 Encoding:
Description: Similar to Base64, but uses a 32-character alphabet, and is designed to encode binary data into a text format that is easier to read and transcribe by humans.
Use Case: Often used in applications like cryptographic hash-based message authentication codes (HMAC) and one-time password (OTP) systems.

8.Morse Code Encoding:
Description: Translates text into Morse code, where each letter and number is represented by a series of dots (.) and dashes (-). It is the classic encoding scheme used in early telecommunication systems.
Use Case: Primarily used in communication systems, emergency signaling, and sometimes in radio communication.

9.ASCII85 Encoding:
Description: A binary-to-text encoding scheme that is more compact than Base64. It uses a set of 85 printable ASCII characters to represent binary data.
Use Case: Used in PostScript and PDF files for embedding binary data in a text-readable format.
