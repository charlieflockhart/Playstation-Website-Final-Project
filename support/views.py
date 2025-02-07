from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SupportRequestForm


def about_me(request):
    if request.method == "POST":
        supportRequest_form = SupportRequestForm(data=request.POST)
        if supportRequest_form.is_valid():
            supportRequest_form.save()
            messages.add_message(request, messages.SUCCESS, "Please check your Email Inbox for a response within 3 - 5 working days.")
            return redirect('support')
                   
    """
    Renders the About page
    """
    supportRequest_form = SupportRequestForm()


    return render(
        request,
        "support/support.html",
        {
         "supportRequest_form": supportRequest_form
        },
    )
