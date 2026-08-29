from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):

    class Priority(models.TextChoices):
        HIGH = "high", "High"
        MEDIUM = "medium", "Medium"
        LOW = "low", "Low"

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    due_date = models.DateField()
    due_time = models.TimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['due_time', '-priority']

    def __str__(self):
        return self.title


class MoodEntry(models.Model):

    class Mood(models.TextChoices):
        GREAT = "great", "😄"
        GOOD = "good", "🙂"
        OKAY = "okay", "😐"
        LOW = "low", "😔"
        BAD = "bad", "😞"

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE, related_name='moods')
    date = models.DateField()
    mood = models.CharField(
        max_length=10, choices=Mood.choices, default=Mood.OKAY)
    energy = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ['owner', 'date']

    def __str__(self):
        return f'{self.owner} - {self.mood} - {self.date}'


class Reflection(models.Model):

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE, related_name='reflections')
    date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.owner} - {self.date}'


class Goal(models.Model):

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=75)
    target_date = models.DateField(null=True, blank=True)
    progress = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-progress']

    def __str__(self):
        return self.title


class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = 'income', 'Income'
        EXPENSE = 'expense', 'Expense'

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=Type.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    @property
    def sign(self):
        return "+" if self.type == self.Type.INCOME else "-"

    def __str__(self):
        sign = "+" if self.type == self.Type.INCOME else "-"
        return f"{sign}{self.amount} — {self.description or self.type}"
