from django.db import models
from accounts.models import CustomUser

# Create your models here.
class KakeiboPost(models.Model):
    CATEGORY = (
        ('給料', '給料'),
        ('お小遣い', 'お小遣い'),
        ('家賃', '家賃'),
        ('水道光熱費', '水道光熱費'),
        ('通信費', '通信費'),
        ('食費', '食費'),
        ('日用品費', '日用品費'),
        ('交際費', '交際費'),
        ('交通費', '交通費'),
        ('教育費', '教育費'),
    )
    
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='日付')
    title = models.CharField(verbose_name='タイトル',max_length=50)
    amount = models.IntegerField(verbose_name='金額')
    comment = models.TextField(verbose_name='コメント')
    category = models.CharField(verbose_name='カテゴリ', max_length=30, choices=CATEGORY)
    
    def __str__(self):
        return self.title
    
class Total(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    bank = models.IntegerField(verbose_name="銀行")
    income = models.IntegerField(verbose_name="収入")
    outcome = models.IntegerField(verbose_name="支出")
    datetime = models.DateTimeField(verbose_name='日時', auto_now=True)