from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages 
from django.contrib.auth.decorators import login_required  #giris kontrolu. giris yapilip yapilmadigini kontrol eder.(16.satir)
# Create your views here.

def articles(request):
     keyword = request.GET.get("keyword")   #eger bir arama yapildiysa 

     if keyword:
          articles = Article.objects.filter(title__contains = keyword) #keywordun gectigi title lari cagiriyoruz.
          return render(request,"articles.html",{"articles":articles})
          
     articles = Article.objects.all()

     return render(request,"articles.html",{"articles":articles})  # articles articles anahtar kelimesi ile gondermek istiyoruz. onun icin {"articles = articles "} yapiyoruz.
def index(request):   #her  views de en basta bulunmasi gereken bir parametre. requesti daha sonra post veya get requestleri kullanacagiz.
     return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url= "user:login")   #bunu ekledigimiz zaman giris yapmayan kullanicilarin dashboard a erismesini engelliyoruz.
def dashboard(request):
     articles = Article.objects.filter(author = request.user)   # burda yazdigimiz parametre ile konrol panelinde filtreleme yapiyoruz ve yazari kullanici olan makaleleri yazdiriyoruz.
     context = {
          "articles":articles

     }
     return render(request,"dashboard.html",context)


@login_required(login_url= "user:login") #eger giris yapilmadiysa userin altindaki login sayfasina gitmesini soyluyoruz.
def addarticle(request):
     form = ArticleForm(request.POST or None,request.FILES or None)

     if form.is_valid():
          article = form.save(commit=False)               #burda commit=False diyoruz cunku makaleyi bizim manuel olarak kayit yapacagimizi soyluyoruz.
          
          article.author = request.user
          article.save()

          messages.success(request,"Makale Basariyla Olusturuldu")
          return redirect("article:dashboard")

     return render(request,"addarticle.html",{"form":form})


def detail(request,id):
    #article = Article.objects.filter(id=id).first()     #=> hata firlatmak icin bunu iptal edip altina bu satiri ekliyoruz.
    article = get_object_or_404(Article,id=id)                #id si istenen article yi yazdir. eger yoksa get_list_or_404 ile ekrana hata firlatiyoruz.

    comments = article.comments.all()    # burda detay sayfamizda makalemizle ilgiili butun yorumlari almamizi siyluyoruz.
    return render(request,"detail.html",{"article":article,"comments":comments}) 




@login_required(login_url= "user:login")
def updateArticle(request,id):
     article = get_object_or_404(Article,id=id)
     form = ArticleForm(request.POST or None,request.FILES or None,instance = article)   #istenilen makale icerigini yazdir diyoruz.
     if form.is_valid():
          article = form.save(commit=False)               #burda commit=False diyoruz cunku makaleyi bizim manuel olarak kayit yapacagimizi soyluyoruz.
          
          article.author = request.user
          article.save()

          messages.success(request,"Makale Basariyla Guncellendi")
          return redirect("article:dashboard")

     return render(request,"update.html",{"form":form})

@login_required(login_url= "user:login")
def deleteArticle(request,id):
     article = get_object_or_404(Article,id=id)  
     article.delete()

     messages.success(request,"Makale Basariyla Silindi")

     return redirect("article:dashboard")  #bu sekilde article nin altindaki dashboard a gitmesini soyluyoruz.


def addComment(request,id):
    article = get_object_or_404(Article,id = id )

    if request.method == "POST":
         comment_author = request.POST.get("comment_author")
         comment_content = request.POST.get("comment_content")

         newComment = Comment(comment_author = comment_author, comment_content= comment_content)

         newComment.article = article

         newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))

    #/articles/detail/15 ekledigimiz reverse fonksiyonu ile bi ust satirdaki redirect url sini bu sekilde duzenleyebiliyoruz.