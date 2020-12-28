from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:                                         
        model = Article
        fields = ["title","content","article_image"]    #models.py de ki hazir bir modelden bir form aliyoruz. bu sekilde yeni bir form olustururarak imput alani olusturuyoruz.





#https://docs.djangoproject.com/fr/2.2/topics/forms/modelforms/