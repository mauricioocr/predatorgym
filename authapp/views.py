from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contacto, Membresia, Entrenadore, Usuario,Asistencia
# Create your views here.
def Home(request):
    return render(request,"index.html")

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Por favor inicie sesion e intente de nuevo")
        return redirect('/login')
    user=request.user
    posts=Usuario.objects.filter(Email=user.email)
    attendance=Asistencia.objects.filter(Usuario=user.username)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)  

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)<10:
            messages.info(request,"El nombre de usuario debe tener al menos 10 digitos")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"La contraseña no coincide")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
            
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"El usuario ha sido creado. Inicie sesión.")
        return redirect('/login')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Inicio de sesión exitosa")
            return redirect('/')
        else:
            messages.error(request,"Credenciales no válidas")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Cierre de sesión exitoso")    
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('Nombre')
        email=request.POST.get('Email')
        number=request.POST.get('Telefono')
        desc=request.POST.get('Descripcion')
        myquery=Contacto(Nombre=name,Email=email,Telefono=number,Descripcion = desc)
        myquery.save()       
        messages.info(request,"Gracias por contactarnos, nos comunicaremos con usted pronto.")
        return redirect('/contact')
    
    return render(request,"contact.html") 

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Por favor inicie sesion e intente de nuevo")
        return redirect('/login')
    membresias = Membresia.objects.all()
    entrenadores = Entrenadore.objects.all()
    context={"Membresia":membresias, "Entrenadore":entrenadores}
    if request.method=="POST":
        NombreCompleto = request.POST.get('NombreCompleto')
        Cedula = request.POST.get('Cedula')
        Email = request.POST.get('Email')
        Telefono = request.POST.get('Telefono')
        Direccion = request.POST.get('Direccion')
        Member = request.POST.get('Member')
        Trainer = request.POST.get('Trainer')
        FN = request.POST.get('FechaNacimiento')
        query=Usuario(NombreCompleto=NombreCompleto,Email=Email,Cedula=Cedula,Telefono=Telefono,Direccion=Direccion, SeleccionarMembresia=Member,SeleccionarEntrenador=Trainer, FechaNacimiento = FN)
        query.save()
        messages.success(request,"Gracias por inscribirse")
        return redirect('/join')
    
    return render(request,"enroll.html",context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Por favor inicie sesión e intente de nuevo")
        return redirect('/login')
    entrenadores = Entrenadore.objects.all()
    context={"entrenadores":entrenadores}
    if request.method=="POST":
        Usuario = request.POST.get('username')
        InicioSesion = request.POST.get('Logintime')
        FinSesion = request.POST.get('Loginout')
        Entrenamiento = request.POST.get('workout')
        query=Asistencia(Usuario=Usuario,InicioSesion=InicioSesion,FinSesion=FinSesion,Entrenamiento=Entrenamiento)
        query.save()
        messages.warning(request,"Asistencia aplicada")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

def nosotros(request):
    return render(request, 'nosotros.html')

def service(request):
    return render(request, 'service.html')
