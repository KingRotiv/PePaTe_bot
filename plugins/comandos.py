from telebot import TeleBot
from telebot.util import escape
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

import textos
import botoes


def menu_start() -> InlineKeyboardMarkup:
    """
    Retorna o menu do comando /start.
    """
    menu = [
        [
            InlineKeyboardButton(text=botao, callback_data=f"#op {op}")
            for op, botao in botoes.botoes_opcoes.items()
        ]
    ]
    return InlineKeyboardMarkup(keyboard=menu)


def comando_start(msg: Message, bot: TeleBot) -> None:
    """
    Responde ao comando /start.
    """
    nome = escape(msg.from_user.first_name)
    bot.reply_to(
        message=msg, text=textos.mensagem_start.format(nome), reply_markup=menu_start()
    )


def comando_regras(msg: Message, bot: TeleBot) -> None:
    """
    Responde ao comando /regras.
    """
    bot.reply_to(message=msg, text=textos.mensagem_regras)
