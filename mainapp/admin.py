from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


class InputFilter(admin.SimpleListFilter):
    template = "admin/input_filter.html"

    def lookups(self, request, model_admin):
        return ((),)

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice["query_parts"] = (
            (k, v) for k, v in changelist.get_filters_params().items() if k != self.parameter_name
        )
        yield all_choice


class TextInputFilter(InputFilter):
    parameter_name = "text"
    title = _("Text in news title")

    def queryset(self, request, queryset):
        if self.value() is not None:
            text = self.value()
            return queryset.filter(title__contains=text)


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]
    list_filter = [TextInputFilter, "created"]
    date_hierarchy = "created"


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")
