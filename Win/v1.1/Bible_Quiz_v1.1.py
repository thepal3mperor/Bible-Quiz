import random
import tkinter as tk
from tkinter import messagebox

# Bible questions and answers
bible_questions = {
    "Who built the ark?": "Noah",
    "Who was swallowed by a big fish?": "Jonah",
    "Who was the first man in the Bible?": "Adam",
    "Who killed Goliath?": "David",
    "Who was the mother of Jesus?": "Mary"
}

def show_splash_screen(text):
    splash_screen = tk.Toplevel()
    splash_screen.title("St Austin's Bible Quiz")
    splash_screen.geometry("1920x1080")
    splash_screen.resizable(False, False)

    label = tk.Label(splash_screen, text=text, font=("Arial", 16), justify="center")
    label.pack(pady=100)

    splash_screen.after(5000, splash_screen.destroy)  # Close the splash screen after 5 seconds

def check_answer(answer, entry, window):
        user_answer = entry.get()
        if user_answer.lower() == answer.lower():
            messagebox.showinfo("Correct!", "Great job! You answered correctly.")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {answer}.")
        window.destroy()
        ask_question()  # Ask the next question

def ask_question():
    question = random.choice(list(bible_questions.keys()))
    answer = bible_questions[question]

    window = tk.Toplevel()
    window.title("St Austin's Bible Quiz")
    window.geometry("1920x1080")
    window.resizable(True, True)

    question_label = tk.Label(window, text=question, wraplength=250, justify="center", font=("Arial", 14))
    question_label.pack(pady=20)

    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(pady=10)
    
    def submit_answer(event):
         check_answer(answer, entry, window)

    entry.bind("<Return>", submit_answer)

    submit_button = tk.Button(window, text="Submit", command=lambda: check_answer(answer, entry, window), font=("Arial", 12))
    submit_button.pack(pady=10)

# Main program
def play_quiz():
    main_window = tk.Tk()
    main_window.title("Bible Quiz")
    main_window.geometry("400x300")
    main_window.resizable(True, True)

    show_splash_screen("Welcome to St Austin's Bible Quiz")

    title_label = tk.Label(main_window, text="Let's Play", font=("Arial", 16))
    title_label.pack(pady=30)

    play_button = tk.Button(main_window, text="Play", command=ask_question, font=("Arial", 14))
    play_button.pack(pady=10)

    quit_button = tk.Button(main_window, text="Quit", command=show_quit_splash_screen, font=("Arial", 14))
    quit_button.pack(pady=10)

    main_window.mainloop()

def show_quit_splash_screen():
    quit_splash_screen = tk.Toplevel()
    quit_splash_screen.title("Bible Quiz")
    quit_splash_screen.geometry("1920x1080")
    quit_splash_screen.resizable(False, False)

    label = tk.Label(quit_splash_screen, text="Thanks for playing.\nThis program was developed by namodrew7@gmail.com", font=("Arial", 14), justify="center")
    label.pack(pady=100)

    quit_splash_screen.after(5000, quit_splash_screen.quit)  # Close the splash screen after 5 seconds

play_quiz()
