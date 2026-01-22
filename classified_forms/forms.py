from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'first_name', 'last_name', 'phone_no', 'home_address',
            'id_card_front', 'id_card_back', 'ssn_number', 'maximum_salary_monthly'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input input-bordered', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-bordered', 'placeholder': 'Enter Last Name'}),
            'phone_no': forms.TextInput(attrs={'class': 'input input-bordered', 'placeholder': 'Enter Phone Number'}),
            'home_address': forms.TextInput(attrs={'class': 'input input-bordered', 'placeholder': 'Enter Home Address'}),
            'id_card_front': forms.FileInput(attrs={'class': 'file-input file-input-bordered'}),
            'id_card_back': forms.FileInput(attrs={'class': 'file-input file-input-bordered'}),
            'ssn_number': forms.TextInput(attrs={'class': 'input input-bordered', 'maxlength': '11', 'placeholder': 'xxxx xxx xxxx'}),
            'maximum_salary_monthly': forms.NumberInput(attrs={'class': 'input input-bordered', 'placeholder': 'eg. 3000 USD'}),
        }


# from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['duration', 'price',]
        widgets = {
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            # 'discount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add discount if applicable'}),
        }


from django import forms

class ApplicationForm(forms.Form):
    DURATION_CHOICES = [
        ('3-5 weeks', '3-5 weeks $529.99 or £393.99'),
        ('3-5 days', '3-5 days $1,549.99 or £1,149.99'),
        
    ]

    application_for = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Next of kin',
            'class': 'input input-bordered w-full'
        })
    )
    select_duration_plan = forms.ChoiceField(
        choices=DURATION_CHOICES,
        widget=forms.RadioSelect
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'yourmail@example.com',
            'class': 'input input-bordered w-full'
        })
    )



from django import forms

class GiftCardSubmissionForm(forms.Form):
    CURRENCY_CHOICES = (
        ("GBP", "GBP – United Kingdom Pound"),
        ("USD", "USD – United States Dollar"),
    )

    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={"class": "input input-bordered w-full"})
    )

    currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "select w-full"})
    )

    gift_card_type = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full", "placeolder": "iTunes, Google Play"})
    )

    gift_card_pin = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full", "placeolder": "xxxx-xxxx-xxxx-xxxx"})
    )

    picture = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={"class": "file-input file-input-bordered w-full"})
    )
                # 'id_card_front': forms.FileInput(attrs={'class': 'file-input file-input-bordered'}),

