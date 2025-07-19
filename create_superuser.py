import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from users.signals import createProfile  # Custom signal that creates profile
from users.models import Profile

User = get_user_model()

# Disconnect the signal to prevent sending emails
post_save.disconnect(createProfile, sender=User)

# Create the superuser
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    # Manually create the profile
    Profile.objects.create(
        user=user,
        name='Admin User',
        username='admin',
        email='admin@example.com',
        location='Admin City',
        short_intro='Superuser account',
        bio='This is the admin account.',
    )
    print("✅ Superuser and profile created: admin / admin123")
else:
    print("ℹ️ Superuser already exists")
