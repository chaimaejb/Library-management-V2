# Library Management System

A modular Python application for managing books, members, and library operations — built with clean architecture and persistent JSON storage.

---

## Features

### Member Management
- Create, block, and end memberships
- Secure password management via `bcrypt`
- Two membership types: **Student** (limited borrowing) and **Premium** (higher capacity)

### Book Management
- Add and remove books (manager-only)
- Track availability, borrowing history, and lost books
- Borrow and return books with deadline enforcement

### Internal Law Management
- Managers can configure borrowing deadlines, late fees, and loss penalties
- Members can view current rules at any time

### Notifications
Members are automatically notified when:
- A book becomes available from the waiting list
- A reservation expires
- Internal laws are updated

### Data Persistence
All data is stored in JSON files: books, members, borrowed books, waiting lists, notifications, internal law, and member tracking.

---

## Project Structure

```
LIBRARY MANAGEMENT/
│
├── data/
│   ├── books.json
│   ├── borrowedBooks.json
│   ├── internalLaw.json
│   ├── members.json
│   ├── nextMember.json
│   ├── notifications.json
│   └── waitingList.json
│
└── main/
    ├── abstracts/          # LibraryItem, MembershipStrategy
    ├── dataProvider/       # JSON read/write handlers
    ├── exceptions/         # Custom exceptions (e.g. BookNotAvailable)
    ├── helper/             # Validation and utility helpers
    ├── interface/          # CLI, Facade, and user interfaces
    ├── mappers/            # Data transformation (Book, DVD, Member, etc.)
    ├── model/              # Domain models (Book, DVD, Member, InternalLaw)
    ├── services/           # Business logic (BookService, MemberService, WaitingList)
    ├── track/              # Book tracking
    └── __main__.py
```

---

## Requirements

- Python 3.13.11
- [`bcrypt`](https://pypi.org/project/bcrypt/)

Standard libraries used: `json`, `collections`, `datetime`, `pathlib`, `uuid`, `abc`

---

## Installation

1. Install Python 3.13.11
2. Install the required dependency:

```bash
pip install bcrypt
```

---

## Usage

Run from the root project directory:

```bash
python main/__main__.py
```

---

## Design Patterns

- **Strategy Pattern** — `MembershipStrategy` for membership type behavior
- **Facade Pattern** — `LibraryFacade` for simplified interface
- **Data Mapper Pattern** — clean separation between models and storage
- **Layered Architecture** — models, services, data providers, and interface are fully decoupled
- **UUID-based identifiers** and **bcrypt password hashing**

---

## Roadmap

- [ ] Graphical User Interface (GUI)
- [ ] Replace JSON storage with a relational database
- [ ] Advanced search and filtering
- [ ] Role-based authentication
- [ ] Unit testing suite

---

## Author

**Chaimae Jbaida** — Python Developer in progress 🚀
