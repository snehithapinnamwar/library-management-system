# Library Management System

A simple command-line library management system built in Python. It uses plain text files for storage — no database setup required.

## Features
- Add, view, search, update, and delete books
- Add students
- Issue books to students (tracks stock automatically)
- Return books, with automatic fine calculation for late returns
- Simple admin login

## Files
- `library_manage.py` — main program
- `books.txt` — book records (`id,name,author,quantity`)
- `students.txt` — student records (`id,name`)
- `issued_books.txt` — issue records (`book_id,student_id,issue_date`)

## Getting Started

### Requirements
- Python 3

### Run it
```bash
python library_manage.py
```

Login with:
- Username: `admin`
- Password: `1`

Then pick an option from the menu to manage books, students, and issued books.

## How it works
Each entity (books, students, issued records) is stored as comma-separated lines in its own `.txt` file, read and rewritten on each operation — so no external database is needed.

## Possible Improvements
- Move from `.txt` files to a proper database (e.g. SQLite)
- Add input validation
- Add a GUI or web interface
