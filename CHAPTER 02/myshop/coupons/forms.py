from django import forms
from . import models

class CouponApplyForm(forms.Form):
    code=forms.CharField()
    