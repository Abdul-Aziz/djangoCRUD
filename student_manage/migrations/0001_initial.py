# Generated by Django 5.1.3 on 2024-12-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('branch', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('English', 'English'), ('Geography', 'Geography'), ('History', 'History'), ('Sociology', 'Sociology'), ('Business', 'Business'), ('Arts', 'Arts'), ('Literature', 'Literature'), ('Fine Arts', 'Fine Arts'), ('Music', 'Music'), ('Physical Education', 'Physical Education'), ('Home Economics', 'Home Economics'), ('Health Science', 'Health Science'), ('Psychology', 'Psychology'), ('Sports Science', 'Sports Science'), ('Environmental Studies', 'Environmental Studies')], max_length=200)),
            ],
        ),
    ]
