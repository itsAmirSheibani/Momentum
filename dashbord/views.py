from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Sum, Avg
from django.contrib import messages
from .models import Task, Goal, MoodEntry, Reflection, Transaction
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import *


@login_required
def edit_journal(request, reflection_id):

    reflection = get_object_or_404(
        Reflection, id=reflection_id, owner=request.user)

    if request.method == 'POST':

        form = ReflectionForm(request.POST, instance=reflection)

        if form.is_valid():
            form.save()

            return redirect('dashbord:journal')

    else:
        form = ReflectionForm(instance=reflection)

    context = {
        "form": form,
        "page_title": "Edit Reflection",
        "page_subtitle": "Update your reflection details.",
        "submit_text": "Save Changes",
        "cancel_url": reverse("dashbord:journal"),
    }

    return render(
        request,
        "edit.html",
        context
    )


@login_required
def edit_goal(request, goal_id):

    goal = get_object_or_404(Goal, id=goal_id, owner=request.user)

    if request.method == 'POST':

        form = GoalForm(request.POST, instance=goal)

        if form.is_valid():
            form.save()

            return redirect('dashbord:goals')

    else:
        form = GoalForm(instance=goal)

    context = {
        "form": form,
        "page_title": "Edit Goal",
        "page_subtitle": "Update your goal details.",
        "submit_text": "Save Changes",
        "cancel_url": reverse("dashbord:goals"),
    }

    return render(
        request,
        "edit.html",
        context
    )


@login_required
def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id, owner=request.user)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('dashbord:tasks')

    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
        "page_title": "Edit Task",
        "page_subtitle": "Update your task details.",
        "submit_text": "Save Changes",
        "cancel_url": reverse("dashbord:tasks"),
    }

    return render(
        request,
        "edit.html",
        context
    )


@login_required
def edit_finance(request, transaction_id):

    transaction = get_object_or_404(
        Transaction, id=transaction_id, owner=request.user)

    if request.method == 'POST':

        form = FinanceForm(request.POST, instance=transaction)

        if form.is_valid():
            form.save()

            return redirect('dashbord:finance')

    else:
        form = FinanceForm(instance=transaction)

    context = {
        "form": form,
        "page_title": "Edit Transaction",
        "page_subtitle": "Update your transaction details.",
        "submit_text": "Save Changes",
        "cancel_url": reverse("dashbord:finance"),
    }

    return render(
        request,
        "edit.html",
        context
    )


@login_required
def delete_finance(request, transaction_id):
    if request.method == 'POST':
        transaction = get_object_or_404(Transaction,
                                        id=transaction_id, owner=request.user)
        transaction.delete()

    return redirect('dashbord:finance')


@login_required
def delete_goal(request, goal_id):
    if request.method == 'POST':
        goal = get_object_or_404(Goal,
                                 id=goal_id, owner=request.user)
        goal.delete()

    return redirect('dashbord:goals')


@login_required
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id,
                                 owner=request.user)

        task.delete()

    return redirect('dashbord:tasks')


@login_required
def delete_journal(request, reflection_id):
    if request.method == 'POST':
        reflection = get_object_or_404(Reflection, id=reflection_id,
                                       owner=request.user)

        reflection.delete()

    return redirect('dashbord:journal')


@login_required
def add_goal(request):
    today = timezone.localdate()
    if request.method == "POST":
        form = GoalForm(request.POST)

        if form.is_valid():
            goal = form.save(commit=False)
            goal.owner = request.user

            goal.save()

            return redirect("dashbord:goals")

    else:
        form = GoalForm()

    context = {
        "form": form,
        "page_title": "Add Goal",
        "page_subtitle": "Add a goal you wanna achieve.",
        "submit_text": "Add Goal",
        "cancel_url": reverse("dashbord:goals"),
    }

    return render(request, "add.html", context)


@login_required
def add_finance(request):
    today = timezone.localdate()
    if request.method == "POST":
        form = FinanceForm(request.POST)

        if form.is_valid():
            finance = form.save(commit=False)
            finance.owner = request.user
            finance.date = today
            finance.save()

            return redirect("dashbord:finance")

    else:
        form = FinanceForm()

    context = {
        "form": form,
        "page_title": "Add Transaction",
        "page_subtitle": "Add a transaction you did today.",
        "submit_text": "Add Transaction",
        "cancel_url": reverse("dashbord:finance"),
    }

    return render(request, 'add.html', context)


@login_required
def add_task(request):
    today = timezone.localdate()
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.due_date = today
            task.save()
            
            return redirect("dashbord:tasks")

    else:
        form = TaskForm()

    context = {
        "form": form,
        "page_title": "Add Task",
        "page_subtitle": "Add something you want to accomplish today.",
        "submit_text": "Add Task",
        "cancel_url": reverse("dashbord:tasks"),
    }

    return render(request, "add.html", context)


@login_required
def toggle_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        owner=request.user
    )

    task.is_completed = not task.is_completed

    if task.is_completed:
        task.completed_at = timezone.now()
    else:
        task.completed_at = None

    task.save()

    return redirect(request.META.get("HTTP_REFERER", "dashbord:dashboard"))


@login_required
def dashboard(request):
    today = timezone.localdate()

    # mood / energy
    if request.method == "POST" and (
        "mood" in request.POST or "energy" in request.POST
    ):
        mood = request.POST.get("mood")
        energy = request.POST.get("energy")

        entry, _created = MoodEntry.objects.get_or_create(
            owner=request.user,
            date=today,
            defaults={
                "mood": mood or MoodEntry.Mood.OKAY,
                "energy": int(energy) if energy else 5,
            },
        )
        if mood:
            entry.mood = mood
        if energy:
            entry.energy = int(energy)
        entry.save()

        return redirect("dashbord:dashboard")

    # reflection
    if request.method == "POST":
        form = ReflectionForm(request.POST)

        if form.is_valid():
            reflect = form.save(commit=False)
            reflect.owner = request.user
            reflect.date = today
            reflect.save()

            return redirect("dashbord:dashboard")

    else:
        form = ReflectionForm()

    today_reflections = Reflection.objects.filter(
        owner=request.user,
        date=today
    ).order_by("-id")

    past_entries = Reflection.objects.filter(
        owner=request.user
    ).exclude(
        date=today
    ).order_by("-date", "-id")

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

    goals_progress = Goal.objects.filter(owner=request.user).aggregate(
        avg=Avg("progress"))["avg"] or 0

    context = {
        "today": today,
        "tasks_today": tasks_today,
        "timed_tasks_today": tasks_today.exclude(due_time__isnull=True).order_by("due_time"),
        "tasks_today_count": tasks_today.count(),
        "today_mood": mood_entry.mood if mood_entry else None,
        "today_mood_display": mood_entry.get_mood_display() if mood_entry else "",
        "today_energy": mood_entry.energy if mood_entry else None,
        "today_reflection": reflection,
        "stats": {
            "completed": tasks_today.filter(is_completed=True).count(),
            "remaining": tasks_today.filter(is_completed=False).count(),
        },
        "finance": {"income": income, "expenses": expenses, "balance": income - expenses},
        "transactions": month_transactions,
        "goals": Goal.objects.filter(owner=request.user)[:3],
        "goals_progress": round(goals_progress),
        "today_reflections": today_reflections,
        "past_entries": past_entries,
        "form": form,
    }
    return render(request, "dashboard.html", context,)


@login_required
def tasks(request):
    today = timezone.localdate()
    status = request.GET.get("status", "all")
    tasks_qs = Task.objects.filter(owner=request.user)

    if status == "active":
        tasks_qs = tasks_qs.filter(is_completed=False)
    elif status == "completed":
        tasks_qs = tasks_qs.filter(is_completed=True)

    context = {"tasks": Task.objects.filter(owner=request.user),
               "tasks_today": tasks_qs,
               "current_status": status}
    return render(request, "tasks.html", context)


@login_required
def journal(request):
    today = timezone.localdate()

    if request.method == "POST":
        form = ReflectionForm(request.POST)

        if form.is_valid():
            reflect = form.save(commit=False)
            reflect.owner = request.user
            reflect.date = today
            reflect.save()

            return redirect("dashbord:journal")

    else:
        form = ReflectionForm()

    today_reflections = Reflection.objects.filter(
        owner=request.user,
        date=today
    ).order_by("-id")

    past_entries = Reflection.objects.filter(
        owner=request.user
    ).exclude(
        date=today
    ).order_by("-date", "-id")

    context = {
        "today_reflections": today_reflections,
        "past_entries": past_entries,
        "form": form,
    }

    return render(request, "journal.html", context)


@login_required
def goals(request):

    context = {"goals": Goal.objects.filter(
        owner=request.user,)}
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

    type_filter = request.GET.get("type", "all")

    transactions = month_transactions
    if type_filter == "income":
        transactions = transactions.filter(type="income")
    elif type_filter == "expense":
        transactions = transactions.filter(type="expense")

    context = {
        "finance": {"income": income, "expenses": expenses, "balance": income - expenses},
        "transactions": transactions,
        "current_type": type_filter,
    }
    return render(request, "finance.html", context)


@login_required
def settings(request):
    if request.method == "POST":
        if "profile_submit" in request.POST:
            profile_form = ProfileForm(request.POST, instance=request.user)
            password_form = MomentumPasswordChangeForm(request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Profile updated.")
                return redirect("dashbord:settings")

        elif "preferences_submit" in request.POST:
            profile_form = ProfileForm(instance=request.user)
            password_form = MomentumPasswordChangeForm(request.user)

        elif "password_submit" in request.POST:
            profile_form = ProfileForm(instance=request.user)
            password_form = MomentumPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password changed.")
                return redirect("dashbord:settings")
    else:
        profile_form = ProfileForm(instance=request.user)
        password_form = MomentumPasswordChangeForm(request.user)

    return render(request, "settings.html", {
        "profile_form": profile_form,
        "password_form": password_form,
    })
