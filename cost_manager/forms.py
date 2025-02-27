from django import forms
from .models import PurchaseItem

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['name', 'price', 'quantity', 'purchase_link', 'status', 'purchase_date']