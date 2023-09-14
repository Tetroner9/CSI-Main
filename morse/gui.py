import tkinter as tk
# import tkinter.font as tkFont
import random
import time
from playsound import playsound
from PIL import Image, ImageTk
import threading

# Define Morse code dictionaries
morse_code_dict_1 = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    ' ': ' '
}
morse_code_dict_2 = {
    '.-': 'Z', '-...': 'Y', '-.-.': 'X', '-..': 'W', '.': 'V',
    '..-.': 'U', '--.': 'T', '....': 'S', '..': 'R', '.---': 'Q',
    '-.-': 'P', '.-..': 'O', '--': 'N', '-.': 'M', '---': 'L',
    '.--.': 'K', '--.-': 'J', '.-.': 'I', '...': 'H', '-': 'G',
    '..-': 'F', '...-': 'E', '.--': 'D', '-..-': 'C', '-.--': 'B',
    '--..': 'A',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    ' ': ' '
}

morse_code_dict_3 = {
    '.-': 'M', '-...': 'N', '-.-.': 'V', '-..': 'C', '.': 'Z',
    '..-.': 'L', '--.': 'O', '....': 'P', '..': 'Y', '.---': 'E',
    '-.-': 'J', '.-..': 'U', '--': 'B', '-.': 'Q', '---': 'D',
    '.--.': 'T', '--.-': 'A', '.-.': 'W', '...': 'R', '-': 'S',
    '..-': 'I', '...-': 'F', '.--': 'G', '-..-': 'X', '-.--': 'H',
    '--..': 'K',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    ' ': ' '
}
selected_dict = None
running = True

# Create a global variable to track whether the GIF is playing
gif_playing = False
stop_event = threading.Event()


# Function to start the GIF animation
def start_gif_animation():
    global gif_playing
    gif_playing = True
    animation(count)


# Function to stop the GIF animation
def stop_gif_animation():
    global gif_playing
    gif_playing = False
    gif_canvas.place_forget()


# Function to select a random dictionary
def select_random_dictionary():
    random_n = random.randint(1, 100)
    global random_num
    global selected_dict
    random_num = (random_n % 3) + 1
    print(f"Dictionary: {random_num}")

    # Generate a random number between 1 and 3
    if random_num == 1:
        selected_dict = morse_code_dict_1
    elif random_num == 2:
        selected_dict = morse_code_dict_2
    elif random_num == 3:
        selected_dict = morse_code_dict_3


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


# Function to play Morse code as audio
def play_morse(message):
    while running:  # Continue playing until interrupted
        for char in message:
            if char == ".":
                playsound("short.mp3")
                time.sleep(0.5)
            elif char == "-":
                playsound("long.mp3")
                time.sleep(0.35)
            elif char == " ":
                time.sleep(1.2)
        playsound("stathicc.wav")  # Play the ending sound after Morse code


# Function to handle the "Convert" button click event
def convert_to_morse():
    global running
    running = True  # Reset the running flag
    text = input_text.get()
    select_random_dictionary()
    morse_code = text_to_morse(text, selected_dict)
    print(f"ENCODED MORSE CODE: {morse_code}")

    if selected_dict is None:
        return

    if not text == "Enter Text":
        # Start Morse code playback in a separate thread
        morse_thread = threading.Thread(target=play_morse, args=(morse_code,))
        morse_thread.start()
        start_gif_animation()


# Function to handle the "Stop" button click event
def stop_morse():
    global running
    running = False  # Set the running flag to stop Morse code playback
    stop_event.set()  # Set the stop event to signal the audio thread to stop
    stop_gif_animation()  # Stop the GIF animation and make it invisible
    input_text.delete(0, tk.END)
    input_text.config(fg="white")
    input_text.insert(0, placeholder)
    root.focus_set()


def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


def on_input_click(event):
    input_text.delete(0, tk.END)
    input_text.config(fg="#39FF14")


root = tk.Tk()
file = 'ezgif.com-resize.gif'
info = Image.open(file)
frames = info.n_frames
print(frames)
root.title("Morse Code Converter")
root.state("zoomed")
toggle_fullscreen()
root.bind("<Escape>", toggle_fullscreen)

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load the background image and resize it to match the screen dimensions
bg_image = Image.open("bgnew.jpg")
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas widget to display the background image
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()

# Display the background image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# Create and place input elements directly on the canvas
placeholder = "Enter Text"
input_text = tk.Entry(root, font=("Digital-7", 24), fg="white", bg="black", justify="center", borderwidth=0)
input_text.insert(0, placeholder)
input_text.bind("<FocusIn>", on_input_click)
input_text_window = canvas.create_window(
    1030, 345, anchor=tk.NW, window=input_text, height=50, width=200
)

# Create "Convert" button on the canvas
convert_button = tk.Button(root, text="Convert", command=convert_to_morse, width=8, height=2, font=("Digital-7", 12),
                           fg="#39FF14", bg="#09262e", activebackground="#09262e", justify="center", borderwidth=0,
                           highlightthickness=0, highlightbackground="#09262e")
convert_button_window = canvas.create_window(
    912, 583, anchor=tk.NW, window=convert_button
)

# Create a "Stop" button on the canvas
stop_button = tk.Button(root, text="Stop", command=stop_morse, width=8, height=2, font=("Digital-7", 12), fg="#39FF14",
                        bg="#090e0e", activebackground="#090e0e", borderwidth=0, highlightthickness=0,
                        highlightbackground="#090e0e")
stop_button_window = canvas.create_window(
    1280, 583, anchor=tk.NW, window=stop_button
)

gif_canvas_width = 50
gif_canvas_height = 50

# Create a Canvas widget for the GIF on the background canvas
gif_canvas = tk.Canvas(canvas, width=gif_canvas_width, height=gif_canvas_height, bg='black', highlightthickness=0)
gif_canvas.place(x=1008, y=432)

# GIF
im = [tk.PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
count = 0


def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    if gif_playing:
        root.after(50, animation, count)


gif_label = tk.Label(gif_canvas, image="", borderwidth=0)
gif_label.pack()

root.mainloop()
