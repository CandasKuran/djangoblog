from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE , verbose_name= "Yazar")  #burda olusturulmus bir clastaki isimleri "verbose_name" ile istenilen dilde kelimeler ekleyebiliyoruz.
    title = models.CharField(max_length=50 , verbose_name= " Baslik")
    content = RichTextField() # ckeditoru modulunden import edip bunu kullaniyoruz.
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Olusturulma Tarihi")
    article_image = models.FileField(blank = True , null = True,verbose_name="Makaleye Fotograf Ekleyin") #  bu alanimiz bos da olabilir dolu daolabilir diye ekliyoruz parantez icerisine


    def __str__(self):          # bu modul ile makale basligini istedigimiz opsiyonu atayabiliyoruz. tittle yaparsak makaleler makale basligi ile gorunecek
        return self.title       # eger author yaparsak da makale yazari gorunecek. bu sekilde istedigimiz sekilde gorunmesini ayarlayabiliriz.

#burda bir tablo classi lousturuyoruz. daha sonra admin.py de "from .models import Article" i ekliyoruz. daha sonra => admin.site.register(Article) yaziyoruz 
# ve admin paneline ekliyoruz. Daha sonra settings.py de INSTALLED_APPS kismina "article" classimizi ekliyoruz.


    class Meta:
        ordering = ['-created_date']    # class meta daki ordering formunu kullanarak makaleleri olusturulma tarihine gore siraliyoruz. daha sonra terminal acip bunu djangoya tanitiyoruz. "makemigrations" ve "migrate"
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments") #burda yaptigimiz foreingkey ise commentimizi istedigimiz articleye bagliyor.
    comment_author = models.CharField(max_length=50,verbose_name="isim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']    

''' 
comment modelini olusturduktan sonra terminal acip bunu django ya tanitmamiz gerekiyor. bunun icin yapacagimiz islemler su sekilde olacak

python manage.py makemigrations

python manage.py migrate => diyoruz cunku veri tabaninda olusturmak istiyoruz.
'''




"""<img class "img-fluid rounded" src="{{article.article_image.url}}" alt="">

article_image = models.FileField(blank = True , null = True,verbose_name="Makaleye Fotograf Ekleyin") #  bu alanimiz bos da olabilir dolu daolabilir diye ekliyoruz parantez icerisine

artik admin panelimizde articlenin altinda commnets kismi olusmus durumda
"""


