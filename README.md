# behavioralflow

PT-BR

**BehavioralFlow** é fruto de um hobby onde eu busquei simular princípios básicos da Análise do Comportamento (AC), ciência que estuda o comportamento dos organismos. Consegui simular alguns dos conceitos básicos da AC (como reforçamento, punição, variação e discriminação de estímulos) e deixei alguns de fora (pelo menos nessa versão). Como resultado, percebi que acabei criando um algoritmo de aprendizagem por reforço, então decidi transformá-lo nesta biblioteca e compartilhar.

A biblioteca contém uma classe chamada Aprendente (simula o organismo capaz de aprender como agir). Os objetos instanciados com essa classe são capazes de aprender por reforçamento e podem levar em consideração o contexto (também chamado de antecedente em AC). Ou seja, eles aprendem o que devem fazer de acordo com o contexto fornecido. Além disso, podem criar sequências de ações básicas para criar ações novas.

EN-US

**BehavioralFlow** is the result of a hobby where I sought to simulate basic principles of Behavior Analysis (BA), the science that studies the behavior of organisms. I managed to simulate some of the basic BA concepts (such as reinforcement, punishment, variation, and stimulus discrimination) and left some out (at least in this version). As a result, I realized that I had created a reinforcement learning algorithm, so I decided to turn it into this library and share it.

The library contains a class called Aprendente (which simulates an organism capable of learning how to act). Objects instantiated with this class can learn through reinforcement and can consider the context (also called antecedent in BA). In other words, they learn what they should do according to the given context. Additionally, they can create sequences of basic actions to form new actions.


PT-BT

## Como usar a biblioteca

### Como criar um agente que aprende

Ao instaciar um Aprendente você deve passar como parâmetro obrigatório um dicionário contendo as ações básicas desse Aprendente.

As chaves desse dicionário obrigatoriamente devem ser tuplas (preferencialmente com apenas um ítem do tipo String) que serão os 'nomes' das ações.

Já os valores obrigatoriamente devem ser listas de dois ítens do tipo int >= 0.
O primeiro será o custo daquela ação (algo como a dificuldade que um organismo tem para realizar uma ação, ou energia gasta para realizar essa ação, quanto maior esse custo menor as chances dessa ação ser realizada).
O segundo int será um 'fator de probabilidade' quanto maior esse número em relação aos fatores das outras ações, maior as chances dessa ação acontecer. Se todas as ações tiverem o mesmo fator e mesmo custo terão a mesma chance de acontecer.

EXEMPLO:
    
    from behavioralflow.core import Aprendente

    acoes_do_exemplo1 = {
        ("ação_1",): [2, 5],  # custo = 2, fator de probabilidade = 5
        ("ação_2",): [1, 3]
    }

    agente = Aprendente(acoes_do_exemplo1)


Existem 2 parametros opcionais ao se instanciar um Aprendente.
O primeiro é um booleano (por padrão ele é False), que se refere à capacidade do organismo de realizar a simulação de variação comportamental. Nesse caso se refere à capacidade de combinar ações básica passadas no primeiro parâmetro para criar novas ações. Isso pode acontecer quando uma ação ocorre e não é reforçada.
O segundo parametro opcional é um float x, tal que 1 < x > 0. Esse parametro se refere à probabilidade do Aprendente variar o comportamento a cada vez que não é reforçado, por padrão esse valor é 0.25


EN-US

## How to Use the Library

### How to Create a Learning Agent

When instantiating an Aprendente, you must pass a required dictionary containing the basic actions of this Aprendente.

The keys of this dictionary must be tuples (preferably with only one item of type String) that will be the 'names' of the actions.

The values must be lists of two items of type int >= 0. The first is the cost of that action (something like the difficulty an organism has in performing an action, or energy spent to perform it; the higher this cost, the lower the chance of this action being performed). The second int will be a 'probability factor'; the higher this number in relation to the factors of other actions, the higher the chances of this action occurring. If all actions have the same factor and cost, they will have the same probability of occurring.

EXAMPLE:

from behavioralflow.core import Aprendente

actions_example = {
    ("action_1",): [2, 5],  # cost = 2, probability factor = 5
    ("action_2",): [1, 3]
}

agent = Aprendente(actions_example)


There are two optional parameters when instantiating an Aprendente.
The first is a boolean (default is False), which refers to the organism's ability to simulate behavioral variation. In this case, it refers to the ability to combine basic actions passed in the first parameter to create new actions. This can happen when an action occurs and is not reinforced.
The second optional parameter is a float x, such that 1 < x > 0. This parameter refers to the probability of the Aprendente varying its behavior each time it is not reinforced. By default, this value is 0.25.


PT-BR

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


EN-US

### How to make the agent perform actions and how to reinforce or punish

For the Aprendente to emit an action, you must use the method 'Aprendente.proxima_acao()'. This method requires a parameter that will be used as an antecedent or context. This parameter must be a tuple, and the number and type of items are up to you.

context = ("example_context",)
action = agent.proxima_acao(context)
print(f"Emitted action: {action}")

When the Aprendente performs an action that should occur more frequently, you should use the 'Aprendente.reforcar()' method. This method has two optional parameters.
The first must be an int and represents the magnitude of reinforcement. By default, it is 1. The higher the value, the more reinforced the action will be, meaning the probability of that action occurring increases.
If this parameter's value is < 0, the action will be punished, reducing its probability. If the factor reaches or falls below the cost, the action will no longer occur and thus cannot be reinforced.
The second parameter is the action to be reinforced. By default, it reinforces the last defined action.

if action == desired_action_in_this_context:
    agent.reforcar()
elif action == undesired_action:
    agent.reforcar(-1)

PT-BR

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


EN-US

### Usage Suggestion

My suggestion for using this library is that your code has a loop where:

The antecedent/context to be passed as a parameter is defined.

The next action is determined using .proxima_acao(antecedente).

The defined action is executed by calling another function and passing the defined action as a parameter.

After the action is executed, it can be reinforced or punished according to your project's objective (e.g., reinforcing if the agent manages to predict some data according to the context).

Restart the loop.

Check the 'exemplo.py' file for a practical case where the agent learns an expected sequence of actions. To do this, I used the agent's previous action as context and reinforced if the next action matched the sequence I wanted and punished if it did not. By the end of the interaction, the agent is executing actions in the expected sequence, using the previously executed action as context to choose the next one.

while True:
    antecedente = definir_antecedente()

    acao = agente.proxima_acao(antecedente)

    resultado_da_acao = executar_acao(acao)

    if resultado_da_acao == resultado_positivo:
        agente.reforcar()

PT-BR

## Instalação

Para instalar a biblioteca, use o `pip`:

pip install behavioralflow


EN-US

## Installation

To install the library, use pip:

pip install behavioralflow

