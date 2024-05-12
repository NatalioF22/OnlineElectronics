from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Profile, Categories




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_description', 'product_price', 'product_link', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description', 'rows': 4}),
            'product_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Price'}),
            'product_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Link'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Categories.objects.all()
        self.fields['category'].label = 'Select a Category'
        self.fields['category'].empty_label = 'Choose Category'
          

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), required=False)
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=False)
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=False)
   
    
    profile_image = forms.ImageField(label="Profile Picture",required=False)
    profile_bio = forms.CharField(label="Profile Bio",widget= forms.Textarea(attrs={'class':'form-control','placeholder':'Profile Bio'}),required=False)
    website_link= forms.CharField(label="Website Link",widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Website Link'}),required=False)
    facebook_link = forms.CharField(label="Facebook link",widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook link'}),required=False)
    instagram_link = forms.CharField(label="Instagram link",widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Instagram link'}),required=False)
    linkedIn_link = forms.CharField(label="LinkedIn link",widget= forms.TextInput(attrs={'class':'form-control','placeholder':'LinkedIn link'}),required=False)
    
    
    class Meta:
        model = Profile
        fields = ['email','first_name','last_name','profile_image', 'profile_bio', 'website_link', 'facebook_link', 'instagram_link', 'linkedIn_link']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), required=False)
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=False)
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=False)
   
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    
   
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
       
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Your User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = "<span class='form-text text-muted'><small>Required. 150 characters or fewer. Letters, digits, and symbols.</small></span>"
       
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = "<span class='form-text text-muted'><small>Your password must be at least 8 characters long. It must contain at least 2 digits, 2 letters, and 2 symbols.</small></span>"
       
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = "<span class='form-text text-muted'><small>Enter the same password as above.</small></span>"
        
    def clean_username(self):
        username = self.cleaned_data['username']
        current_user = self.instance
        if User.objects.exclude(pk=current_user.pk).filter(username=username).exists():
            raise forms.ValidationError("A user with this username already exists.")
        return username


class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        required=False,
        label='Select a Category',
        empty_label='All Categories'
    )