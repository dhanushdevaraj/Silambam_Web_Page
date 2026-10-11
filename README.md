# ⚔️ Veera Silambam Academy Web Application

A modern, high-performance, responsive martial arts website built with **Python (Flask)** and **SQLite**, designed specifically for traditional Silambam academies, masters, and instructors.

---

## 🌟 Key Features

- **Warrior Aesthetics:** Dark obsidian slate theme, vibrant amber/gold accents, subtle glassmorphism, responsive navigation drawer, and martial typography.
- **Online Free Trial / Admission Booking:**
  - Fast, intuitive registration form with date picker, batch selector, and notes.
  - Automatically stored in local **SQLite database** (`silambam.db`).
  - Booking confirmation receipt with reference ID and direct **WhatsApp notification** to the Guru.
- **Admin Management Dashboard (`/admin`):**
  - Real-time KPI statistics (Total Bookings, Pending, Enrolled Students).
  - Instant status updates (*New* → *Contacted* → *Enrolled* → *Cancelled*).
  - One-click **Export to Excel (CSV)** for student rosters.
  - One-click WhatsApp message button to contact any student directly.
- **Curriculum & Weapons Showcase (`/programs` & `/weapons`):**
  - Full belt progression syllabus (White to Black Belt / Ashan).
  - Traditional weaponry breakdown: Nedunkambu (Bamboo Staff), Kurunkambu (Short Sticks), Surul Vaal (Flexible Sword), Maduvu (Deer Horns).
- **Interactive Tuition Fee Calculator (`/schedule`):**
  - Dynamically calculates monthly, quarterly (10% off), or annual (25% off) fees with optional starter weapon kit add-ons.
- **Direct WhatsApp Widget:**
  - Floating WhatsApp action button for instant mobile inquiries.

---

## 🚀 How to Run Locally

### Option 1: Double-Click Launcher (Windows)
Double-click the included `run.bat` file in this directory.

### Option 2: Terminal / PowerShell
```powershell
python app.py
```

Then open your browser at:
👉 **`http://127.0.0.1:5000`**

To view received student registrations in the admin portal:
👉 **`http://127.0.0.1:5000/admin`**

---

## 📸 How to Use Your Own Images

Your website already includes high-resolution sample photography in `static/images/`. To replace them with your actual class and academy photos:

1. Copy your photos into the folder:
   ```
   Silambam_Web_Page/static/images/
   ```
2. Name them as follows to replace the corresponding slots automatically:
   - **`hero-bg.jpg`** — Main large banner at the top of the homepage
   - **`training.jpg`** — Class training / student practice photo
   - **`weapons.jpg`** — Traditional weapons & equipment display
   - **`master.jpg`** — Chief Guru / Instructor portrait
3. Refresh your browser!

*(You can also add any additional images, such as `tournament.jpg` or `student1.jpg`, and link them in any template).*

---

## ⚙️ Customizing Your Academy Information

All academy contact information and details are configured in one place in `app.py`:

Open `app.py` and modify the `ACADEMY_INFO` dictionary:
```python
ACADEMY_INFO = {
    "name": "Your Academy Name",
    "tamil_name": "உங்கள் அகாடமி பெயர்",
    "tagline": "Master the Ancient Art of Tamil Warriors",
    "phone": "+91 98765 43210",
    "whatsapp": "919876543210",
    "email": "contact@yourdomain.com",
    "address": "Your Academy Address, City, Tamil Nadu",
    "timings": "Mon - Sun: 5:30 AM - 9:30 AM | 5:00 PM - 8:30 PM",
    "head_master": "Ashan Name",
    "experience_years": "25+ Years of Gurukulam Tradition"
}
```
All pages, the header, the footer, and WhatsApp links will update automatically!

---

## 🗄️ Project Structure

```
Silambam_Web_Page/
├── app.py                      # Flask routes, API endpoints, and configuration
├── database.py                 # SQLite database helper functions
├── silambam.db                 # SQLite database (stores student registrations & inquiries)
├── requirements.txt            # Python dependencies
├── run.bat                     # Windows one-click start script
├── run.ps1                     # PowerShell start script
├── README.md                   # Documentation
├── static/
│   ├── css/
│   │   └── style.css           # Premium warrior design system (Vanilla CSS)
│   ├── js/
│   │   └── main.js             # Mobile nav, fee calculator, accordion, validation
│   └── images/
│       ├── hero-bg.jpg         # Hero banner
│       ├── training.jpg        # Training session photo
│       ├── weapons.jpg         # Weapons photo
│       ├── master.jpg          # Chief Guru portrait
│       └── README.txt          # Image swap instructions
└── templates/
    ├── base.html               # Master layout, navigation, footer, WhatsApp widget
    ├── index.html              # Homepage with hero, programs, timetable, reviews, booking
    ├── programs.html           # Full curriculum and belt progression
    ├── weapons.html            # Silambam weaponry encyclopedia
    ├── schedule.html           # Batch timetable and interactive fee calculator
    ├── book_trial.html         # Dedicated online registration page
    ├── success.html            # Booking receipt and confirmation
    ├── contact.html            # Contact details and direct message form
    └── admin.html              # Admin management portal & CSV export
```

---

## 🛡️ License & Heritage
Preserving and celebrating the sacred martial heritage of Tamil Nadu.
