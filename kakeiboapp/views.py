from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import KakeiboPostForm, TotalForm, ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import KakeiboPost, Total
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
class IndexView(ListView):
    model = Total
    template_name = 'kakeiboapp/index.html'
    context_object_name = 'latest'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # ログイン済みならユーザーのデータを返す
            return Total.objects.filter(user=self.request.user).order_by('-datetime')[:1]
        else:
            # 未ログインなら空のクエリセットを返す
            return Total.objects.none()

@method_decorator(login_required, name='dispatch')
class AddTotalView(CreateView):
    model = Total
    form_class = TotalForm
    template_name = 'kakeiboapp/addtotal.html'
    success_url = reverse_lazy('kakeiboapp:add_success')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = KakeiboPost
    form_class = KakeiboPostForm
    template_name = 'kakeiboapp/addpost.html'
    success_url = reverse_lazy('kakeiboapp:add_success')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
class AddSuccessView(TemplateView):
    template_name = 'kakeiboapp/add_success.html'
    
@method_decorator(login_required, name='dispatch')
class KakeiboListView(ListView):
    model = KakeiboPost
    template_name = 'kakeiboapp/kakeibo_list.html'
    context_object_name = 'records'
    paginate_by = 4
    
    def get_queryset(self):
        # ユーザーごとの投稿を取得
        return KakeiboPost.objects.filter(user=self.request.user).order_by('-date')

@method_decorator(login_required, name='dispatch')
class CategoryView(ListView):
    template_name = 'kakeiboapp/kakeibo_list.html'
    context_object_name = 'records'
    paginate_by = 4
    
    def  get_queryset(self):
        category = self.kwargs['category']
        return KakeiboPost.objects.filter(category=category, user=self.request.user).order_by('date')
    
class DetailView(DetailView):
    template_name = 'kakeiboapp/detail.html'
    model = KakeiboPost
    context_object_name = 'records'
    
class DeleteView(DeleteView):
    model = KakeiboPost
    template_name = 'kakeiboapp/post_delete.html'
    success_url = reverse_lazy('kakeiboapp:kakeibo_list')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class ContactView(FormView):
    template_name = 'kakeiboapp/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('kakeiboapp:contact')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nタイトル: {2}\nメッセージ: {3}'.format(name, email, title, message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)