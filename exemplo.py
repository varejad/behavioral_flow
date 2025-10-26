from behavioralflow import Aprendente

# define uma variável com um dicionário onde as chaves são string contendo o "nome" da ação
# e os valores são listas onde o indice [0] é o custo da ação e o indice [1] é o fator da probabilidade dessa ação ser escolhida
# essa varia´vel será passada como atributo na instancia do aprendente
acoes_do_exemplo1 = {"ação A": [5, 10],
                   "ação B": [5, 10],
                   "ação C": [5, 10],
                   "ação D": [5, 10],}

acao = "-"
acao_anterior = "-"

# METODOS DAS AÇÕES
def acao_A(passo):
    print(f"executando {exemplo1.acao_atual}")
    if antecedente[0] == "ação D":
        exemplo1.reforcar(1.0)
    #else: exemplo1.reforcar(-5)

def acao_B():
    print(f"executando {exemplo1.acao_atual}")
    if antecedente[0] == "ação A":
        exemplo1.reforcar(1.0)
    #else: exemplo1.reforcar(-5)
        
def acao_C():
    print(f"executando {exemplo1.acao_atual}")
    if antecedente[0] == "ação B":
        exemplo1.reforcar(1.0)
    #else: exemplo1.reforcar(-5)
        
def acao_D():
    print(f"executando {exemplo1.acao_atual}")
    if antecedente[0] == "ação C":
        exemplo1.reforcar(1.0)
    #else: exemplo1.reforcar(-5)
        
# instanciando o Aprendente
exemplo1 = Aprendente(acoes_do_exemplo1, prob_variacao=0, taxa_extincao=0.0, k=1)

def executar_acao(acao):
    #if len(acao) > 1: exemplo1.reforcar(10)

    for passo in acao: # caso a acao tenha mais de um passo
        #print(f"passo: {passo}")
        if passo == "ação A":
            acao_A(passo)
        elif passo == "ação B":
            acao_B()
        elif passo == "ação C":
            acao_C()
        elif passo == "ação D":
            acao_D()

# loop onde se define o antecedente, a proxima ação e chama a função par executar a ação
for i in range(100):
    #print(f"\n{exemplo1.antecedentes_e_respostas}")
    # definir antecedende (neste exemplo estou usando como antecedente apenas a ultima acao executada)
    antecedente = [acao[0], acao_anterior[0]]

    acao_anterior = acao

    #chamar próxima ação
    acao = exemplo1.proxima_acao(antecedente)

    #chamar função para executar a ação definida acima
    executar_acao(acao)
    
#for item in exemplo1.antecedentes_e_respostas:    print(f"{item}:  {exemplo1.antecedentes_e_respostas[item]}")

#print(f"\n\n{exemplo1.antecedentes_e_respostas}")