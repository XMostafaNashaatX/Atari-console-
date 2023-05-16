import tkinter as tk
import random

# Create the main window
x5 = tk.Tk()
x5.title("Guess the Flag")
x5.geometry("600x400")


# Set the background image
x5.config(bg="#322e2f")

# Load the flag images
flag_images = []

for i in range(1, 11):
    flag_image = tk.PhotoImage(file=f"flag{i}.png")
    flag_images.append(flag_image)

# Choose a random flag to display
flag = random.choice(flag_images)

# Create a label to display the flag
label = tk.Label(x5, image=flag, bg="#b63780")
label.pack()

# Create a function to check the user's guess
def check_guess():
    guess = guess_entry.get()
    if guess.lower() == flag_answers[flag]:
        result_label.config(text="Correct!", fg="green",bg="pink", font="Helvetica 16 bold")
        x5.config (bg="pink")
    else:
        result_label.config(text="Incorrect. Try again.", fg="red",bg="black", font="Helvetica 16 bold")
        x5.config (bg="black")

# Create an entry widget for the user to enter their guess
guess_entry = tk.Entry(x5, bg="lightgrey", font="Helvetica 16", fg="black")
guess_entry.pack()

# Create a button to check the user's guess
check_button = tk.Button(x5, text="Check", command=check_guess, bg="#e2d810", font="Helvetica 16", fg="black")
check_button.pack()

# Create a label to display the result
result_label = tk.Label(x5, text="", bg="#322e2f", font="Helvetica 16", fg="black")
result_label.pack()

# Create a mapping from flag images to country names
flag_answers = {
    flag_images[0]: "canada",
    flag_images[1]: "china",
    flag_images[2]: "france",
    flag_images[3]: "germany",
    flag_images[4]: "india",
    flag_images[5]: "egypt",
    flag_images[5]: "om el donia",
    flag_images[6]: "japan",
    flag_images[7]: "mexico",
    flag_images[8]: "russia",
    flag_images[9]: "united states",
    flag_images[9]: "usa",
}
# Create a function to reset the game
def reset_game():
    # Choose a new random flag to display
    global flag
    flag = random.choice(flag_images)
    label.config(image=flag)
    # Clear the entry widget and the result label
    guess_entry.delete(0, tk.END)
    result_label.config(text="")
    x5.config (bg="#322e2f")

# Create a button to reset the game
reset_button = tk.Button(x5, text="Reset", command=reset_game, bg="#e2d810", font="Helvetica 16", fg="black")
reset_button.pack()

# Run the main loop
x5.mainloop()
