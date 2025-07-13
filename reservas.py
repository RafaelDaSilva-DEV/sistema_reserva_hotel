def processar_reservas(quartos_disponiveis, reservas_solicitadas):
    quartos_disponiveis = set(quartos_disponiveis)
    confirmadas = []
    recusadas = []

    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            confirmadas.append(quarto)
            quartos_disponiveis.remove(quarto)
        else:
            recusadas.append(quarto)

    return confirmadas, recusadas