from django.db import models
from django.utils import timezone

# Create your models here.
#########################################################################
class Roles(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название')

    class Meta:
        verbose_name_plural = 'Роли'
        verbose_name = 'Роль'

    def __str__(self):
        return self.name

#########################################################################
class FeedbackType(models.Model):
    option = models.CharField(max_length=50, verbose_name = 'Тип')

    class Meta:
        verbose_name_plural = 'Типы обратной связи'
        verbose_name = 'Тип обратной связи'

    def __str__(self):
        return self.option


#########################################################################
class Work(models.Model):
    nameWork = models.CharField(max_length=50, verbose_name = 'Наименование работы')
    description = models.CharField(max_length=250, verbose_name = 'Описание работы')
    price = models.PositiveIntegerField(verbose_name = 'Цена')

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услуга'

    def __str__(self):
        return self.nameWork
#########################################################################
class Staff(models.Model):
    firstname = models.CharField(max_length=50, verbose_name = 'Имя')
    lastname = models.CharField(max_length=50, verbose_name = 'Фамилия')
    numberphone = models.CharField(max_length=20, verbose_name = 'Номер телефона')
    email = models.CharField(max_length=70, verbose_name = 'email адрес')
    isactive = models.BooleanField(default=True, verbose_name = 'Активный')
    ban = models.BooleanField(default=False, verbose_name = 'Заблокирован')
    datecreation = models.DateTimeField(default=timezone.now, verbose_name = 'Дата создания')
    role = models.ForeignKey(Roles,  on_delete=models.CASCADE, verbose_name='Роль')
    idtelegram = models.IntegerField(null=True)
    about = models.CharField(max_length=100, verbose_name= 'Обо мне', null=True)
    profileimg = models.CharField(max_length=30,verbose_name="Фото",default="profile.png")

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    def __str__(self):
        return self.firstname + ' ' + self.lastname

#########################################################################
class Client(models.Model):
    firstname = models.CharField(max_length=50, verbose_name = 'Имя')
    lastname = models.CharField(max_length=50, verbose_name = 'Фамилия', null=True)
    numberphone = models.CharField(max_length=20, verbose_name = 'Номер телефона')
    email = models.CharField(max_length=70, verbose_name = 'email адрес',null=True)
    isactive = models.BooleanField(default=True, verbose_name = 'Активный')
    ban = models.BooleanField(default=False, verbose_name = 'Заблокирован')
    datecreation = models.DateTimeField(default=timezone.now, verbose_name = 'Дата создания')

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'

    def __str__(self):
        return self.firstname + ' ' + self.numberphone

#########################################################################
class Bid(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name = 'Клиент')
    textbid = models.CharField(max_length=200, verbose_name = 'Текст заявки')
    typeFeedback = models.ForeignKey(FeedbackType, on_delete=models.PROTECT, verbose_name = 'Тип обратной связи', null=True)
    datecreation = models.DateTimeField(default=timezone.now, verbose_name = 'Дата создания')
    unloadTelegram = models.BooleanField(default= False, verbose_name = 'Выгружена в телеграм')
    worker = models.ForeignKey(Staff, null=True,on_delete=models.CASCADE,verbose_name='Ответственынй')

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'

#########################################################################
class Сomment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name = 'Клиент')
    textcomment = models.CharField(max_length=200, verbose_name = 'Текст отзыва')
    datecreation = models.DateTimeField(default=timezone.now,verbose_name = 'Дата создания')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

