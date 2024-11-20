# # forms.py

# from django import forms
# from .models import Product, Size

# class ProductForm(forms.ModelForm):
#     # Multiple selection for sizes
#     sizes = forms.ModelMultipleChoiceField(
#         queryset=Size.objects.all(),
#         widget=forms.CheckboxSelectMultiple,  # Or you could use SelectMultiple for a dropdown
#         required=True
#     )

#     class Meta:
#         model = Product
#         fields = ['name', 'category', 'image', 'description', 'sizes', 'colors', 'original_price', 'discounted_price']



