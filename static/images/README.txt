HOW TO USE YOUR OWN IMAGES:
===================================
You can easily replace the sample images in this folder with your actual photos:

1. hero-bg.jpg   -> Main banner image shown at the top of the website
2. training.jpg  -> Class & students practice photo
3. weapons.jpg   -> Silambam weapons & equipment photo
4. master.jpg    -> Chief Instructor / Ashan / Guru photo

HOW TO REPLACE:
- Rename your own image files to match the names above (e.g., hero-bg.jpg)
- Paste them directly into this folder: static/images/
- Refresh your browser!

You can also drop any additional photos here (e.g., student1.jpg, tournament.jpg)
and reference them in the HTML templates as {{ url_for('static', filename='images/your_photo.jpg') }}.
