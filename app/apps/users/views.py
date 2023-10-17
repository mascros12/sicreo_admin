from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import ensure_csrf_cookie

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, CustomUserChangeForm

@ensure_csrf_cookie
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            #messages.success(request, 'Welcome {}!'.format(user.get_full_name()))
            return redirect('index')
        else:
            messages.error(request, 'El usuario o contraseña es incorrecto.')
    return render(request, 'users/login.html',{})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión Cerrada')
    return redirect('login')

class  CreateUser(FormView):
    form_class = UserCreationForm
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('login')  # Página a la que redirigir tras el registro exitoso

    def form_valid(self, form):
        # Aquí puedes realizar acciones adicionales antes de guardar el usuario
        form.save()
        return super().form_valid(form)

@login_required
@staff_member_required  
def register(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Success Register') 
            return redirect('index') 
    return render(request, 'users/userForm.html',{
        'form':form
    })

def user_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users = User.objects.all()
    return render(request, 'users/userList.html',{
        'object_list':users
    })

class UserUpdate(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/userFormUpdate.html'
    success_url = reverse_lazy('user_list')    

class UserDelete(DeleteView):
    model = User
    template_name = 'users/userDelete.html'
    success_url = reverse_lazy('user_list') 

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.kwargs['pk'])

@login_required
@staff_member_required
def change_password(request, user_id):
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        new_password = request.POST['new_password']
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Contraseña cambiada exitosamente.')
        return redirect('user_list')

    return render(request, 'users/passwordChange.html', {'user': user})
