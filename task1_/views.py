from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from Urban.task1.forms import UserRegister
from django.http import HttpResponse


def menu_page(request):
    return render(request, 'menu.html')

def shop_page(request):
    clothes = ['Футбоки', 'Джинсы', 'Кроссовки ', 'Кофты']
    context = {
        'clothes': clothes
}
    return render(request, 'shop_page.html', context)

def bin_page(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    return render(request, 'bin_page.html', context)


def sign_up_by_html(request):
    users = ['Dmitry', 'Alexey', 'Alexandr']
    info = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем, {username}!')

        print(f"Имя: {username}")
        print(f"Пароль: {password}")
        print(f"Повтор пароля: {repeat_password}")
        print(f"Возраст: {age}")


    return render(request, 'registration_page.html', info)



def sign_up_by_django(request):
    Buyers = Buyer.objects.all()  # Получаем всех покупателей
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Проверяем, существует ли пользователь с таким именем
                user_exists = False
                for buyer in Buyers:
                    if buyer.name == username:  # Предполагается, что у модели Buyer есть поле username
                        user_exists = True
                        break

                if user_exists:
                    info['error'] = 'Пользователь уже существует'
                else:
                    # Создаем нового покупателя
                    Buyer.objects.create(name=username, balance=0, age=age)
                    return HttpResponse(f'Приветствуем, {username}!')

    info['form'] = form
    return render(request, 'registration_page.html', info)

def collect_of_games(request):
    Games = Game.objects.all()
    context = {
        'Games':Games,
    }

    return render(request, 'games.html', context)

def main_page(request):
    return HttpResponse("Это главная страница")
# Create your views here.
