def checar_vencedor(op_jogador: str, op_cpu: str) -> tuple[str, str | None]:
    """
    Retorna a mensagem do vencedor e a opção vencedora.
    """
    if op_jogador == op_cpu:
        msg = "Empatou!"
        op = None
    elif (
        (op_jogador == "pe" and op_cpu == "te")
        or (op_jogador == "pa" and op_cpu == "pe")
        or (op_jogador == "te" and op_cpu == "pa")
    ):
        msg = "Parabéns, você ganhou!"
        op = op_jogador
    else:
        msg = "Eu ganhei! Haha."
        op = op_cpu
    return msg, op
