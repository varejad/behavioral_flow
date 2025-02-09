# behavioralflow

**BehavioralFlow** é fruto de um hobby onde eu busquei simular princípios básicos da Análise do Comportamento (AC), ciência que estuda o comportamento dos organismos.
Consegui simular alguns dos conceitos básicos da AC (como reforçamento, punição, variação e discriminação de estímulos) e deixei alguns de fora (pelo menos nessa versão).
Como resultado percebi que acabei criando um algorítmo de aprendizagem por reforço, então decidi transformar nesta biblioteca e compartilhar.

A biblioteca contém uma classe chamada Aprendente (simula o organismo capaz de aprender como agir).
Os objetos instaciados com essa classe são capazes de aprender por reforçamento e podem levar em cosideração o contexto (também chamado de antecedente em AC).
Ou seja, eles aprendem o que devem fazer de acordo com o contexto fornecido. Além disso, podem criar sequências de ações básicas para criar ações novas.


## Como usar a biblioteca

### Como criar um agente que aprende

Ao instaciar um Aprendente você deve passar como parâmetro obrigatório um dicionário contendo as ações básicas desse Aprendente.

As chaves desse dicionário obrigatoriamente devem ser tuplas (preferencialmente com apenas um ítem do tipo String) que serão os 'nomes' das ações.

Já os valores obrigatoriamente devem ser listas de dois ítens do tipo int >= 0.
O primeiro será o custo daquela ação (algo como a dificuldade que um organismo tem para realizar uma ação, ou energia gasta para realizar essa ação, quanto maior esse custo menor as chances dessa ação ser realizada).
O segundo int será um 'fator de probabilidade' quanto maior esse número em relação aos fatores das outras ações, maior as chances dessa ação acontecer. Se todas as ações tiverem o mesmo fator e mesmo custo terão a mesma chance de acontecer.

EXEMPLO:
    
    from behavioralflow import Aprendente

    acoes_do_exemplo1 = {
        ("ação_1",): [2, 5],  # custo = 2, fator de probabilidade = 5
        ("ação_2",): [1, 3]
    }

    agente = Aprendente(acoes_do_exemplo1)


Existem 2 parametros opcionais ao se instanciar um Aprendente.
O primeiro é um booleano (por padrão ele é False), que se refere à capacidade do organismo de realizar a simulação de variação comportamental. Nesse caso se refere à capacidade de combinar ações básica passadas no primeiro parâmetro para criar novas ações. Isso pode acontecer quando uma ação ocorre e não é reforçada.
O segundo parametro opcional é um float x, tal que 1 < x > 0. Esse parametro se refere à probabilidade do Aprendente variar o comportamento a cada vez que não é reforçado, por padrão esse valor é 0.25




### Como fazer o agente realizar ações e como reforçar ou punir
Para que o Aprendente emita alguma ação você deve usar o método 'Aprendente.proxima_acao()', esse método precisa de um parâmentro que será usado como antecedente ou contexto, esse parâmetro deve ser uma tupla, a quantidade e tipo dos iténs ficam a seu critério.

    contexto = ("contexto_exemplo",)
    acao = agente.proxima_acao(contexto)
    print(f"Ação emitida: {acao}")


Quando o aprendente executar uma ação que deva acontecer mais vezes você deve usar o método 'Apredente.reforcar()'. Esse método possui 2 parâmetro opcionais.
O primeiro deve ser um int e é a magnitude do reforçamento, por padrão é 1, quanto maior mais reforçada a ação será, ou seja, mais aumenta a probabilidade daquela ação ocorrer.
Se o valor desse parâmetro for < 0 então a ação será punida, ou seja, a probabilidade séra diminuída. Se o fator chegar a ser igual ou menor que o custo a ação não aconterá mais, portanto não poderá ser reforçada.
O segundo parâmetro é a ação a ser reforçada, por padrão ele irá reforçar a última ação definida.

    if acao = acao_desejada_nesse_contexto:
        agente.reforcar()
    elif acao = acao_indesejada
        agente.reforcar(-1)


### Sugestão de uso

Minha sugestão para usar essa biblioteca é que seu código tenha um loop onde 
1) o antecedente/contexto que será passado como parâmetro será definido.
2) a proxima ação será definida usando .proxima_acao(antecedente).
3) a ação que foi definida será executada, para isso eu chamo outra função e passo a ação definida como parâmetro.
4) após a ação ser executada pode-se reforçada ou punida de acordo com o objetivo do seu projeto (por exemplo, reforçar se o agente conseguir prever algum dado de acordo com o contexto)
5) reiniciar o loop

Confira o arquivo 'exemplo.py' para ver um caso prático em que o agente aprende uma sequência esperada de ações.
para isso eu usei a ação anterior do agente como contexto e reforcei se a proxima ação correspondesse à sequência que eu gostaria e punia caso não.
No fim da interação o agente está executando as ações na sequência esperada, usando como contexto a ação executada anteriormente para escolher a próxima.

    when True:
        antecedente = definir_antecedente()

        acao = agente.proxima_acao(antecedente)

        resultado_da_acao = executar_acao(acao)

        if resultado_da_acao = resultado_positivo:
            agente.reforcar()

## Instalação

Para instalar a biblioteca, use o `pip`:

pip install behavioralflow
