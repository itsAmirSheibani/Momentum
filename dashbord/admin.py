from django.contrib import admin

# وقتی مدل‌ها رو تو models.py نوشتی، این import رو کامل کن:
# from .models import Task, MoodEntry, Reflection, Habit, HabitLog, Goal, Transaction

# راهنمای کلی:
# برای هر مدل یه کلاس ادمین با دکوریتور @admin.register(ModelName) بساز.
# سه‌تا attribute اصلی هر ModelAdmin:
#   list_display  -> کدوم فیلدها به‌عنوان ستون تو لیست نشون داده بشن (tuple از اسم فیلدها)
#   list_filter   -> کدوم فیلدها به‌عنوان فیلتر کنار صفحه ظاهر بشن (معمولاً فیلدهای
#                    choices یا boolean یا date، نه متن آزاد)
#   search_fields -> کدوم فیلدهای متنی قابل جستجو باشن (تو باکس سرچ بالای صفحه)


# TODO: TaskAdmin
# list_display پیشنهادی: title, owner, priority, category, due_date, due_time, is_completed
# list_filter پیشنهادی: priority, is_completed, category, due_date
# search_fields پیشنهادی: title, description
# اضافه‌ها:
#   - date_hierarchy = "due_date"   (یه ناوبری تاریخ بالای صفحه اضافه می‌کنه)
#   - list_editable = ("is_completed",)  (این فیلد مستقیم تو خود لیست قابل تغییره،
#     ولی نکته: هر فیلدی تو list_editable باشه نباید اولین ستون تو list_display باشه)


# TODO: MoodEntryAdmin
# list_display: owner, date, mood, energy
# list_filter: mood, date
# date_hierarchy: "date"


# TODO: ReflectionAdmin
# list_display: owner, date, و یه متد کمکی مثلاً short_content که content رو
#   کوتاه‌شده (مثلاً ۶۰ کاراکتر اول + "…") نشون بده — چون TextField طولانی تو
#   جدول لیست زشت می‌شه. برای همچین متدی، تو کلاس ادمین یه تابع معمولی بنویس که
#   obj رو می‌گیره و رشته برمی‌گردونه، بعد اسمش رو تو list_display بذار.
# search_fields: content
# date_hierarchy: "date"


# TODO: HabitAdmin
# list_display: name, owner, frequency, target_per_week, is_archived
# list_filter: frequency, is_archived
# search_fields: name
# اختیاری ولی توصیه‌شده: یه HabitLogInline بساز (کلاسی که از admin.TabularInline
#   ارث می‌بره، model = HabitLog, extra = 1) و تو HabitAdmin با
#   inlines = [HabitLogInline] وصلش کن — این‌طوری وقتی یه Habit رو تو ادمین باز
#   می‌کنی، لاگ‌های روزانه‌ش هم همون‌جا زیرش قابل مدیریت‌ان.


# TODO: HabitLogAdmin
# list_display: habit, date, completed
# list_filter: completed, date
# date_hierarchy: "date"


# TODO: GoalAdmin
# list_display: title, owner, progress, target_date, is_archived
# list_filter: is_archived
# search_fields: title
# list_editable = ("progress",)


# TODO: TransactionAdmin
# list_display: description, owner, type, amount, date
# list_filter: type, date
# search_fields: description
# date_hierarchy: "date"


# یادت نباشه: برای اینکه پنل ادمین اصلاً قابل لاگین باشه باید یه سوپریوزر بسازی:
#   python manage.py createsuperuser
