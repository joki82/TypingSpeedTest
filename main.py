import random
from tkinter import *


class TypeWriter(Tk):
    """Create main window, words list,  variables to count correctly and incorrectly typed words.
    Call method create_widgets"""

    def __init__(self):
        super().__init__()
        self.font = ("American Typewriter", 24)
        self.title("Typing speed test")
        self.config(bg="#DDEFEF")
        self.minsize(width=400, height=300)
        self.correct = 0
        self.mistyped = 0
        self.word_list = []

        self.create_word_list()
        self.create_widgets()

        self.mainloop()

    def create_word_list(self):
        """Create word list from txt file containing 1000 words, each in new line"""
        with open("words.txt") as file:
            content = file.readlines()
            for line in content:
                new_word = line.replace("\n", "")
                self.word_list.append(new_word)

    def create_widgets(self):
        """Create widgets and place in window using pack."""
        # Labels
        self.label_start = Label(text="TEST YOUR TYPING SPEED")
        self.label_start.config(fg="#000000", bg="#DDEFEF", font=self.font)
        self.label_start.pack(pady=10)
        self.label_time = Label(text="IN 60s")
        self.label_time.config(fg="#000000", bg="#DDEFEF", font=self.font)
        self.label_time.pack(pady=10)
        self.label_word = Label(text="Type word followed by ENTER")
        self.label_word.config(fg="#FF0000", bg="#DDEFEF", font=("Andale Mono", 20))
        self.label_word.pack(pady=10)
        # Entry
        self.user_entry = Entry(width=20)
        self.user_entry.config(fg="#000000", bg="#DDEFEF", background="#FFFFFF", font=self.font,
                               insertbackground="#000000")
        self.user_entry.bind('<Return>', self.user_typed)
        self.user_entry.pack()
        # Buttons
        self.start_button = Button(text="Start", command=self.button_pressed, highlightbackground="#DDEFEF",
                                   font=self.font)
        self.start_button.pack(side=LEFT, expand=True, anchor=N, pady=15, ipadx=2, ipady=2)
        self.cancel_button = Button(text="Cancel", command=self.cancel, bg="#DDEFEF", highlightbackground="#DDEFEF",
                                    font=self.font)
        self.cancel_button.pack(side=LEFT, expand=True, anchor=N, pady=15, ipadx=2, ipady=2)

    def random_word(self):
        """Random number in range 0-1000, used for pickup random word on a word list"""
        self.i = random.randint(0, 1001)

    def user_typed(self, event=None):
        """Get word typed by user, convert characters in lower.
        Check if user typed word is correct and increase correct counter for 1, otherwise increase mistyped."""
        typed_by_user = self.user_entry.get().lower()
        print(typed_by_user)
        if typed_by_user == self.word_list[self.i]:
            self.correct += 1
        else:
            self.mistyped += 1
        # Empty entry box, get another random word and display it
        self.user_entry.delete(0, END)
        self.random_word()
        self.label_word.config(text=self.word_list[self.i])

    def button_pressed(self):
        """Start button pressed triggers start method and disables the button."""
        self.start(seconds=3)
        self.start_button.config(state="disabled")

    # 321 Go!
    def start(self, seconds):
        """Count down 3 sec and triggers timer method (that counts 60sec) and gives focus to entry box"""
        if seconds > 0:
            self.after(1000, self.start, seconds - 1)
            self.label_start.config(text=f"{seconds}")
            self.label_time.config(text="")
            self.label_word.config(text="")
            self.user_entry.delete(0, END)
            self.correct = 0
            self.mistyped = 0
        else:
            self.label_start.config(text="COUNTDOWN:")
            self.random_word()
            self.label_word.config(text=self.word_list[self.i], fg="#FF0000", bg="#DDEFEF", font=("Andale Mono", 30))
            self.timer(60)
            self.user_entry.focus()

    def timer(self, seconds):
        """Timer counting down 60 seconds"""
        if seconds > 0:
            self.after(1000, self.timer, seconds - 1)
            self.label_time.config(text=f"{seconds}")

        # When count down finished removes focus and empties entry box, finally displays result and enables Start button
        else:
            self.focus()
            self.user_entry.delete(0, END)
            self.label_start.config(text=f"You typed {self.correct} words in a minute")
            self.label_time.config(text="+")
            self.label_word.config(text=f"{self.mistyped} with a typo.", fg="#000000", font=self.font)
            self.start_button.config(state="normal")

    def cancel(self):
        """Closes main window"""
        self.destroy()


# Running app
if __name__ == '__main__':
    TypeWriter()
