
from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration

        fields = [
            "full_name",
            "gender",
            "parayan",
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

            "gender": forms.RadioSelect(),

            "parayan": forms.RadioSelect(),

            "mobile": forms.TextInput(attrs={
                "placeholder": "10 अंकी मोबाईल नंबर",
                "inputmode": "numeric",
                "maxlength": "10"
            }),

            "address": forms.Textarea(attrs={
                "placeholder": "आपल्या गावाचे नाव लिहा",
                "rows": 3
            }),

            "other_service": forms.RadioSelect(),

            "whatsapp_group": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # सर्व Radio Fields मधील Blank Options काढणे
        radio_fields = [
            "gender",
            "parayan",
            "other_service",
            "whatsapp_group"
        ]

        for field_name in radio_fields:
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
