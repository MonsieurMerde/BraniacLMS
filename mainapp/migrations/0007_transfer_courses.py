from django.db import migrations


def transfer_func(apps, schema_editor):
    Courses = apps.get_model("mainapp", "Courses")
    Interim_courses = apps.get_model("mainapp", "Interim_model")
    id_courses_list = Courses.objects.values_list("id", flat=True)
    description_courses_list = Courses.objects.values_list("description", flat=True)
    for item_id, item_description in zip(id_courses_list, description_courses_list):
        Interim_courses.objects.create(id=item_id, description=item_description)


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0006_create_interim_model"),
    ]

    operations = [
        migrations.RunPython(transfer_func),
    ]
