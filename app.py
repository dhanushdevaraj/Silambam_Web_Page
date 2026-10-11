"""
Silambam Martial Arts Academy - Flask Web Application
Provides online presence, curriculum showcase, interactive timetable,
and SQLite-backed Student Trial Class / Admission booking system.
"""

import os
import csv
import io
from flask import Flask, render_template, request, redirect, url_for, flash, Response, jsonify
import database

app = Flask(__name__)
app.secret_key = 'silambam_warrior_secret_key_2026'

# Ensure database tables exist on startup
database.init_db()

# Academy Configuration Information (Easily customizable)
ACADEMY_INFO = {
    "name": "Kalai Thai Silambam Dharmapuri",
    "short_name": "Kalai Thai Silambam",
    "city": "Dharmapuri",
    "tamil_name": "கலைத்தாய் சிலம்பம் தருமபுரி",
    "tagline": "Ancient Tamil Warrior Heritage of Dharmapuri",
    "phone": "+91 98765 43210",
    "whatsapp": "919876543210",
    "email": "contact@kalaithaisilambam.com",
    "address": "Kalai Thai Silambam Training Arena, Dharmapuri, Tamil Nadu, India",
    "timings": "Mon - Sun: 5:30 AM - 9:30 AM | 5:00 PM - 8:30 PM",
    "head_master": "Ashan Manikandan",
    "head_master_tamil": "ஆசான் மணிகண்டன்",
    "experience_years": "Traditional Dharmapuri Gurukulam"
}


@app.context_processor
def inject_academy_info():
    """Makes academy metadata globally accessible across all Jinja templates."""
    return dict(academy=ACADEMY_INFO)


@app.route('/')
def home():
    """Main landing page featuring hero banner, heritage, programs, and quick booking."""
    return render_template('index.html')


@app.route('/programs')
def programs():
    """Detailed curriculum and training programs page."""
    return render_template('programs.html')


@app.route('/weapons')
def weapons():
    """Traditional Silambam weapons guide and cultural history."""
    return render_template('weapons.html')


@app.route('/schedule')
def schedule():
    """Class timetable and interactive tuition fee calculator."""
    return render_template('schedule.html')


@app.route('/book-trial', methods=['GET', 'POST'])
def book_trial():
    """Handles online registration and free trial class bookings."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        age = request.form.get('age', '').strip()
        experience = request.form.get('experience', 'Beginner')
        batch = request.form.get('batch', 'Morning Batch')
        preferred_date = request.form.get('preferred_date', '')
        notes = request.form.get('notes', '').strip()

        # Simple validation
        if not name or not phone:
            flash('Please provide at least your full name and phone number.', 'danger')
            return render_template('book_trial.html')

        try:
            booking_id = database.add_trial_booking(
                name=name,
                phone=phone,
                email=email,
                age=int(age) if age.isdigit() else None,
                experience_level=experience,
                batch_preference=batch,
                preferred_date=preferred_date,
                notes=notes
            )
            flash('Success! Your free trial session has been reserved.', 'success')
            return redirect(url_for('booking_success', booking_id=booking_id))
        except Exception as e:
            flash(f'An error occurred while booking: {str(e)}', 'danger')
            return render_template('book_trial.html')

    return render_template('book_trial.html')


@app.route('/booking-success/<int:booking_id>')
def booking_success(booking_id):
    """Booking confirmation screen with reference ID and WhatsApp follow-up link."""
    return render_template('success.html', booking_id=booking_id)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact details and inquiry message form."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', 'General Inquiry').strip()
        message = request.form.get('message', '').strip()

        if not name or not phone or not message:
            flash('Please fill in your name, contact phone, and message.', 'danger')
            return render_template('contact.html')

        database.add_contact_inquiry(name, phone, email, subject, message)
        flash('Thank you! Your message has been received. Our team will contact you shortly.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/admin')
def admin_dashboard():
    """Admin dashboard to view bookings and inquiries stored in SQLite."""
    status_filter = request.args.get('status', 'All')
    bookings = database.get_all_bookings(status_filter)
    inquiries = database.get_all_inquiries()
    stats = database.get_dashboard_stats()
    return render_template(
        'admin.html',
        bookings=bookings,
        inquiries=inquiries,
        stats=stats,
        current_filter=status_filter
    )


@app.route('/admin/update-status/<int:booking_id>', methods=['POST'])
def update_status(booking_id):
    """Updates status for a student booking."""
    new_status = request.form.get('status', 'New')
    database.update_booking_status(booking_id, new_status)
    flash(f'Booking #{booking_id} updated to "{new_status}".', 'info')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/delete-booking/<int:booking_id>', methods=['POST'])
def delete_booking(booking_id):
    """Removes a booking record."""
    database.delete_booking(booking_id)
    flash(f'Booking #{booking_id} removed successfully.', 'warning')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/export-csv')
def export_csv():
    """Exports all student registrations to CSV for spreadsheet use."""
    bookings = database.get_all_bookings('All')
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Name', 'Phone', 'Email', 'Age', 'Experience', 'Batch Preference', 'Preferred Date', 'Notes', 'Status', 'Registered At'])

    for b in bookings:
        writer.writerow([
            b['id'], b['name'], b['phone'], b['email'] or '',
            b['age'] or '', b['experience_level'] or '',
            b['batch_preference'] or '', b['preferred_date'] or '',
            b['notes'] or '', b['status'], b['created_at']
        ])

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=silambam_student_bookings.csv"}
    )


if __name__ == '__main__':
    # Running locally on http://127.0.0.1:5000
    app.run(host='127.0.0.1', port=5000, debug=True)
