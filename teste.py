from main import Aprendente

# define uma variável com um dicionário onde as chaves são tuplas contendo o "nome" da ação
# e os valores são listas onde o indice [0] é o custo da resposta e o indice [1] é o fator da probabilidade
# essa varia´vel será passada como atributo na instancia do apredente
acoes_do_teste1 = {("ação A",): [0, 5],
                   ("ação B",): [0, 5],
                   ("ação C",): [0, 5],
                   ("ação D",): [0, 5],}

# CRIAR AQUI A FUNÇÃO QUE PEDE PELA PROXIMA AÇÃO, EXECUTA A AÇÃO (INCLUSIVE SE ELA VIER COM MAIS DE UM PASSO) E PEDE NOVAMENTE PELA PROXIMA AÇÃO

teste1 = Aprendente(acoes_do_teste1, variar=True)

for i in range(20):
    print(teste1._antecedentes_e_respostas)
    acao = teste1.proxima_acao(["nada"])
    print(acao)
    if acao == ("ação A",) or acao == ("ação B",):
        #teste1.reforcar()
        pass
    if len(acao) == 2:
        print(f"passos: {len(acao)}")
        teste1.reforcar(-10)
    print(len(teste1.respostas_atuais))


# sobre as ações geradas na variação: fica como resposabilidade de quem usar essa biblioteca garantir que 
    # cada açao da lista de gerada na variação seja executada antes de pedir uma nova ação
    """# verifica se a ação atual não tem mais um passo a ser realizado,
    se tiver retorna a ação sem o passo já realizado
    if len(self._acao_atual) > 1:
      identado dentro desse if poderia estar o código para retornar a proxima acao da tupla até que fossem realizadas todas,
      mas optei por outra abordagem descrita acima"""