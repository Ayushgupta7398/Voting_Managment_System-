🗳️ Voting Management System (Python Project)

A console-based Voting Management System developed using Python, converted from a C-language implementation while preserving the same logic, structure, and functionality. This project simulates a secure voting process with Admin and User roles, input validation, and real-time result calculation.


---

🔖 Project Badges

    


---

📌 Project Overview

This Python-based Voting Management System provides a role-based voting environment:

Admin Panel – Manage candidates and view election results

User Panel – Allow verified voters to cast votes securely


The system ensures:

✔ One person can vote only once

✔ Only valid College IDs are accepted

✔ Automatic vote counting and winner declaration



---

🚀 Features

🔐 Admin Panel

Password-protected login

Add candidates

Delete candidates

View live election results

Automatic winner calculation


👤 User Panel

College ID validation (Format: ABC1234567)

Duplicate vote prevention

Simple and secure voting process


🎨 User Interface

ANSI color-coded terminal output

Clean menu-driven interface

Loading animation for better user experience



---

🧠 Technologies & Concepts Used

Programming Language: Python 3

Core Concepts:

Classes and Objects

Lists

Functions

String manipulation

Conditional statements & loops


Standard Libraries:

os

time




---

🏗️ Data Structures Used

Candidate Class

class Candidate:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.votes = 0

Voter Storage

voted_ids = []

Prevents duplicate voting

Stores voter IDs securely during runtime



---

🛂 College ID Validation Rules

✔ Exactly 10 characters
✔ First 3 uppercase letters (A–Z)
✔ Last 7 digits (0–9)

Example:

ABC1234567


---

⚙️ How the System Works

1. Program starts with Main Menu


2. User selects:

Admin Panel

User Panel



3. Admin manages candidates


4. User enters College ID


5. System validates ID


6. Vote is cast securely


7. Results are calculated and displayed




---

▶️ How to Run the Program

Requirements

Python 3.x installed


Run Command

python voting_management_system.py

> Works on Linux, macOS, and Windows terminals




---

🔑 Admin Credentials

Password: ayush123

> ⚠️ Hardcoded for learning purposes only




---

🧪 Limitations

No permanent data storage (no files/database)

Hardcoded admin password

Terminal-based application only



---

🔮 Future Enhancements

File handling for permanent vote storage

Password hashing for admin login

Database integration

GUI version using Tkinter

Result visualization using charts



---

📚 Learning Outcomes

Understanding Python OOP concepts

Converting logic from C to Python

Input validation and security basics

Role-based system design

Terminal UI styling with ANSI codes



---

📊 GitHub Stats






---

👨‍💻 Developer Information

Name: Aayush Gupta
Degree: B.Tech (CSE)
University: Invertis University
Domains: Python | Embedded Systems | IoT | Core Programming


---

⭐ Acknowledgement

This project is developed for academic and learning purposes, demonstrating how a real-world voting system can be implemented using Python.


---

📌 License

This project is open-source and free to use for educational purposes.


---

✨ If you like this project, don’t forget to ⭐ star the repository!
