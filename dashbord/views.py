from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# وقتی مدل‌ها رو نوشتی، اینا رو هم اضافه کن (فقط چیزی که واقعاً استفاده می‌کنی):
# from django.utils import timezone
# from django.db.models import Sum
# from .models import Task, MoodEntry, Reflection, Habit, HabitLog, Goal, Transaction

# راهنمای کلی:
# هر تابع یه HttpRequest می‌گیره و باید render(request, "template_name.html", context)
# برگردونه. همه‌شون @login_required دارن چون داشبورد شخصیه — بدون این دکوریتور
# هر کسی حتی بدون لاگین می‌تونه صفحه رو ببینه (با دیتای خالی چون request.user
# آنانیمس می‌شه).
#
# مهم: تا وقتی خودت تو تمپلیت‌ها {{ }} و {% for %} اضافه نکردی، context لازم
# نیست — همون render(request, "template.html") بدون آرگومان سوم کافیه. وقتی
# تمپلیت آماده شد، context رو طبق راهنمای هر تابع اضافه کن.


@login_required
def dashboard(request):
    """صفحه‌ی اصلی. باید این‌ها رو تو context بفرستی (اسم کلیدها رو دقیقاً
    همین‌جوری نگه دار، چون تمپلیت با همین اسم‌ها کار می‌کنه):

    TODO:
    - today                -> timezone.localdate()
    - tasks_today           -> Task.objects.filter(owner=request.user, due_date=today)
    - timed_tasks_today      -> همون بالایی + .exclude(due_time__isnull=True).order_by("due_time")
                                (برای تایم‌لاین)
    - tasks_today_count      -> tasks_today.count()
    - today_mood, today_energy -> از MoodEntry.objects.filter(owner=..., date=today).first()
                                  بگیر (اگه None بود یعنی هنوز مود امروز ثبت نشده)
    - today_reflection       -> Reflection.objects.filter(owner=..., date=today).first()
    - stats                  -> دیکشنری با completed و remaining
                                (از تعداد تسک‌های تیک‌خورده/نخورده‌ی امروز)
    - goals                  -> Goal.objects.filter(owner=..., is_archived=False)[:3]
                                (فقط ۳ تا برای کارت داشبورد، نه همه)
    """
    return render(request, "dashboard.html")


@login_required
def tasks(request):
    """صفحه‌ی کامل Tasks — همه‌ی تسک‌های کاربر، نه فقط امروز.

    TODO:
    - context باید یه کلید "tasks" داشته باشه که همه‌ی
      Task.objects.filter(owner=request.user) رو برگردونه (بدون فیلتر تاریخ).
    - اگه خواستی فیلتر All/Active/Completed تو صفحه (که الان فقط ظاهریه) رو
      واقعی کنی، یه query param بگیر (مثلاً ?status=completed) و queryset رو
      بر همون اساس فیلتر کن.
    """
    return render(request, "tasks.html")


@login_required
def journal(request):
    """صفحه‌ی Journal — ورودی امروز برای نوشتن، و لیست ورودی‌های قبلی.

    TODO:
    - today_reflection -> Reflection امروز (برای پرکردن textarea بالای صفحه)
    - past_entries      -> Reflection.objects.filter(owner=request.user)
                            .exclude(date=today) — همه‌ی روزهای قبل
    """
    return render(request, "journal.html")


@login_required
def habits(request):
    """صفحه‌ی Habits.

    TODO:
    - context یه کلید "habits" باید داشته باشه:
      Habit.objects.filter(owner=request.user, is_archived=False)
    - برای هر Habit تو تمپلیت، باید بتونی استریک و وضعیت ۷ روز اخیر رو نشون
      بدی. این‌ها تو دیتابیس ذخیره نشدن، پس یا:
        (الف) یه property/متد رو مدل Habit بنویس (مثلاً current_streak) که از
              روی HabitLog محاسبه کنه، و تو تمپلیت صداش کن، یا
        (ب) تو همین ویو، برای هر habit یه لیست از ۷ تا HabitLog اخیر بساز و
            به‌عنوان دیکشنری اضافه‌ای تو context بفرست.
      روش (الف) تمیزتره چون منطق تو مدل می‌مونه، نه ویو.
    """
    return render(request, "habits.html")


@login_required
def goals(request):
    """صفحه‌ی کامل Goals (نه فقط ۳ تای بالا مثل داشبورد).

    TODO:
    - context: "goals" -> Goal.objects.filter(owner=request.user, is_archived=False)
    """
    return render(request, "goals.html")


@login_required
def finance(request):
    """صفحه‌ی Finance — جمع ماه جاری + لیست تراکنش‌ها.

    TODO:
    - today                -> timezone.localdate()
    - month_transactions    -> Transaction.objects.filter(owner=request.user,
                                date__year=today.year, date__month=today.month)
    - income, expenses      -> با .filter(type="income"/"expense")
                                .aggregate(total=Sum("amount"))["total"] or 0
                                (or 0 لازمه چون اگه هیچ تراکنشی نباشه، aggregate
                                None برمی‌گردونه نه صفر)
    - context: "finance" -> دیکشنری {"income":..., "expenses":..., "balance": income-expenses}
    - context: "transactions" -> خود month_transactions (برای لیست پایین صفحه)
    """
    return render(request, "finance.html")


@login_required
def settings(request):
    """صفحه‌ی Settings.

    TODO:
    - این صفحه بیشتر با request.user مستقیم کار می‌کنه (username, first_name,
      email)، نه یکی از مدل‌های خودت — پس context خاصی لازم نداره، مقادیر رو
      مستقیم تو تمپلیت از {{ user.username }} و مشابه بگیر.
    - برای بخش "Update password"، به‌جای دستی چک‌کردن پسورد، از فرم آماده‌ی
      جنگو استفاده کن: django.contrib.auth.forms.PasswordChangeForm
      بعد از form.save() هم حتماً
      django.contrib.auth.update_session_auth_hash(request, user) رو صدا بزن،
      وگرنه کاربر بعد از عوض کردن پسورد خودش از سشن پرت می‌شه بیرون.
    - برای دکمه‌ی "Log out"، از django.contrib.auth.views.LogoutView یا
      django.contrib.auth.logout(request) استفاده کن — نیازی نیست خودت
      منطق حذف سشن رو بنویسی.
    """
    return render(request, "settings.html")
