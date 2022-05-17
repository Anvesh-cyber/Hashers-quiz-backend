from distutils.command.upload import upload
from django.db import models


class User(models.Model):
    profile = models.TextField(blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32,blank=True)
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    )  
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    mobile_number = models.BigIntegerField()
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.email + " (" +  self.first_name + " )"







class Quiz(models.Model):
    type_quiz = models.CharField(max_length=100)

    def __str__(self):
        return self.type_quiz

class Question(models.Model):
    type_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

    def get_question():
        return self.question_set.all

class Answer(models.Model):
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    score = models.IntegerField()

    def __str__(self):
        return self.text

    def get_answers():
        return self.anwer.all

class Result(models.Model):
    type_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField()


