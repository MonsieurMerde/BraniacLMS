from django.db import migrations


def truncate_func(apps, schema_editor):
    Courses = apps.get_model("mainapp", "Courses")
    id_courses_list = Courses.objects.values_list("id", flat=True)
    for item_id in id_courses_list:
        Courses.objects.update_or_create(
            id=item_id,
            defaults={"description": None},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0007_transfer_courses"),
    ]

    operations = [migrations.RunPython(truncate_func)]
