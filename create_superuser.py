# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from users.signals import createProfile  # if this signal sends email
from django.contrib.auth.models import User

# Disconnect the signal that might send email
post_save.disconnect(createProfile, sender=User)

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✅ Superuser created: admin / admin123")
else:
    print("ℹ️ Superuser already exists")
