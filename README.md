# PACE: An Encrypted Secondary Physical Clipboard
![How to copy and paste between computers](https://preview.redd.it/slpt-how-to-copy-and-paste-between-computers-v0-wpkv1rtiy0k81.jpg?width=640&crop=smart&auto=webp&s=9886243f5a228b2ed364b85a61238d27c735b040)

## Project Overview
**PACE** is a virtual encrypted intelligent clipboard that enhances productivity by enabling secure data transfer and multi-system management. Designed for seamless copying, pasting, and transferring of files and credentials, PACE offers a user-friendly, secure, and efficient way to manage data across multiple systems.

---

## Key Features
- **Multi-System Clipboard**: Store and manage multiple copied items in a stack for easy access.
- **Encryption**: Secure your data with one-click encryption, ensuring privacy across systems.
- **Password Management**: Save and auto-fill credentials securely with a master password.
- **Cross-Device Functionality**: Switch between devices effortlessly with wired or wireless connectivity.
- **Ease of Use**: Simple shortcuts for copy, paste, encrypt, decrypt, and more.

---

## Motivation
The idea for PACE originated from a need to simplify tasks like copying and pasting across multiple systems or filling repetitive information on websites. It eliminates the need for external devices or complex software for data transfer.

---

## Scope
PACE is ideal for sectors like BPOs, design firms, and events management, where managing multiple independent systems is a necessity. Its ability to reduce complexity and increase efficiency makes it invaluable for professionals and organizations.

---

## Objective
To develop a software and hardware combination that:
- Enables secure data sharing between systems.
- Simplifies multitasking by reducing dependency on external storage devices.
- Provides a universal clipboard for easy file and credential management.

---

## Technologies Used
- **Programming Languages**: Python (Core logic and cryptography)
- **Hardware**: Arduino Uno and Leonardo
- **Libraries**: 
  - `keyboard` (hotkeys)
  - `pyperclip` (clipboard handling)
  - `cryptocode` (encryption/decryption)
  - `pyfirmata` (Arduino communication)
- **Protocols**: Firmata for Arduino communication

---

## Hardware Requirements
- Arduino Uno / Leonardo
- IR Sensors
- Wi-Fi Module
- USB connectivity for Arduino boards

---

## Design Framework
PACE employs:
- **Stack Implementation**: Allows storing multiple copied items in a Last-In-First-Out (LIFO) manner.
- **Cryptography**: Ensures secure handling of sensitive data like passwords.
- **Arduino Integration**: Facilitates seamless hardware interaction for device switching and clipboard functionality.

---

## Installation and Usage
### Prerequisites:
1. Install Python 3.8 or higher.
2. Install required Python libraries using:
   ```bash
   pip install keyboard pyperclip cryptocode pyfirmata
