from django.shortcuts import render
from django.http import HttpResponse

from .models import Work, Сomment, Client, Bid, FeedbackType , Staff

from PCHelp.management.commands import settingsbot
from telebot import types
import telebot


# Create your views here.
def home(request):
    if request.method == "POST":  # тут обрабатываем данные от пользователя с формы
        pass

    return render(request, 'pchelp/home.html')


# def uslugi(request):
#     return render(request, 'pchelp/detailblocks/uslugi.html')


def main(request):
    listuslugi = None
    listcomments = None
    listmasters = None

    if request._post['Page'] == 'Uslugi':
        listuslugi = Work.objects.all()
    elif request._post['Page'] == 'Comments':
        listcomments = Сomment.objects.order_by('-datecreation')
    elif request._post['Page'] == 'OurTeam':
        listmasters = Staff.objects.all()

    data = {
        'pagename': 'pchelp/detailblocks/' + request._post['Page'] + '.html',
        'listuslugi': listuslugi,
        'listcomments': listcomments,
        'listmasters': listmasters,
    }
    return render(request, 'pchelp/detailblocks/main.html', data)


def addcomment(request):
    if request.method == "POST":  # тут обрабатываем данные от пользователя с формы добавки комментария
        number = request._post['NumberComment']  # Берем с формы телефон
        newtextcomment = request._post['TextComment']

        try:
            findclient = Client.objects.get(numberphone=number)  # ищем по телефону клиента в базе
            newcomment = Сomment(client=findclient, textcomment=newtextcomment)
            newcomment.save()

            return HttpResponse('Комментарий отправлен.')
        except:
            return HttpResponse('Не найден номер телефона! Комментарий не отправлен.')


def createbid(request):
    if request.method == "POST":
        if 'createbid' in request.COOKIES:
            return HttpResponse("Вы уже отправляли заявку.")

        Firstname = request._post['Firstname']
        # Lastname = request._post['Secondname']
        Phone = request._post['Phone']
        # Email = request._post['Email']
        Message = request._post['Message']
        # GroupSelect = request._post['GroupSelect']

        # test = FeedbackType.objects.get(id=int(GroupSelect))
        try:
            client = Client.objects.get(numberphone=Phone)  # ищем по телефону клиента в базе
        except:    #Если не нашли создаем нового через попытку
            try:
                client = Client(firstname=Firstname, numberphone=Phone)
                client.save()
            except:
                return HttpResponse('Не удалось создать клиента.')

        # Через попытку создаем новый объект заявки
        try:
            newbid = Bid(client=client, textbid=Message)

            try:  # Через попытку отправляем уведомление в телегу
                sendbidTelegram(Firstname, Phone, Message)
                newbid.unloadTelegram = True
            except:
                newbid.unloadTelegram = False

            try:
                newbid.save()
                response = HttpResponse('Заявка отправлена!')
                response.set_cookie('createbid', True)
            except:
                response = HttpResponse('Заявка не отправлена!')
                #response.set_cookie('createbid', False)

            return response
        except:
            return HttpResponse('Не удалось создать объект заявки.')


# функция отправки сообщения в телеграм при создании заявки
def sendbidTelegram(Firstname, Phone, Message):
    # bot = telebot.TeleBot('1020021516:AAGd6g5b8jv25b2z9oLba7eVoi4NU3e4sw4')
    bot = telebot.TeleBot(settingsbot.TOKEN);
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Принять", callback_data='take')
    textformessage = "Клиент <b>{}</b>; \nНомер телефона: <b>{}</b>;\nПроблема: \n{};".format(Firstname,Phone, Message)
    markup.add(item1)

    result = bot.send_message(-471481995, textformessage, parse_mode='html', reply_markup=markup)
    return result