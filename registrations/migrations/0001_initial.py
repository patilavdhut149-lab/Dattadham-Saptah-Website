# Generated initial migration
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150, verbose_name="सेवेकऱ्याचे पूर्ण नाव")),
                ("mobile", models.CharField(db_index=True, max_length=10, verbose_name="मोबाईल नंबर")),
                ("address", models.TextField(verbose_name="पूर्ण पत्ता")),
                ("other_service", models.CharField(choices=[("प्रहर", "प्रहर"), ("याग", "याग"), ("दोन्ही", "दोन्ही")], max_length=20, verbose_name="पारायण व्यतिरिक्त सेवा")),
                ("whatsapp_group", models.CharField(choices=[("होय", "होय"), ("नाही", "नाही")], max_length=5, verbose_name="अधिकृत WhatsApp Group")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="नोंदणी तारीख")),
            ],
            options={"verbose_name": "सेवेकरी नोंदणी", "verbose_name_plural": "सेवेकरी नोंदणी", "ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="SiteContent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=80, unique=True)),
                ("value", models.TextField(blank=True)),
            ],
            options={"verbose_name": "वेबसाइट मजकूर", "verbose_name_plural": "वेबसाइट मजकूर"},
        ),
        migrations.CreateModel(
            name="ProgramItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("section", models.CharField(max_length=100, verbose_name="विभाग")),
                ("title", models.CharField(max_length=180, verbose_name="शीर्षक / वेळ")),
                ("description", models.TextField(blank=True, verbose_name="माहिती")),
                ("sort_order", models.PositiveIntegerField(default=0, verbose_name="क्रम")),
            ],
            options={"verbose_name": "कार्यक्रम", "verbose_name_plural": "कार्यक्रम", "ordering": ["sort_order", "id"]},
        ),
    ]
