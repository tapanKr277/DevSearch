import os
import django
import random
from faker import Faker

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')  # Change `your_project` to your project name
django.setup()

from users.models import Profile, Skill
from projects.models import Project, Tag, Review
from django.contrib.auth.models import User

fake = Faker()

from users.signals import createProfile
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Disconnect the email signal before seeding
post_save.disconnect(createProfile, sender=User)

def create_profiles(n=20):
    profiles = []
    for _ in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
        profile = Profile.objects.create(
            user=user,
            name=fake.name(),
            email=user.email,
            username=user.username,
            location=fake.city(),
            short_intro=fake.sentence(),
            bio=fake.paragraph(),
            social_github=fake.url(),
            social_linkedin=fake.url(),
            social_twitter=fake.url(),
            social_youtube=fake.url(),
            social_website=fake.url()
        )
        profiles.append(profile)
    return profiles

def create_tags():
    tag_names = ['Python', 'Django', 'React', 'Docker', 'API', 'AWS', 'UI/UX', 'JavaScript', 'PostgreSQL', 'Machine Learning']
    tags = []
    for name in tag_names:
        tag, _ = Tag.objects.get_or_create(name=name)
        tags.append(tag)
    return tags

def create_projects(profiles, tags, n=20):
    projects = []
    for _ in range(n):
        owner = random.choice(profiles)
        project = Project.objects.create(
            owner=owner,
            title=fake.sentence(nb_words=4),
            description=fake.paragraph(),
            demo_link=fake.url(),
            source_link=fake.url()
        )
        selected_tags = random.sample(tags, k=random.randint(1, 4))
        project.tags.set(selected_tags)
        project.save()
        projects.append(project)
    return projects

def create_reviews(projects, profiles, n=40):
    for _ in range(n):
        project = random.choice(projects)
        owner = random.choice(profiles)
        if not Review.objects.filter(project=project, owner=owner).exists():
            Review.objects.create(
                project=project,
                owner=owner,
                value=random.choice(['up', 'down']),
                body=fake.sentence()
            )
        project.getVoteCount  # trigger vote ratio update

def create_skills(profiles, n=30):
    for _ in range(n):
        Skill.objects.create(
            owner=random.choice(profiles),
            name=fake.job(),
            description=fake.sentence()
        )

if __name__ == '__main__':
    print("Seeding data...")
    profiles = create_profiles(20)
    tags = create_tags()
    projects = create_projects(profiles, tags, 20)
    create_reviews(projects, profiles, 40)
    create_skills(profiles, 30)
    print("Done seeding!")
