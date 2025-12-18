# ⚡ Final Combined Project – Library Management System

This is the **final combined project** for your Python fundamentals roadmap.  
You will bring together **file handling, OOP, error handling, algorithms, and menus** in one real-world style app.

---

## 🧠 Concepts Used

- Classes & objects (OOP)  
- Relationships between classes (Book, Member, Library)  
- JSON file storage (save & load data)  
- Error handling (try/except, invalid input, unavailable resources)  
- Search & filtering (find books, members, borrow records)  
- Menu-based CLI program (loop until user quits)  

---

## 📚 Project: Library Management System

You will build a small system to manage a library.

### 🧩 Core Classes

- **Book**
  - Attributes: id, title, author, year, available_copies, total_copies, etc.
- **Member**
  - Attributes: id, name, borrowed_books, etc.
- **Library**
  - Holds collections of books and members
  - Provides methods to add/search/borrow/return

---

### 🔧 Features

Your system should support at least:

- **Books**
  - Add new books  
  - Remove books  
  - Search books (by title, author, or ID)  

- **Members**
  - Add new members  
  - (Optional) Remove members  
  - Search members by name or ID  

- **Borrow / Return**
  - Borrow a book (decrease available copies)  
  - Return a book (increase available copies)  
  - Prevent borrowing if book is unavailable  

- **Reports**
  - List all books  
  - List available books  
  - (Optional) List borrowed books or books per member  

---

### 💾 Data Storage (JSON)

- Store books and members in **JSON files**  
- On program start: load existing data (if file exists)  
- On changes (add/borrow/return): save updated data back to JSON  

---

### ⚠️ Error Handling

Handle errors such as:

- Invalid book or member ID  
- Trying to borrow a book with no available copies  
- Invalid menu choices  
- Broken or missing JSON file (graceful messages, not crashes)  

---

### 🧭 Menu Interface

Create a **text menu** that runs in a loop:

- Show options:
  - 1) Add book  
  - 2) Add member  
  - 3) Search books  
  - 4) Borrow book  
  - 5) Return book  
  - 6) Reports  
  - 0) Exit  

- Keep running until user chooses to quit.  

This project combines **everything** you’ve learned from Stages 1–11 into one coherent, realistic tool.
