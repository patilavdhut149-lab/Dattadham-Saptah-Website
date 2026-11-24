from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .forms import RegistrationForm
from .models import Registration, SiteContent, ProgramItem

def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = RegistrationForm()
    content = {item.key: item.value for item in SiteContent.objects.all()}
    week_days = [
        ("बुधवार – १६ डिसेंबर २०२६", "ग्रामदेवता सन्मान, मंडल मांडणी"),
        ("गुरुवार – १७ डिसेंबर २०२६", "मंडल स्थापना, अग्नि स्थापना, स्थापित देवता हवन"),
        ("शुक्रवार – १८ डिसेंबर २०२६", "नित्यस्वाहाकार श्री गणेश याग व श्री मनोबोध याग"),
        ("शनिवार – १९ डिसेंबर २०२६", "नित्यस्वाहाकार, स्वामी याग"),
        ("रविवार – २० डिसेंबर २०२६", "नित्यस्वाहाकार, गीताई याग"),
        ("सोमवार – २१ डिसेंबर २०२६", "नित्यस्वाहाकार, चंडी याग"),
        ("मंगळवार – २२ डिसेंबर २०२६", "नित्यस्वाहाकार, श्री रुद्र याग / मल्हारी याग"),
        ("बुधवार – २३ डिसेंबर २०२६", "नित्यस्वाहाकार, बली – पूर्णाहुती. दुपारी १२:१३ वा. श्रीदत्त जन्मोत्सव"),
        ("गुरुवार – २४ डिसेंबर २०२६", "श्री सत्यदत्त पूजन, देवता विसर्जन. अखंड नाम जप – यज्ञ सप्ताह सांगता"),
    ]
    daily_items = [
        ("सकाळी ७:३० ते ८:००", "औंदुंबर प्रदक्षिणा"),
        ("सकाळी ८:००", "भूपाळी आरती. भूपाळी आरती संपन्न होईल."),
        ("सकाळी ८:३० ते १०:३०", "माईकवरून सामुदायिक श्री गुरुचरित्र वाचन. त्यावेळी यज्ञमंडपात प्रतिनिधिक स्वरूपात सेवेकऱ्यांकडून नित्य स्वाहाकार."),
        ("सकाळी १०:३०", "नैवेद्य आरती. सकाळच्या तीन आरत्या, मंत्र पुष्पांजली व प्रार्थना."),
        ("सकाळी १०:३० ते दुपारी १२:३०", "विशेष याग. दिवसानुरूप विशेष याग संपन्न होतील."),
        ("संध्याकाळी ६:३०", "नैवेद्य आरती. संध्याकाळच्या सर्व आरत्या मंत्र पुष्पांजलीसह."),
        ("संध्याकाळी ६:५०", "नित्यध्यान व सामुदायिक वाचन: नित्यध्यान, गीताई, श्री मनाचे श्लोक, गीतेचा १५ वा अध्याय, श्री तुकारामांचा अभंग, पसायदान, श्री विष्णुसहस्रनाम वाचन, श्री स्वामी समर्थ मंत्र जप एक माळ. त्यानंतर ऐच्छिक श्री स्वामी चरित्र किंवा दुर्गा सप्तशती सामुदायिक वाचन करावे."),
    ]
    return render(request, "registrations/home.html", {"form": form, "content": content, "week_days": week_days, "daily_items": daily_items})

def success(request):
    return render(request, "registrations/success.html")

def admin_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and user.is_staff:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Username किंवा Password चुकीचा आहे किंवा Admin परवानगी नाही.")
    return render(request, "registrations/login.html")

def admin_logout(request):
    logout(request)
    return redirect("home")

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    q = request.GET.get("q", "").strip()
    registrations = Registration.objects.all()
    if q:
        registrations = registrations.filter(Q(full_name__icontains=q) | Q(mobile__icontains=q))
    return render(request, "registrations/dashboard.html", {
        "registrations": registrations,
        "total": Registration.objects.count(),
        "q": q,
    })

@login_required
@user_passes_test(lambda u: u.is_staff)
def registration_detail(request, pk):
    item = get_object_or_404(Registration, pk=pk)
    return render(request, "registrations/detail.html", {"item": item})

@login_required
@user_passes_test(lambda u: u.is_staff)
def registration_edit(request, pk):
    item = get_object_or_404(Registration, pk=pk)
    form = RegistrationForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "नोंदणी अपडेट झाली.")
        return redirect("dashboard")
    return render(request, "registrations/edit.html", {"form": form, "item": item})

@login_required
@user_passes_test(lambda u: u.is_staff)
def registration_delete(request, pk):
    item = get_object_or_404(Registration, pk=pk)
    if request.method == "POST":
        item.delete()
        messages.success(request, "नोंदणी Delete झाली.")
        return redirect("dashboard")
    return render(request, "registrations/delete.html", {"item": item})

@login_required
@user_passes_test(lambda u: u.is_staff)
def export_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Registrations"
    ws.append(["पूर्ण नाव", "मोबाईल", "पत्ता", "इतर सेवा", "WhatsApp Group", "नोंदणी तारीख"])
    for r in Registration.objects.all():
        ws.append([r.full_name, r.mobile, r.address, r.other_service, r.whatsapp_group, timezone.localtime(r.created_at).strftime("%d-%m-%Y %H:%M")])
    for col in ws.columns:
        letter = col[0].column_letter
        ws.column_dimensions[letter].width = min(max(max(len(str(c.value or "")) for c in col) + 2, 14), 42)
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="sevakari_registrations.xlsx"'
    wb.save(response)
    return response

@login_required
@user_passes_test(lambda u: u.is_staff)
def export_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="sevakari_registrations.pdf"'
    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=18, leftMargin=18, topMargin=20, bottomMargin=20)
    styles = getSampleStyleSheet()
    story = [Paragraph("Sevakari Registration List", styles["Title"]), Spacer(1, 12)]
    data = [["Name", "Mobile", "Address", "Service", "WhatsApp", "Registered"]]
    for r in Registration.objects.all():
        data.append([r.full_name, r.mobile, r.address[:90], r.other_service, r.whatsapp_group, timezone.localtime(r.created_at).strftime("%d-%m-%Y")])
    table = Table(data, repeatRows=1, colWidths=[115, 75, 220, 65, 65, 75])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e58a16")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#d9c9a5")),
        ("FONTSIZE", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#fff8ed")]),
    ]))
    story.append(table)
    doc.build(story)
    return response
