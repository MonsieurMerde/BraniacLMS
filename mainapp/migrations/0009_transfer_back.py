from django.db import migrations


def transfer_back_func(apps, schema_editor):
    Courses = apps.get_model("mainapp", "Courses")
    Interim_courses = apps.get_model("mainapp", "Interim_model")
    id_courses_list = Interim_courses.objects.values_list("id", flat=True)
    description_courses_list = Interim_courses.objects.values_list("description", flat=True)
    for item_id, item_description in zip(id_courses_list, description_courses_list):
        Courses.objects.update_or_create(
            id=item_id,
            defaults={"description": item_description},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0008_truncate_courses"),
    ]

    operations = [
        migrations.RunPython(transfer_back_func),
    ]
