# दत्तधाम सप्ताह नावनोंदणी वेबसाइट

Python Django आधारित responsive website. Public users फॉर्म भरू शकतात; नोंदणीची संपूर्ण माहिती फक्त Admin Login नंतर दिसते.

## आवश्यक
- Python 3.10 किंवा नवीन
- इंटरनेट (पहिल्यांदा packages install करण्यासाठी)

## Windows वर चालवण्याची पद्धत
1. ZIP extract करा.
2. त्या folder मध्ये CMD / PowerShell उघडा.
3. खालील commands चालवा:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

4. वेबसाइट: http://127.0.0.1:8000/
5. Admin Dashboard: http://127.0.0.1:8000/admin-panel/login/

`createsuperuser` करताना स्वतःचे username, email (optional) आणि मजबूत password द्या. Password code मध्ये hardcode केलेला नाही.

## Admin सुविधा
- Dashboard आणि Total Registrations
- Registration यादी, details, edit आणि delete
- नाव / मोबाईल नंबर search
- PDF / Excel download आणि print
- सप्ताहाची माहिती व कार्यक्रम Django Admin मधून edit करता येतात

Django Admin: http://127.0.0.1:8000/django-admin/

## Online Deploy (Render)
1. हा project GitHub repository मध्ये upload करा.
2. Render वर New Web Service निवडा आणि repository connect करा.
3. Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
4. Start Command: `gunicorn saptah.wsgi:application`
5. Environment Variables:
   - `SECRET_KEY` = स्वतःचा random secret key
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = तुमचा Render domain (उदा. `your-app.onrender.com`)
   - `CSRF_TRUSTED_ORIGINS` = `https://your-app.onrender.com`

Production मध्ये persistent database (PostgreSQL) आणि persistent storage वापरणे शिफारसीय आहे. या starter project मध्ये SQLite वापरले आहे; Render ephemeral filesystem वर SQLite data deploy/restart नंतर टिकेलच याची खात्री नसते. Public launch पूर्वी persistent PostgreSQL जोडा.

## महत्त्वाचे
- Public page वर इतर सेवेकऱ्यांची माहिती दाखवली जात नाही.
- Admin routes login protected आहेत.
- पहिल्या live launch आधी सर्व तारखा, वेळा, धार्मिक मजकूर आणि संस्थेचा Logo तपासून घ्या.
- Logo सध्या Reference PDF मधील जागेसाठी placeholder आहे; प्रत्यक्ष Logo file `static/images/logo.png` मध्ये ठेवा आणि template मध्ये update करा.


## नवीन अपडेट
- मुख्य Header मध्ये दिलेला श्री स्वामी समर्थांचा फोटो Logo म्हणून जोडला आहे.
- नोंदणी फॉर्ममधील WhatsApp Group प्रश्नाखाली QR Code आणि थेट Join लिंक दिली आहे.
