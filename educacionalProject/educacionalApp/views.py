from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         # Redirecionar para uma página após o login bem-sucedido
    #         return redirect('area_aluno.html')
    # else:
    #     return render(request, 'index.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = get_user_model()
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            user = None
    if user is not None and user.check_password(password):
        session = request.session
        session.clear_expired()
        session.set_expiry(settings.SESSION_COOKIE_AGE)
        login(request, user)
        try:
            aluno = Aluno.objects.get(user=user)
            return render(request, 'area_aluno.html', {'aluno': aluno})
        except Aluno.DoesNotExist:
            return render(request, 'index.html', {'error': 'Aluno matching query does not exist.'})
    else:
        return render(request, 'login.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # Aqui você pode adicionar o código para enviar um e-mail ou salvar as informações de contato
        messages.success(request, 'Contato enviado com sucesso!')
        return redirect('home')
    return render(request, 'contact_modal.html')

@login_required
def area_restrita(request):
    return render(request, 'area_aluno.html')