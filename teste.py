from main import Acao, Aprendente

#acao1 = Acao(["testar"], 1, 2)


acoes_do_teste1 = {("andar_para_frente"): [2, 5],
                   ("andar_para_tras"): [2, 5],
                   ("ficar_parado"): [0, 5],
                   ("pular"): [4, 5]}

teste1 = Aprendente(acoes_do_teste1)
teste1.proxima_acao(["nada"])
