
# 💳 ATM System

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Language-Python-blue?logo=python"></a>
  <a href="https://www.arduino.cc/"><img src="https://img.shields.io/badge/Integration-Arduino-00979D?logo=arduino"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <img src="https://img.shields.io/badge/Status-Prototype-orange">
</p>

---

## 📖 Overview

This project is a **Python-based ATM system** integrated with **Arduino hardware** for simulating a real-world ATM interface.  
It allows users to perform essential banking operations such as **balance inquiry, deposit, and withdrawal**, while ensuring secure **PIN-based authentication**.  

The system is **lightweight and modular**, making it ideal for demonstrations, prototyping, and learning purposes.

---

## 🛠 Features

- **Secure Login** – PIN-protected user authentication  
- **Balance Inquiry** – Check account balance quickly  
- **Deposit & Withdrawal** – Perform simulated transactions  
- **Hardware Integration** – Arduino-based keypad and optional LCD display for a more ATM-like interface  
- **Transaction Logging** – Store actions for tracking and debugging  

---

## 🧰 Tech Stack

- **Programming:** Python (core logic), Arduino (I/O handling)
- **Hardware:** Arduino Uno (keypad & I/O), optional LCD display for user interaction  
- **Data Storage:** Local file/database for balance and transaction history  
- **Extras:** Keypad interface & Serial communication for Python-Arduino integration  

---

## 🗂 Project Structure

```

ATM-System/
│
├── main.py                # Main ATM logic (Python)
├── arduino/               # Arduino integration code
│   └── atm\_input.ino      # Handles keypad & serial communication
├── data/
│   └── accounts.json      # Stores user data and balances
├── extras/
│   ├── engineering\_drawing.png   # ATM design drawing
│   └── interface\_mockup.png      # UI/UX mockup
└── README.md

```

---

## ⚙️ How It Works

1. **User Authentication**  
   - Enter a **PIN** via keypad (Arduino) or console input.  
   - Validate credentials against stored data.  

2. **Select Operation**  
   - Options: **Balance Inquiry**, **Deposit**, **Withdrawal**, **Exit**  

3. **Perform Transaction**  
   - Update the account data accordingly.  
   - (Optional) Display messages on an **LCD screen** connected to the Arduino.  

4. **Log & Save**  
   - All transactions are logged for review.  

---

## 🚀 Future Improvements

- **Card Reader Integration** – Using RFID or NFC modules.  
- **Touchscreen UI** – Replace physical keypad with an interactive touch interface.  
- **Database Integration** – Migrate from JSON to MySQL/PostgreSQL for real banking simulation.  
- **Encryption** – Secure stored PINs and transactions with hashing.  

---

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE`](./LICENSE) for details.

---

## 👤 Author

**Hatim Ahmed Hassan** – 2025  
For inquiries or collaborations: **xayari229@gmail.com**
```

