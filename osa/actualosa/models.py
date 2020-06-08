from django.db import models

# Create your models here.

class Command(models.Model):
    command = models.CharField(max_length=200)
    instrumentResponse = models.CharField(max_length=200)

class State(models.Model):
    POSSIBLE_STATES = [
        ("R", "RUN"),
        ("I","IDLE"),
        ("RO","RUN ONCE")
    ]
    state = models.CharField(max_length=4, choices = POSSIBLE_STATES, default="I")

