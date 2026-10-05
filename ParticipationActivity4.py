"""
Program Name: Unicode Decode Error Example
Author: Makaden Eveland
Purpose: Demonstrate how a UnicodeDecodeError can occur and how to
         handle it using a try-except block.
Starter Code: None
Date: 10/04/2026
"""

try:
    data = b"\xff\xfe"
    text = data.decode("utf-8")
    print(text)

except UnicodeDecodeError:
    print("A UnicodeDecodeError occurred while decoding the data.")
