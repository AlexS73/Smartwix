from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from PCHelp.models import Staff
from . import settingsbot

class Command(BaseCommand):
    help = 'Телеграмм- бот pyTelegramBotAPI'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(settingsbot.TOKEN)
        print(bot.get_me())

        @bot.message_handler(content_types=["text"])
        def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
            bot.send_message(message.chat.id, message.text)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            # remove inline buttons

            try:
                staffperson = Staff.objects.get(idtelegram=call.from_user.id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=call.message.text + "\n Ответственный: " + staffperson.firstname + ' ' + staffperson.lastname,
                                      reply_markup=None)
            except:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Не найден сотрудник по telegram id ")


        #if(__name__ ) == 'PCHelp.management.commands.bot2':
        #    bot.polling(none_stop=True)
        bot.polling(none_stop=True)