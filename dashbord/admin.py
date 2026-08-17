from django.contrib import admin

from .models import Task, MoodEntry, Reflection, Habit, HabitLog, Goal, Transaction


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "priority", "category",
                    "due_date", "due_time", "is_completed")
    list_filter = ("priority", "is_completed", "category", "due_date")
    search_fields = ("title", "description")
    date_hierarchy = "due_date"
    


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ("owner", "date", "mood", "energy")
    list_filter = ("mood", "date")
    date_hierarchy = "date"


@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = ("owner", "date", "short_content")
    list_filter = ("date",)
    search_fields = ("content",)
    date_hierarchy = "date"

    def short_content(self, obj):
        return (obj.content[:60] + "…") if len(obj.content) > 60 else obj.content
    short_content.short_description = "Content"


class HabitLogInline(admin.TabularInline):
    model = HabitLog
    extra = 1


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "frequency",
                    "target_per_week", )
    list_filter = ("frequency",)
    search_fields = ("name",)
    inlines = [HabitLogInline]


@admin.register(HabitLog)
class HabitLogAdmin(admin.ModelAdmin):
    list_display = ("habit", "date", "completed")
    list_filter = ("completed", "date")
    date_hierarchy = "date"


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "progress", "target_date", "is_archived")
    list_filter = ("is_archived",)
    search_fields = ("title",)
    list_editable = ("progress",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("description", "owner", "type", "amount", "date")
    list_filter = ("type", "date")
    search_fields = ("description",)
    date_hierarchy = "date"
