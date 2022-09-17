from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


# Create your views here.
def registration(request):
    if request.method == "POST":
        form = CustomerRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_student = True
            user.staff = False
            user.admin = False
            user.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = CustomerRegForm()
    return render(request=request, template_name="registration/registration.html", context={"register_form": form})