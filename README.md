# 🏧 ATM Simulator

> A fully functional ATM Simulator built with Python.

---

## 📸 Screenshots

### User Interface
![User GUI](Screenshots/User_GUI.png)

### Admin Main Menu
![Admin Main Menu](Screenshots/Admin_Main_Menu.png)

### Admin Casette Menu
![Admin Casette Menu](Screenshots/Admin_Casette_Menu.png)
---

## 📋 Overview

ATM Simulator is a desktop application that replicates the core functionality of a real-world ATM machine. Built with Python and a modular architecture, it separates the UI, business logic, and admin components into clean, maintainable layers.

---

## ✨ Features

- 💳 **Card Reader** — Simulates card insertion and PIN verification
- 🏦 **Account Management** — Balance inquiry, deposits, and withdrawals
- 💵 **Cash Dispensing** — Cassette-based cash handling and dispensing logic
- 📒 **Checkbook Requests** — Request a new checkbook through the ATM
- 🔐 **Admin Panel** — Manage cassettes, unblock cards, and monitor the system
- 🗄️ **SQLite Database** — Lightweight local database for accounts and transactions

---

## 🗂️ Project Structure

```
ATM Simulator/
├── ADMIN/
│   ├── Casette/
│   │   ├── Fill/
│   │   └── casette_gui.py
│   ├── Login/
│   ├── Menu/
│   ├── admin.py
│   ├── exit_button.py
│   └── state.py
├── ATM_GUI/
│   ├── Dispensers/
│   ├── inputOutput/
│   ├── Logic/
│   ├── admin_button.py
│   ├── atm_gui.py
│   └── unblock_cards.py
├── ATM_LOGIC/
│   ├── atm.py
│   ├── bank_account.py
│   ├── card_reader.py
│   ├── card.py
│   ├── casette.py
│   ├── init_db.py
│   ├── main.py
│   └── request_checkbook.py
├── main.py
└── README.md
```

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python | Core language |
| Tkinter | GUI framework |
| SQLite | Local database |

---

## 🙈 .gitignore

The following are excluded from version control:

```
__pycache__/
*.pyc
*.pyo
atm.db
.env
```
