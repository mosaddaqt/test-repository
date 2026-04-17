import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld.settings')

application = get_wsgi_application()
```

---

### What was created

| File | Purpose |
|---|---|
| `requirements.txt` | Pins Django 4.2 |
| `manage.py` | Django CLI entry point |
| `helloworld/settings.py` | Minimal Django config |
| `helloworld/urls.py` | Routes `/` to the view |
| `helloworld/views.py` | Returns `<h1>Hello World</h1>` |
| `helloworld/wsgi.py` | WSGI entry point for deployment |

### To run locally
```bash
pip install -r requirements.txt
python manage.py runserver
```
Then open **http://127.0.0.1:8000** — you'll see **Hello World**.