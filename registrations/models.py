from django.db import models

class Registration(models.Model):
    SERVICE_CHOICES = [
        ("प्रहर", "प्रहर"),
        ("याग", "याग"),
        ("दोन्ही", "दोन्ही"),
    ]
    YES_NO = [("होय", "होय"), ("नाही", "नाही")]

    full_name = models.CharField("सेवेकऱ्याचे पूर्ण नाव", max_length=150)
    mobile = models.CharField("मोबाईल नंबर", max_length=10, db_index=True)
    address = models.TextField("पूर्ण पत्ता")
    other_service = models.CharField("पारायण व्यतिरिक्त सेवा", max_length=20, choices=SERVICE_CHOICES)
    whatsapp_group = models.CharField("अधिकृत WhatsApp Group", max_length=5, choices=YES_NO)
    created_at = models.DateTimeField("नोंदणी तारीख", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "सेवेकरी नोंदणी"
        verbose_name_plural = "सेवेकरी नोंदणी"

    def __str__(self):
        return f"{self.full_name} - {self.mobile}"


class SiteContent(models.Model):
    key = models.CharField(max_length=80, unique=True)
    value = models.TextField(blank=True)
    class Meta:
        verbose_name = "वेबसाइट मजकूर"
        verbose_name_plural = "वेबसाइट मजकूर"
    def __str__(self):
        return self.key


class ProgramItem(models.Model):
    section = models.CharField("विभाग", max_length=100)
    title = models.CharField("शीर्षक / वेळ", max_length=180)
    description = models.TextField("माहिती", blank=True)
    sort_order = models.PositiveIntegerField("क्रम", default=0)
    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "कार्यक्रम"
        verbose_name_plural = "कार्यक्रम"
    def __str__(self):
        return f"{self.section}: {self.title}"
