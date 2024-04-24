from time import sleep
from random import choice

from telebot import TeleBot
from telebot.types import CallbackQuery

import utils
import textos
import botoes


def resposta_opcao_escolhida(msg: CallbackQuery, bot: TeleBot) -> None:
    """
    Responde a escolhe uma opção.
    """
    op_jogador = msg.data.split()[-1]
    botao_jogador = botoes.botoes_opcoes[op_jogador]
    op_cpu = choice(seq=list(botoes.botoes_opcoes.keys()))
    botao_cpu = botoes.botoes_opcoes[op_cpu]
    msg_resultado, op = utils.checar_vencedor(op_jogador=op_jogador, op_cpu=op_cpu)

    bot.edit_message_text(
        text=textos.mensagem_cpu_jogando,
        chat_id=msg.from_user.id,
        message_id=msg.message.message_id,
    )
    sleep(2)
    texto = textos.mensagem_resultado.format(msg_resultado, botao_cpu, botao_jogador)
    bot.edit_message_text(
        text=texto, chat_id=msg.from_user.id, message_id=msg.message.message_id
    )

    if op:  # Envia o emoji da opção vencedora
        op_vencedor = botoes.botoes_opcoes[op]
        bot.send_message(chat_id=msg.from_user.id, text=op_vencedor.split()[0])
