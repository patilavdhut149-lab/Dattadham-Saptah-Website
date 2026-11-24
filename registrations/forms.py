from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "full_name",
            "mobile",
            "address",
            "other_service",
            "whatsapp_group"
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "आपले पूर्ण नाव लिहा",
                "autocomplete": "name"
            }),
            "mobile": forms.TextInput(attrs={
                "placeholder": "10 अंकी मोबाईल नंबर",
                "inputmode": "numeric",
                "maxlength": "10"
            }),
            "address": forms.Textarea(attrs={
                "placeholder": "आपला संपूर्ण पत्ता लिहा (घर / गल्ली, गाव, तालुका, जिल्हा, राज्य)",
                "rows": 3
            }),
            "other_service": forms.RadioSelect(),
            "whatsapp_group": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove blank radio options
        for field_name in ["other_service", "whatsapp_group"]:
            field = self.fields[field_name]
            field.required = True
            field.choices = [
                (value, label)
                for value, label in field.choices
                if value not in ("", None)
            ]

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"].strip()

        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError(
                "कृपया योग्य 10 अंकी मोबाईल नंबर टाका."
            )

        return mobile