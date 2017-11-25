#!/usr/bin/python3
#encryptdecrypt.py

# Takes the input_text and encrypts it, returning the result
def encryptText(input_text, key):

    input_text = input_text.upper()
    result = " "
    
    for letter in input_text:
        # Ascii Uppercase 65-90 Lowercase 97-122 (Full range 32-126)
        ascii_value = ord(letter)
        
        # Exclude non-characters from encryption
        if (ord("A") > ascii_value) or (ascii_value > ord("Z")):
            result += letter
        else:
            # Apply encryption key
            key_val = ascii_value + key

            # Ensure we use A-Z regardless of key
            if not ((ord("A")) < key_val < ord("Z")):
                # check to see if the letter we are looking at is not between A and Z
                key_val = ord("A") + (key_val - ord("A")) % (ord("Z") - ord("A")+1)
            # Add the encoded letter to the result string
            result += str(chr(key_val))

            return result

# we can reuse this script in other scripts as keypassing.py
if __name__ == "__main__":

    print("Please enter text to scramble:")
    # get user input
    try:
        user_input = input()
        scrambled_result = encryptText(user_input, 10)
        print("Result: " + scrambled_result)
        print("To unscramble, press enter again")
        input()
        unscrambled_result = encryptText(scrambled_result, -10)
        print("Result: " + unscrambled_result)
    except UnicodeDecodeError:
        print("Sorry.. only ASCII characters are supported! :(")
main()


