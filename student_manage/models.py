from django.db import models

CHOICES =[
    ('Computer Science', 'Computer Science'),
    ('Mathematics', 'Mathematics'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('English', 'English'),
    ('Geography', 'Geography'),
    ('History', 'History'),
    ('Sociology', 'Sociology'),
    ('Business', 'Business'),
    ('Arts', 'Arts'),
    ('Literature', 'Literature'),
    ('Fine Arts', 'Fine Arts'),
    ('Music', 'Music'),
    ('Physical Education', 'Physical Education'),
    ('Home Economics', 'Home Economics'),
    ('Health Science', 'Health Science'),
    ('Psychology', 'Psychology'),
    ('Sports Science', 'Sports Science'),
    ('Environmental Studies', 'Environmental Studies')
]

class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    branch = models.CharField(max_length=200,choices=CHOICES)

    def __str__(self):
        return self.fname + " " + self.lname

# Create your models here.
