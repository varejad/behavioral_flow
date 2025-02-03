from main import Aprendente

# define uma variável com um dicionário onde as chaves são tuplas contendo o "nome" da ação
# e os valores são listas onde o indice [0] é o custo da ação e o indice [1] é o fator da probabilidade dessa ação ser escolhida
# essa varia´vel será passada como atributo na instancia do apredente
acoes_do_exemplo1 = {("ação A",): [0, 5],
                   ("ação B",): [0, 5],
                   ("ação C",): [0, 5],
                   ("ação D",): [0, 5],}

acao = ("a",)

# METODOS DAS AÇÕES
def acao_A():
    print("executando acao A")
    if antecedente[0] == "ação D":
        exemplo1.reforcar(10)

def acao_B():
    print("executando acao B")
    if antecedente[0] == "ação A":
        exemplo1.reforcar(10)

def acao_C():
    print("executando acao C")
    if antecedente[0] == "ação B":
        exemplo1.reforcar(10)

def acao_D():
    print("executando acao D")
    if antecedente[0] == "ação C":
        exemplo1.reforcar(10)

# instanciando o Aprendente
exemplo1 = Aprendente(acoes_do_exemplo1, True)


def executar_acao(acao):
    for passo in acao: # caso a acao tenha mais de um passo
        if passo == "ação A":
            acao_A()
        elif passo == "ação B":
            acao_B()
        elif passo == "ação C":
            acao_C()
        elif passo == "ação D":
            acao_D()

# loop onde se define o antecedente, a proxima ação e chama a função par executar a ação
for i in range(100):
    # definir antecedende (neste exemplo estou usando como antecedente apenas a ultima acao executada)
    antecedente = acao

    #chamar próxima ação
    acao = exemplo1.proxima_acao(antecedente)

    #chamar função para executar a ação definida acima
    executar_acao(acao)

