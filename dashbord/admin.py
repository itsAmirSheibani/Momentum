from django.contrib import admin

from .models import Task, MoodEntry, Reflection, Goal, Transaction


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
    list_display = ("owner", "date", "content")
    list_filter = ("date",)
    search_fields = ("content",)
    date_hierarchy = "date"

    def short_content(self, obj):
        return (obj.content[:60] + "…") if len(obj.content) > 60 else obj.content
    short_content.short_description = "Content"


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "progress", "target_date")
    list_filter = ("progress",)
    search_fields = ("title",)
    list_editable = ("progress",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("description", "owner", "type", "amount", "date")
    list_filter = ("type", "date")
    search_fields = ("description",)
    date_hierarchy = "date"
