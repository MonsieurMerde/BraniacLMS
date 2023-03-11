from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0005_data_teachers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interim_model",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.TextField(verbose_name="Description", blank=True, null=True)),
            ],
        ),
    ]
