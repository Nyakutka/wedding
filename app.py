from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = os.environ.get('WEDDING_SECRET', 'change-me-for-prod')

# Basic wedding data
COUPLE = {
    'groom': 'Никита',
    'bride': 'Кира',
}
DATE = '09.08.2026'

DETAILS = {
    'time': '16:00',
    'venue_name': 'Vinity Amore',
    'address': 'Ленинградская область, Ломоносовский район, Лопухинское сельское поселение',
    # OpenStreetMap embed (centered at lon=29.340311, lat=59.732283)
    'map_url': 'https://www.openstreetmap.org/export/embed.html?bbox=29.330311%2C59.722283%2C29.350311%2C59.742283&layer=mapnik&marker=59.732283%2C29.340311',
    'map_link': 'https://www.openstreetmap.org/?mlat=59.732283&mlon=29.340311#map=14/59.732283/29.340311',
    'yandex_link': 'https://yandex.ru/maps/-/CLdqNUnO',
    'google_link': 'https://maps.app.goo.gl/QHFW24mnW7KfUTzd9',
    'two_gis_link': 'https://go.2gis.com/n9mH2',
    'parking': 'Парковка доступна на территории клуба. Рекомендуем подъезжать со стороны главной дороги и следовать указателям.',
    'dress_code': 'Smart casual (удобно и празднично)',
    'notes': 'Пожалуйста, подтвердите присутствие заранее. Есть парковка и детская зона.'
}

 

# Simple gallery images
GALLERY = [
    {'image': 'gallery1.jpg', 'caption': 'Настроение праздника'},
    {'image': 'gallery2.jpg', 'caption': 'Романтика на природе'},
    {'image': 'gallery3.jpg', 'caption': 'Весёлые моменты'},
    {'image': 'gallery4.jpg', 'caption': 'Уют и тепло'},
]

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
RSVP_CSV = os.path.join(DATA_DIR, 'rsvps.csv')
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'static', 'uploads')


def ensure_data_dir():
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.isfile(RSVP_CSV):
        with open(RSVP_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'email', 'attending', 'guests', 'message'])
    # ensure upload dir exists
    if not os.path.isdir(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.route('/')
def index():
    # Pass gallery and details
    return render_template('index.html', couple=COUPLE, date=DATE, gallery=GALLERY, details=DETAILS)


@app.route('/details')
def details():
    return render_template('details.html', details=DETAILS, couple=COUPLE, date=DATE)





@app.route('/rsvp', methods=['POST'])
def rsvp():
    ensure_data_dir()
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    attending = request.form.get('attending', 'no')
    guests = request.form.get('guests', '0')
    message = request.form.get('message', '').strip()

    if not name:
        flash('Пожалуйста, укажите имя.');
        return redirect(request.referrer or url_for('index'))

    with open(RSVP_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, email, attending, guests, message])

    return redirect(url_for('thankyou'))


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html', couple=COUPLE, date=DATE)


if __name__ == '__main__':
    ensure_data_dir()
    app.run(host='0.0.0.0', port=5000, debug=True)
