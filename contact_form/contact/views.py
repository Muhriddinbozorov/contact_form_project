from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("message_list")
    
    else:
        form = ContactForm()
        return render(request, "contact/home.html", {"form":form})


def message_list(request):
    messages = ContactMessage.objects.all().order_by("-created_at")
    
    return render(request, "contact/message_list.html", {"messages": messages})