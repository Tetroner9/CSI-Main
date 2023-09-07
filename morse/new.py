import random
import time
from playsound import playsound

# Define Morse code dictionaries
morse_code_dict_1 = {
    '.-': 'A',   '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K',  '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U',  '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    ' ': ' '
}
morse_code_dict_2 = {
    '.-': 'Z',   '-...': 'Y', '-.-.': 'X', '-..': 'W', '.': 'V',
    '..-.': 'U', '--.': 'T', '....': 'S', '..': 'R', '.---': 'Q',
    '-.-': 'P',  '.-..': 'O', '--': 'N', '-.': 'M', '---': 'L',
    '.--.': 'K', '--.-': 'J', '.-.': 'I', '...': 'H', '-': 'G',
    '..-': 'F',  '...-': 'E', '.--': 'D', '-..-': 'C', '-.--': 'B',
    '--..': 'A',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    ' ': ' '
}

morse_code_dict_3 = {
    '.-': 'M',   '-...': 'N', '-.-.': 'V', '-..': 'C', '.': 'Z',
    '..-.': 'L', '--.': 'O', '....': 'P', '..': 'Y', '.---': 'E',
    '-.-': 'J',  '.-..': 'U', '--': 'B', '-.': 'Q', '---': 'D',
    '.--.': 'T', '--.-': 'A', '.-.': 'W', '...': 'R', '-': 'S',
    '..-': 'I',  '...-': 'F', '.--': 'G', '-..-': 'X', '-.--': 'H',
    '--..': 'K',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    ' ': ' '
}

# Function to select a random dictionary
def select_random_dictionary():
    random_n = random.randint(1, 100)
    random_num = (random_n%3)+1
    print(f"Dictionary:{random_num}")
    # Generate a random number between 1 and 3
    if random_num == 1:
        return morse_code_dict_1
    elif random_num == 2:
        return morse_code_dict_2
    elif random_num == 3:
        return morse_code_dict_3



# Function to generate a random alphabetical password
#def generate_random_password(length):
    #alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    #return ''.join(random.choice(alphabet) for _ in range(length))
   

# Function to encode text in Morse code
def text_to_morse(text, selected_dict):
    text = text.upper()
    morse_code = []
    for char in text:
        if char == ' ':
            morse_code.append(' ')
        elif char in selected_dict.values():
            for key, value in selected_dict.items():
                if char == value:
                    morse_code.append(key)
                    break
    return ' '.join(morse_code)

# Function to decode Morse code to text
def morse_to_text(morse_code, selected_dict):
    morse_code = morse_code.split(' ')
    text = ''
    for symbol in morse_code:
        if symbol in selected_dict:
            text += selected_dict[symbol]
        else:
            text += ' '
    return text

# Function to play Morse code as audio
def play_morse(message):
    for char in message:
        if char == ".":
            playsound("short.mp3")
            time.sleep(0.3)  # Sleep for 0.3 second (adjust as needed)
        elif char == "-":
            playsound("long.mp3")
            time.sleep(0.3)  # Sleep for 0.3 seconds (adjust as needed)
        elif char == " ":
            time.sleep(1.5) 

while True:
    select_dict = select_random_dictionary()
    password = input("CODE: ")
    morse_code = text_to_morse(password,select_dict)
    print(f"MORSE CODE:{morse_code}")
    i = True
    try:
        while i:
            play_morse(morse_code)
            playsound("stathicc.wav")
            time.sleep(0.5)
    except KeyboardInterrupt:
        i =False
        
    print("CYCLE COMPLETED.")
