# ChatterBox – Interactive Python Chatbot

ChatterBox is a desktop chatbot application built with Python. It provides a graphical chat interface using Tkinter, an animated welcome screen using Turtle Graphics, predefined rule-based conversational responses, and MySQL integration to store chat messages.

## Features

- Interactive desktop interface built with Tkinter
- Animated welcome screen created with Turtle Graphics
- Rule-based responses selected using keyword matching
- Randomized predefined replies
- MySQL database storage for chat messages

## Technologies Used

- Python
- Tkinter
- Turtle Graphics
- MySQL
- `mysql-connector-python`

## Requirements

- Python installed on your computer
- MySQL Server running
- The Python package listed in `requirements.txt`

## Setup and Installation

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Install the required package:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a MySQL database named `ChatterBox` using MySQL Workbench or the MySQL command line:

   ```sql
   CREATE DATABASE ChatterBox;
   ```

5. Open `main.py` and configure the MySQL connection settings for your own computer. Do not publish your database password in a public repository.
6. Run the application:

   ```bash
   python main.py
   ```

## Database

The application creates a `chats` table when it connects to the `ChatterBox` database. The table stores the sender, message, and timestamp.

## How the Chatbot Works

ChatterBox currently uses rule-based logic. It checks user messages for keywords and selects a suitable response from predefined options. It does not currently use machine learning or a generative AI model.

## Future Improvements

- Add a secure configuration method for database credentials
- Display previous chat history when the app opens
- Add more conversational patterns
- Improve error handling and input validation
- Explore integration with a machine-learning or language model

## Author

Created as a Python desktop application project.
