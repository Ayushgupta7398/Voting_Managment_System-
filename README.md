# 🗳️ Voting Management System (Python Project)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey.svg)

A console-based Voting Management System developed using Python,
converted from a C-language implementation while preserving the same
logic, structure, and functionality.

------------------------------------------------------------------------

## 📌 Project Overview

This Python-based Voting Management System provides a role-based voting
environment:

### 🔐 Admin Panel

-   Manage candidates
-   View election results

### 👤 User Panel

-   Allow verified voters to cast votes securely

### ✅ System Ensures

✔ One person can vote only once\
✔ Only valid College IDs are accepted\
✔ Automatic vote counting\
✔ Winner declaration

------------------------------------------------------------------------

## 🚀 Features

### 🔐 Admin Panel

-   Password-protected login
-   Add candidates
-   Delete candidates
-   View live election results
-   Automatic winner calculation

### 👤 User Panel

-   College ID validation (Format: ABC1234567)
-   Duplicate vote prevention
-   Simple and secure voting process

### 🎨 User Interface

-   ANSI color-coded terminal output
-   Clean menu-driven interface
-   Loading animation

------------------------------------------------------------------------

## 🧠 Technologies & Concepts Used

Programming Language: Python 3

Core Concepts: - Classes and Objects - Lists - Functions - String
Manipulation - Conditional Statements & Loops

Standard Libraries: - os - time

------------------------------------------------------------------------

## 🏗️ Data Structures Used

### Candidate Class

``` python
class Candidate:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.votes = 0
```

### Voter Storage

``` python
voted_ids = []
```

------------------------------------------------------------------------

## 🛂 College ID Validation Rules

✔ Exactly 10 characters\
✔ First 3 uppercase letters (A--Z)\
✔ Last 7 digits (0--9)

Example: ABC1234567

------------------------------------------------------------------------

## ▶️ How to Run

Requirements: - Python 3.x installed

Run command:

python voting_management_system.py

------------------------------------------------------------------------

## 🔑 Admin Credentials

Password: ayush123\
(Hardcoded for learning purposes)

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   File handling for permanent vote storage
-   Password hashing
-   Database integration
-   GUI version using Tkinter
-   Result visualization using charts

------------------------------------------------------------------------

## 👨‍💻 Developer

Name: Aayush Gupta\
Degree: B.Tech (CSE)\
University: Invertis University\
Domains: Python \| Embedded Systems \| IoT \| Core Programming

------------------------------------------------------------------------

⭐ If you like this project, don't forget to star the repository!
