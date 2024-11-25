from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    # サインアップページのビュー
    # forms.py で定義したフォームのクラス
    form_class = SignUpForm
    # レンダリングするテンプレート
    template_name = 'accounts/signup.html'
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')
    
    def form_valid(self, form):
        '''
        CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているCustomUserCreationFormオブジェクト
            Return:
                HttpResponseRedirectオブジェクト:
                    スーパークラスのform_valid()の戻り値を返すことで、
                    success_urlで設定されているURLにリダイレクトさせる
        '''
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    #　サインアップ完了ページのビュー
    # レンダリングするテンプレート
    template_name = 'accounts/signup_success.html'
    
class LogoutSuccessView(TemplateView):
    template_name = 'accounts/logout_success.html'