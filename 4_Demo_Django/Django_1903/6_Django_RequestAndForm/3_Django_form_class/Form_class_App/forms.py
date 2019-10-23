from django import forms
class UserForm(forms.Form):
    username = forms.CharField(label='联系人姓名')
    password = forms.CharField(min_length=6, label='联系人密码')
    email = forms.CharField(max_length=32, label='联系人邮箱')
    phone = forms.CharField(min_length=11, label='联系人电话')




















