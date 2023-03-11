from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0009_transfer_back"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Interim_model",
        )
    ]
