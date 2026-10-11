"""
Database management module for Silambam Academy Web Application.
Uses SQLite for zero-configuration, robust local data storage.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'silambam.db')


def get_db_connection():
    """Returns a connection to the SQLite database with dict-like row access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes database tables if they do not exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Table for Free Trial Class & Student Registrations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trial_bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            age INTEGER,
            experience_level TEXT,
            batch_preference TEXT,
            preferred_date TEXT,
            notes TEXT,
            status TEXT DEFAULT 'New',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Table for General Contact Inquiries
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_inquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            subject TEXT,
            message TEXT NOT NULL,
            status TEXT DEFAULT 'Unread',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def add_trial_booking(name, phone, email, age, experience_level, batch_preference, preferred_date, notes):
    """Inserts a new student trial booking into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trial_bookings (name, phone, email, age, experience_level, batch_preference, preferred_date, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, phone, email, age, experience_level, batch_preference, preferred_date, notes))
    booking_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return booking_id


def get_all_bookings(status_filter=None):
    """Retrieves all student bookings, optionally filtered by status."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if status_filter and status_filter != 'All':
        cursor.execute('SELECT * FROM trial_bookings WHERE status = ? ORDER BY created_at DESC', (status_filter,))
    else:
        cursor.execute('SELECT * FROM trial_bookings ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_booking_status(booking_id, new_status):
    """Updates status for a trial booking (e.g. New -> Contacted -> Enrolled)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE trial_bookings SET status = ? WHERE id = ?', (new_status, booking_id))
    conn.commit()
    conn.close()


def delete_booking(booking_id):
    """Deletes a trial booking record."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM trial_bookings WHERE id = ?', (booking_id,))
    conn.commit()
    conn.close()


def add_contact_inquiry(name, phone, email, subject, message):
    """Saves a contact message."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contact_inquiries (name, phone, email, subject, message)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, phone, email, subject, message))
    inquiry_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return inquiry_id


def get_all_inquiries():
    """Retrieves all contact inquiries."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contact_inquiries ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_dashboard_stats():
    """Returns quick count statistics for the admin overview."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM trial_bookings')
    total_bookings = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM trial_bookings WHERE status = 'New'")
    new_bookings = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM trial_bookings WHERE status = 'Enrolled'")
    enrolled_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM contact_inquiries')
    total_inquiries = cursor.fetchone()[0]

    conn.close()
    return {
        'total_bookings': total_bookings,
        'new_bookings': new_bookings,
        'enrolled_count': enrolled_count,
        'total_inquiries': total_inquiries
    }
