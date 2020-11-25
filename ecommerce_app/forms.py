from django import forms
from .models import *


class CartForm(forms.Form):
    quantity = forms.IntegerField(initial='1')
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CartForm, self).__init__(*args, **kwargs)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('paid','shippig_cost',)

        name = forms.CharField(
            label = 'Name',
            max_length = 1000,
            required = True,
            widget = forms.TextInput(
                attrs = {'class': 'sizefull s-text7 p-l-22 p-r-22'}
            )
        ) 

        email = forms.CharField(
            label = 'Email',
            max_length = 1000,
            required = True,
            widget = forms.TextInput(
                attrs = {'class': 'sizefull s-text7 p-l-22 p-r-22'}
            )
        ) 

        phone = forms.CharField(
            label = 'Phone',
            max_length = 1000,
            required = True,
            widget = forms.TextInput(
                attrs = {'class': 'sizefull s-text7 p-l-22 p-r-22'}
            )
        ) 

        city = forms.CharField(
            label = 'City',
            max_length = 1000,
            required = True,
            widget = forms.TextInput(
                attrs = {'class': ' bo4 of-hidden size15 m-b-20 sizefull s-text7 p-l-22 p-r-22'}
            )
        ) 

        address = forms.CharField(
            label = 'Address',
            max_length = 1000,
            required = True,
            widget = forms.Textarea(
                attrs = {'class': 'dis-block s-text7 size20 bo4 p-l-22 p-r-22 p-t-13 m-b-20','row': 5, 'col': 8}
            )
        ) 
        # widgets = {
        #     'name' : forms.TextInput(
        #     attrs = {'class': 'sizefull s-text7 p-l-22 p-r-22'}
        # ),
        #     'address': forms.Textarea(attrs={'row': 5, 'col': 8}),

        # }