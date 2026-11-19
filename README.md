# BUzz – Campus Event & Opportunity Discovery System

A Python-based command-line application developed for **Computational Thinking and Programming (2026CSAE100)** at **Bennett University**.

## About the Project
Campus event information—such as club recruitments, workshops, hackathons, and seminars—is often scattered across WhatsApp groups, Instagram pages, and LMS announcements. **BUzz** provides a centralized command-line system where students and organizers can store, browse, search, manage, and discover campus events.

## Features
- **Browse Events (`browse`)**: Displays all campus events in chronological order.
- **Keyword Search (`search`)**: Searches across event titles, categories, and descriptions.
- **Event Management (`add`, `edit`, `delete`)**: Add new events with auto-generated unique IDs, update existing records, or delete events with confirmation.
- **Interest-Based Recommendations (`recommend`)**: Matches comma-separated user interests against event details and ranks results by match score (and date for ties).
- **Event Statistics (`stats`)**: Shows total event count, category-wise distribution, and the most active category.
- **CSV Storage**: Automatically saves and loads event records using `events.csv`.

## Technologies Used
- **Language:** Python 3
- **Built-in Libraries:** `csv`, `os`, `datetime`

## How to Run
1. Download `Pythoncollab.py`.
2. Open it in Python IDLE or run it from the terminal:
   ```bash
   python Pythoncollab.py
