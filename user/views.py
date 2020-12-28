from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm
from django.contrib import messages         # django daki messages modulunu dahil ediyourz ve ekrana message yazdirabiliyoruz.
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout       #django daki login modulunu sisteme dahil ediyoruz. newUser imizi login e atayarak kayit olduktan sonra sisteme giris yapmasini saglayacak. , "authenticate" ise datamizda boyle bir kullanici olup olmadigini sorguluyor

# Create your views here.


def register(request):

    form = RegisterForm(request.POST or None)        #bu ise 2. yontem ve kisa olan yontem. burda POST request ise islmeler kayit yapilip devam ediyor.
    if form.is_valid():                                 # eger requestimiz GET ise none devreye giriyor ve context kismi calisiyor .
        username = form.cleaned_data.get("username")   
        password = form.cleaned_data.get("password") 

        newUser = User(username = username)
        newUser.set_password(password)  
            
        newUser.save()                 
        login(request,newUser)    
        messages.success(request,"Basariyla Kayit Oldunuz...")   #burda kayit islemi gerceklestikten sonra ekrana bir succes message i yazdiriyoruz. , bunun olmasi icin msjin gorunmesini istedigimiz yere bir mesaj yazdirma formu ekliyoru. yani layout da navbarincontainer altinda
        return redirect("index")    

    
    context = {                                          
           "form" : form

        }
    return render(request,"register.html",context)





"""  
  if request.method == "POST":      ***kayit ol formu*** 
        form = RegisterForm(request.POST) 
        if form.is_valid():                     #forms.py de yaptigimiz "clean" metodu bu sekilde cagiriyoruz. Parolalari eslesiyor mu eslesmiyor mu sorguluyoruz.
            username = form.cleaned_data.get("username")   
            password = form.cleaned_data.get("password") 

            newUser = User(username = username)
            newUser.set_password(password)  # Bu sekilde alinan parolamizi sifreliyoruz.
            
            newUser.save()                  # bu sekilde artik kullanicimizi datamiza kaydediyoruz.
            login(request,newUser)          # login fonksiyounun ilk parametresi request olmak zorunda. ondan sonra newUser olacak ve yeni kayit olan kullanici direk giris yapacak.
            return redirect("index")               #giris yaptiktan sonra redirect fonksiyonu ile gitmesini istedigimiz url yi giriyoruz.burda gitmesini soyledigimiz "index" ise blog dosyasindaki urls.py de tanimladigimiz ana sayfa ismi
        
        context = {                                     # eger parolalar uyusmuyorsa direk register kismina tekrar donuyor.                   
           "form" : form

        }
        return render(request,"register.html",context)
                                       
    else:
       form = RegisterForm()
       context = {
           "form" : form

       }
       return render(request,"register.html",context) """
   
   
   

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanici Adi veya Parola Hatali!")
            return render(request,"login.html",context)
        else:
            messages.success(request,"Basariyla Giris Yaptiniz.")
            login(request,user)
            return redirect("index")

    return render(request,"login.html",context)

    
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Basariyla Cikis Yaptiniz")
    return redirect("index")