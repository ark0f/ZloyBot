import re
from random import choice

from telegram.ext import CommandHandler, Filters, MessageHandler


class PrimitiveResponse:
    def __init__(self, chat_id):
        self._chat_id = chat_id
    
    def add_handlers(self, add_handler):
        add_handler(MessageHandler(Filters.text, self._run))
        add_handler(CommandHandler('me', self._me, pass_args=True))

    def _run(self, bot, update):
        def text_response(patterns, answer):
            if any(re.search(pattern, text) for pattern in patterns):
                if answer.endswith('.txt'):
                    answer = self._choice_variant_from_file(answer)
                bot.sendMessage(chat_id=chat_id, text=answer,
                                reply_to_message_id=message_id,
                                markdown_support=True)
        
        message = update.message
        chat_id = message.chat_id
        text = message.text.lower()
        message_id = message.message_id
        
        text_response(['ты злой', 'злой ты', 'ты - злой', 'вы злые', 'злые вы',
                       'вы - злые', 'вы все злые'], 'ты злой!')
        
        text_response(['спать', 'посплю'], 'snov.txt')
        
        text_response(['бот злой'], 'Ты не лучше.')
    
        text_response({r'иди на ?хуй', r'на ?хуй пошел', r'на ?хуй иди',
                       r'пошел на ?хуй'}, 'nahui.txt')
        
        text_response(['бот пидор', 'бот идиот', 'бот мудак'], 'И?')
        
        text_response(['бот умер'], 'Герої не вмирають! 🇺🇦')
        
        text_response(['бот няша'], 'Спасибо, ты тоже <3')
        
        text_response(['бот жив', 'бот, ты жив', 'ты жив, бот'],
                      'Так точно, капитан')
        
        text_response(['утра', 'доброе утро', 'утречка'], 'utro.txt')
        
        text_response(['украин'], '🇺🇦')
        
        text_response(['рот ебал', 'ебал в рот'], 'Фуууу, противно!')
    
    def _me(self, bot, update, args):
        message = update.message
        
        text = "{0} {1}".format(message.from_user.username, ' '.join(args))
        bot.sendMessage(chat_id=self._chat_id, text=text)

    @staticmethod
    def _choice_variant_from_file(file_name):
        with open('modules/responses/%s' % file_name) as file:
            variant = choice(file.read().splitlines())
        return variant
