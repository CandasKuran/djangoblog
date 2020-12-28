from django.contrib import admin

from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)


@admin.register(Article)                #django da bi class olusturmak icin bu sekilde admin.register(article) yazabiliriz. daha sonra istedigimiz classi olusturabiliriz,
class ArticleAdmin(admin.ModelAdmin):   #adminin icindeki model.admin den turemesini soyluyoruz.
    
    list_display = ["title","author","created_date"]   #list_display ozelligi ile panelde gorunmesini istedigimiz kisimlari ekliyoruz.
    
    list_display_links = ["title","created_date"]     # burda ise uzerine tiklandigimizda makaleyi acmasini istedigimiz ozellikleri ekliyoruz. yani olusutulma tarihine basildigi zaman da makalemize erisim saglanabilecek.
   
    search_fields = ["title"]  #bu ozellik ile makalelerin ust kisminda bir araba cubugu ekliyoruz ve title a gore arama ozelligi ekliyoruz.
   
    list_filter = ["created_date"]  #liste_filter ile makalelerimizin yanina bir suzgec ozelligi ekliyoruz ve makaleleri istedimiz zamana gore arama ozelligi ekliyoruz.
    class Meta:                         #article ile ArticleAdmini baglamak icin django da boyle bir dizi var. tekrar bir class acarak model = Article yaziyoruz.
        model = Article




# ******* django shell kullanimi.********

# C:\Users\admin\Desktop\blog>python manage.py shell => djangodaki shell i yeni terminal acip calisitiriyoruz.
# >>> from django.contrib.auth.models import User    => daha sonra auth modulunu user ile import ediyoruz.
# >>> from article.models import Article
# >>> User
# <class 'django.contrib.auth.models.User'>
# >>> Article
# <class 'article.models.Article'>
# >>> newUser = User(username = "denemekullaci",password = "123")  => bu sekilde yeni kullanici ekleyebiliyoruz ve newUser.save() ile kaydediyoruz.
# >>> newUser
# <User: denemekullaci>
# >>> newUser.save()                                               => bu sekilde data ya kaydediyoruz.
# >>> newUser2 = User(username = "Denemekullanici2")      => ama ustteki yondtemde belirlenen sifre data base de acik gorunuyor. bunu engellemek icin bir alt satirdaki parola sifreleme fonksiyoununu kullaniyoruz.
# >>> newUser2.set_password("123")
# >>> newUser2.save()

#>>> newUser3 = User()                          => bu sekilde ise bos bir user olusturuyour. daha sonra istedigimiz kisimlari bu sekilde dolduruyoruz.
#>>> newUser3.username = "denemekullanici3"    
#>>> newUser3.set_password("123")
#>>> newUser3.first_name = "Mustafa"
#>>> newUser3.save()

# *** article olusturma.

#>>> article = Article(title = "Django Shell Deneme",content = "icerik icerik",author = newUser4)   => bu sekilde bir article olustururarak istedigimiz ozelliklerini ekleyebiliyoruz.
#>>> article.save()

#Article.objects.create(title = "deneme21",content = "21",author = newUser4)  => bu sekilde de article olusturuluyor.

#**** article ozellik degistirme
# article.title = "deneme30 degisti"
# article.save()     => bu sekilde istedigimiz article nin istedigimiz ozelligini degistirip kaydedebiliyoruz.

# Article.objects.all() ile datamizdaki butun articleleri ekranda gosterebiliyoruz.
# Article.objects.get(title = "Deneme2") ile datamizdaki title i "Deneme2" olan article mizi ekrana yazdiriyoruz.


#**** veri silme
# article.delete() ile istedigimiz article yi datamizdan silebiliyoruz.

#**** filtreleme ozelligi
# Article.objects.filter(title__contains = "Den")  => title in icerisinde "Den" gecen article leri almak istedigimizi soyluyoruz.

