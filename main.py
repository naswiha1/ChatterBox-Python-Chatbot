import os
import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import time
import random
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="ChatterBox"
)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(100),
    message TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

sender = "User"
message = "Hello"
cursor.execute(
    "INSERT INTO chats(sender, message) VALUES(%s, %s)",
    (sender, message)
)

conn.commit()

window = tk.Tk()
window.geometry("450x600")
window.title("ChatterBox AI")
window.configure(bg="white")

logo_canvas = tk.Canvas(
    window,
    width=450,
    height=600,
    bg="black",
    highlightthickness=0
)

logo_canvas.pack(fill="both", expand=True)

screen = TurtleScreen(logo_canvas)
screen.bgcolor("#EAFF00")
screen.tracer(1, 15)

t = RawTurtle(screen)
t.hideturtle()
t.penup()
t.goto(-120, -80)
t.setheading(0)
t.pendown()
t.color("white")
t.fillcolor("white")
t.pensize(3)
t.begin_fill()

for _ in range(2):
    t.forward(240)
    t.circle(20, 90)
    t.forward(100)
    t.circle(20, 90)

t.end_fill()
t.penup()
t.goto(-60, -80)
t.pendown()
t.goto(-80, -110)
t.goto(-35, -80)
t.penup()
t.color("black")
text = "ChatterBox"
x_start = -105
for i, char in enumerate(text):
    t.goto(x_start + i * 22, -5)
    t.write(
        char,
        font=("consolas", 18, "bold")
    )
    screen.update()
    time.sleep(0.12)
t.goto(-30, -45)
t.dot(8, "black")

t.goto(0, -45)
t.dot(8, "black")

t.goto(30, -45)
t.dot(8, "black")
screen.update()
def ai_response(user_msg):

    msg = user_msg.lower().strip()

    if msg in ["hi", "hello", "hey", "hii", "hiii"]:
        return random.choice([
            "Hey! 👋 I'm ChatterBox. How can I help you?",
            "Hello! 😊 Nice to see you!",
            "Hii! 💬 What are you doing today?",
            "Hey there! ✨ How can I help?"
        ])

    elif "how are you" in msg:
        return random.choice([
            "I'm doing great! 😊 Thanks for asking.",
            "I'm good! Ready to chat with you. 🤖",
            "I'm awesome! How about you? 😄"
        ])

    elif "your name" in msg or "who are you" in msg:
        return random.choice([
            "I'm ChatterBox AI 🤖",
            "My name is ChatterBox! 💬",
            "I'm your little AI chat buddy! 😊"
        ])

    elif "python" in msg:
        return random.choice([
            "Python is a beginner-friendly programming language. 🐍",
            "Python is great for AI, data science and automation! 💻",
            "Keep practicing Python! You'll get better step by step. 🐍✨"
        ])

    elif "programming" in msg or "coding" in msg:
        return random.choice([
            "Coding becomes easier when you practice every day! 💻",
            "Don't worry about errors. Errors are part of learning. 😊",
            "Try breaking a big problem into smaller steps. 🧩"
        ])

    elif "study" in msg or "exam" in msg:
        return random.choice([
            "Make a small study plan and take short breaks. 📚",
            "You can do it! Stay consistent and keep practicing. 💪",
            "Focus on one topic at a time. You've got this! ✨"
        ])

    elif "happy" in msg:
        return random.choice([
            "That's wonderful! Keep that positive energy! 😊✨",
            "I'm happy that you're happy! 🥰",
            "That's great to hear! 💛"
        ])

    elif "sad" in msg or "upset" in msg:
        return random.choice([
            "I'm sorry you're feeling this way. 🫂",
            "It's okay to have difficult days. Take some time for yourself. ❤️",
            "Things can get better. Don't give up! 🌸"
        ])

    elif "thank" in msg or "thanks" in msg:
        return random.choice([
            "You're very welcome! 😊",
            "Anytime! 💛",
            "My pleasure! 🫂",
            "Always happy to help! ✨"
        ])

    elif "love" in msg:
        return random.choice([
            "Love makes life a little more beautiful. ❤️",
            "Aww! That's sweet. 🥰",
            "Love is definitely a special feeling! 💕"
        ])

    elif "food" in msg or "hungry" in msg:
        return random.choice([
            "Now you're making me hungry! 😂🍕",
            "How about some pizza? 🍕",
            "Momos sound like a good idea! 😋"
        ])

    elif "weather" in msg:
        return random.choice([
            "I hope the weather is nice where you are! ☀️",
            "Perfect weather for a relaxing day. 😊",
            "Don't forget to carry an umbrella if it looks rainy! ☔"
        ])

    elif "joke" in msg:
        return random.choice([
            "Why did the computer go to the doctor? Because it had a virus! 😂💻",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why did the Python developer wear glasses? Because he couldn't C! 🤓🐍"
        ])

    elif "good morning" in msg or "gm" in msg:
        return random.choice([
            "Good morning! ☀️ Have a wonderful day!",
            "Good morning! 😊 Ready for a great day?",
            "Morning! 🌸 Don't forget to smile today!"
        ])

    elif "good night" in msg or "gn" in msg:
        return random.choice([
            "Good night! 🌙 Sleep well! 😴",
            "Sweet dreams! ✨🌙",
            "Good night! See you tomorrow! 👋"
        ])

    elif "bye" in msg or "goodbye" in msg:
        return random.choice([
            "Bye bye! 👋 See you soon!",
            "Take care! 😊",
            "See you later! ✨",
            "Goodbye! It was nice chatting with you! 💬"
        ])

    else:
        return random.choice([
            f"Interesting! You said: '{user_msg}' 🤔",
            "Hmm... tell me more about that. 👀",
            "That's interesting! Can you explain a little more? 😊",
            "I understand. Tell me what you're thinking. 💬",
            "That's something worth talking about! ✨",
            "Interesting question! 🤖",
            "I'm still learning, but I'm listening! 👂",
            "Got it! What would you like to know about it?",
            "That's cool! 😄 Tell me more.",
            "Hmm... I need to think about that one! 🤔"
        ])
def open_chat_page():

    logo_canvas.destroy()

    header = tk.Frame(
        window,
        bg="#EAFF00",
        height=60
    )

    header.pack(fill="x")

    title = tk.Label(
        header,
        text="💬 ChatterBox AI",
        font=("Arial", 18, "bold"),
        bg="#EAFF00",
        fg="black"
    )

    title.pack(pady=15)

    chat_area = tk.Text(
        window,
        font=("Arial", 12),
        bg="white",
        state="disabled",
        wrap="word"
    )

    chat_area.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    bottom = tk.Frame(
        window,
        bg="white"
    )

    bottom.pack(
        fill="x",
        padx=10,
        pady=10
    )

    message_box = tk.Entry(
        bottom,
        font=("Arial", 13)
    )

    message_box.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=8
    )

    def send_message(event=None):

        message = message_box.get()

        if message.strip() == "":
            return

        chat_area.config(state="normal")

        chat_area.insert(
            tk.END,
            "You: " + message + "\n"
        )

        cursor.execute(
            "INSERT INTO chats (sender, message) VALUES (%s, %s)",
            ("You", message)
        )

        conn.commit()

        message_box.delete(
            0,
            tk.END
        )

        chat_area.config(state="disabled")

        window.after(
            800,
            generate_reply,
            message
        )
    def generate_reply(message):

        reply = ai_response(message)

        chat_area.config(state="normal")

        chat_area.insert(
            tk.END,
            "AI: " + reply + "\n\n"
        )

        cursor.execute(
            "INSERT INTO chats (sender, message) VALUES (%s, %s)",
            ("AI", reply)
        )

        conn.commit()

        chat_area.config(state="disabled")

        chat_area.see(tk.END)

    send_button = tk.Button(
        bottom,
        text="Send",
        font=("Arial", 11, "bold"),
        bg="#EAFF00",
        command=send_message
    )
    send_button.pack(
        side="right",
        padx=5,
        ipadx=10,
        ipady=5
    )
    message_box.bind(
        "<Return>",
        send_message
    )

    message_box.focus()

window.after(
    2000,
    open_chat_page
)
window.mainloop()