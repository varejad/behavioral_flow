from main import Aprendente

# define uma variável com um dicionário onde as chaves são tuplas contendo o "nome" da ação
# e os valores são listas onde o indice [0] é o custo da resposta e o indice [1] é o fator da probabilidade
# essa varia´vel será passada como atributo na instancia do apredente
acoes_do_teste1 = {("andar_para_frente",): [2, 5],
                   ("andar_para_tras",): [2, 5],
                   ("ficar_parado",): [0, 5],
                   ("pular",): [4, 500],
                   ("andar_para_frente","andar_para_frente","andar_para_frente"): [2, 5]}

teste1 = Aprendente(acoes_do_teste1, variar=True)
acao = teste1.proxima_acao(["nada"])

print(f"teste: {acao}")

if acao == ("pular",):
    print("PULANDO")
    teste1.reforcar(3)