from pyexpat.errors import messages

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect

from tblog.models import UsersAll

from django.contrib import messages


# Create your views here.


def first_list(request):
    return render(request, 'base.html')

# def second_list(request):
#     return render(request, 'tblog.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordConf = request.POST.get('password_confirm')
        email = request.POST.get('email')

        try:
            if username and password and email:
                if UsersAll.objects.filter(username=username).exists():
                    return JsonResponse({'error': 'Пользователь с таким именем уже существует'}, status=400)
                if UsersAll.objects.filter(email=email).exists():
                    return JsonResponse({'error': 'Email уже используется'}, status=400)

                UsersAll.objects.create(
                    username=username,
                    password=password,
                    email=email,
                )
                return JsonResponse({'message': 'Пользователь успешно зарегистрирован'})
            else:
                return JsonResponse({'error': 'Все поля должны быть заполнены'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, template_name='tblog.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UsersAll.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'message': 'Успешный вход'})
            else:
                return JsonResponse({'error': 'Неверный пароль'}, status=400)
        except UsersAll.DoesNotExist:
            return JsonResponse({'error': 'Пользователь не найден'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, template_name='tblog.html')
