from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from .models import Task, Goal, MoodEntry, Reflection, Habit, Transaction
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@login_required
def dashboard(request):

    today = timezone.localdate()
    tasks_today = Task.objects.filter(owner=request.user, due_date=today)
    mood_entry = MoodEntry.objects.filter(
        owner=request.user, date=today).first()
    reflection = Reflection.objects.filter(
        owner=request.user, date=today).first()
    month_transactions = Transaction.objects.filter(
        owner=request.user, date__year=today.year, date__month=today.month
    )
    income = month_transactions.filter(type="income").aggregate(
        total=Sum("amount"))["total"] or 0
    expenses = month_transactions.filter(type="expense").aggregate(
        total=Sum("amount"))["total"] or 0

    context = {
        "today": today,
        "tasks_today": tasks_today,
        "timed_tasks_today": tasks_today.exclude(due_time__isnull=True).order_by("due_time"),
        "tasks_today_count": tasks_today.count(),
        "today_mood": mood_entry.mood if mood_entry else None,
        "today_energy": mood_entry.energy if mood_entry else None,
        "today_reflection": reflection,
        "stats": {
            "completed": tasks_today.filter(is_completed=True).count(),
            "remaining": tasks_today.filter(is_completed=False).count(),
            "finance": {"income": income, "expenses": expenses, "balance": income - expenses},
            "transactions": month_transactions,
        },
        "goals": Goal.objects.filter(owner=request.user, is_archived=False)[:3],
    }
    return render(request, "dashboard.html", context)


@login_required
def tasks(request):
    today = timezone.localdate()
    tasks_today = Task.objects.filter(owner=request.user, due_date=today)
    context = {"tasks": Task.objects.filter(
        owner=request.user), "tasks_today": tasks_today, }
    return render(request, "tasks.html", context)


@login_required
def journal(request):

    today = timezone.localdate()
    context = {
        "today_reflection": Reflection.objects.filter(owner=request.user, date=today).first(),
        "past_entries": Reflection.objects.filter(owner=request.user).exclude(date=today),
    }
    return render(request, "journal.html", context)


@login_required
def habits(request):

    context = {"habits": Habit.objects.filter(
        owner=request.user, is_archived=False)}
    return render(request, "habits.html", context)


@login_required
def goals(request):

    context = {"goals": Goal.objects.filter(
        owner=request.user, is_archived=False)}
    return render(request, "goals.html", context)


@login_required
def finance(request):

    today = timezone.localdate()
    month_transactions = Transaction.objects.filter(
        owner=request.user, date__year=today.year, date__month=today.month
    )
    income = month_transactions.filter(type="income").aggregate(
        total=Sum("amount"))["total"] or 0
    expenses = month_transactions.filter(type="expense").aggregate(
        total=Sum("amount"))["total"] or 0

    context = {
        "finance": {"income": income, "expenses": expenses, "balance": income - expenses},
        "transactions": month_transactions,
    }
    return render(request, "finance.html", context)


@login_required
def settings(request):
    """if request.method == "POST" and "current_password" in request.POST:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keeps the user logged in"""
    """ {"password_form": form}"""
    return render(request, "settings.html")
