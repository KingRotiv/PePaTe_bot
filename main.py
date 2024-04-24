import logging

import telebot
from telebot.types import BotCommand

import config
from plugins import comandos
from plugins import respostas


bot = telebot.TeleBot(token=config.TOKEN, parse_mode="HTML")
bot.set_my_commands(
    commands=[
        BotCommand(command="jogar", description="Jogar"),
        BotCommand(command="regras", description="Regras do jogo"),
    ]
)
telebot.logger.setLevel(logging.DEBUG)

# Comandos
bot.register_message_handler(
    callback=comandos.comando_start, commands=["start", "jogar"], pass_bot=True
)
bot.register_message_handler(
    callback=comandos.comando_regras, commands=["regras"], pass_bot=True
)

# Respostas
bot.register_callback_query_handler(
    callback=respostas.resposta_opcao_escolhida,
    func=lambda msg: msg.data.startswith("#op"),
    pass_bot=True,
)


if __name__ == "__main__":
    bot.infinity_polling()
