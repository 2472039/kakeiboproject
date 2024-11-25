from django import forms
from .models import KakeiboPost, Total

class KakeiboPostForm(forms.ModelForm):
    class Meta:
        model = KakeiboPost
        fields = ['date', 'title', 'amount', 'comment', 'category']
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
class TotalForm(forms.ModelForm):
    class Meta:
        model = Total
        fields = ['bank', 'income', 'outcome']
                
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', widget=forms.Textarea(attrs={'cols':'30', 'rows':'1'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.Textarea(attrs={'cols':'30', 'rows':'1'}))
    title = forms.CharField(label='件名', widget=forms.Textarea(attrs={'cols':'30', 'rows':'1'}))
    message = forms.CharField(label='メッセージ', widget=forms.Textarea(attrs={'cols': '70', 'rows': '15'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'