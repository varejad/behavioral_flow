import random, copy, json

class Aprendente:
  # tem que validar se 'acoes' é um dicionario onde as chaves são tuplas e os valores são listas...
  def __init__(self, acoes:dict, prob_variacao=0.0, taxa_extincao=0.1, k=1):
    if not isinstance(acoes, dict):
      raise TypeError("O atributo 'acoes' deve ser uma dicionario onde as chaves são tuplas e os valores são listas...")
    
    self.prob_variacao = prob_variacao
    self.acao_atual = ""
    self.refocado = True
    self.taxa_extincao = taxa_extincao
    self.k = k
    self.variou_na_ultima_tentativa = False
    self.antecedentes_e_respostas = {"":acoes}
    self.respostas_atuais = {}
    self.antecedente_atual = []

  def proxima_acao(self, antecedente):
    """
    Retorna uma lista com ações
    """

    # Verifica se é lista
    if not isinstance(antecedente, list):
        raise TypeError("O atributo 'antecedente' deve ser uma lista.")

    # Converte todos os itens para string
    antecedente = [str(item).strip() for item in antecedente]

    # Verifica se a lista não é vazia e não contém apenas strings vazias
    if not antecedente or all(item == "" for item in antecedente):
        raise ValueError("O atributo 'antecedente' não pode ser vazio nem conter apenas strings vazias.")

    # define o antecedente atual como o parametro de antecedente recebido
    self.antecedente_atual = antecedente

    # resgata o aprendizado relacionado ao antecedente atual e passa para respostas_atuais, se não houver será definodo como respostas_padrao
    self.respostas_atuais = self._resgatar_aprendizado()

    # verifica se foi reforçado, caso não, entra na função de extinção e depois de variação
    if not self.refocado:
      self._extincao()
      variacao = self._variacao()
      if variacao is not None:
        self.acao_atual = variacao
        return self.acao_atual.split(",,")

    self.refocado = False
    self.acao_atual = self._definir_acao()
    return self.acao_atual.split(",,")

  def _definir_acao(self):
    # define os parametro para a funcao choices(), no caso a lista de opções a serem escolhidas e os pesos relativos
    # Passo 1 — extrair opções e pesos originais
    opcoes = list(self.respostas_atuais.keys())
    pesos_das_opcoes = [valor[1] - valor[0] for valor in list(self.respostas_atuais.values())]
    pesos_amplificados = pesos_das_opcoes.copy()

    # Passo 2 — amplificar diferenças (fator k > 1 amplia, k < 1 reduz)
    k = self.k
    media = sum(pesos_das_opcoes) / len(pesos_das_opcoes)
    pesos_amplificados = [media + k * (p - media) for p in pesos_das_opcoes]

    # Passo 3 — garantir que nenhum peso seja <= 0
    minimo = min(pesos_amplificados)
    if minimo <= 0:
        epsilon = 1e-6
        pesos_amplificados = [p - minimo + epsilon for p in pesos_amplificados]
        
    #print(f"antecedentes: {self.antecedente_atual}\namplificado: {pesos_amplificados}")

    return random.choices(opcoes, weights=pesos_amplificados)[0] # essa função retorna lista

  def _resgatar_aprendizado(self):
    """Essa função resgata o aprendizado relacionado a cada item do antecedente, bem como o aprendizado relaciionado ao antecedente como um todo (pode haver erros devido a mudança na ordem dos itens) e unifica em um unico dicionário"""

    aprendizado_acumulado = []

    for item in self.antecedente_atual: 
      if item in self.antecedentes_e_respostas.keys(): # Rever como isso se comporta no caso de variação
        aprendizado_acumulado.append(self.antecedentes_e_respostas[item])
      else:aprendizado_acumulado.append(self.antecedentes_e_respostas[""])
        #print(f"chave: {item} valor: {self._antecedentes_e_respostas[item]}")
      
    str_antecedente_atual = ",".join(self.antecedente_atual) # pega a lista e transforma em string colocando vírgula entre cada item

    if str_antecedente_atual in self.antecedentes_e_respostas.keys():
      aprendizado_acumulado.append(self.antecedentes_e_respostas[str_antecedente_atual])
      #print(f"chave: {str_antecedente_atual} valor: {self._antecedentes_e_respostas[str_antecedente_atual]}")
    else: aprendizado_acumulado.append(copy.deepcopy(self.antecedentes_e_respostas[""]))
    
    #print(f"aprendizado acumulado: {aprendizado_acumulado}")

    respostas_atuais_unificadas = {}

    # 1. Pegamos as chaves de um dos dicionários (assumindo que todas são iguais)
    chaves = self.antecedentes_e_respostas[""].keys()

    # 2. Iteramos sobre cada chave
    for chave in chaves:
      soma_do_segundo_elemento = 0 #serve para fazer a soma do fator de reforçamento, PENSAR SOBRE CUSTO

      # 3. Iteramos sobre a lista de dicionários para acumular a soma
      for resp in aprendizado_acumulado:
        # Acessamos o valor (que é uma lista) e somamos o elemento de índice 1
        soma_do_segundo_elemento += resp[chave][1]

      # 4. Criamos a nova lista de valor para o dicionário unificado.
      #    O primeiro elemento é 0 (ou você pode pegar o primeiro elemento do primeiro dicionário: dicionario_A[chave][0])
      #    O segundo elemento é a soma calculada.
      respostas_atuais_unificadas[chave] = [aprendizado_acumulado[0][chave][0], soma_do_segundo_elemento]

    #print(f"respostas unificadas: {respostas_atuais_unificadas}")

    return respostas_atuais_unificadas
  

  def reforcar(self, magnitude=1, acao=None):
    #preciso pensar no que acontece quando uma ação que não existe em um certo antecedente for reforçada (isso pode acontecer quando houver variação)
    #print(f"REFORÇOU")
    self.refocado = True
    if acao == None: acao = self.acao_atual #quando o parametro 'acao' não é passado

    #todos os antecedentes como um só em uma única string
    str_antecedente_atual = ",".join(self.antecedente_atual)
    if not str_antecedente_atual in self.antecedentes_e_respostas:
      self.antecedentes_e_respostas[str_antecedente_atual] = copy.deepcopy(self.antecedentes_e_respostas[""])

    self.antecedentes_e_respostas[str_antecedente_atual][acao][1] = max(self.antecedentes_e_respostas[str_antecedente_atual][acao][1] + magnitude, 0)
    #self.antecedentes_e_respostas[str_antecedente_atual][acao][1] += magnitude if self.antecedentes_e_respostas[str_antecedente_atual][acao][1] + magnitude > 0 else -self.antecedentes_e_respostas[str_antecedente_atual][acao][1]

    # tentar implementar uma maneira de redestribuir o valor do r+ (quanto mais uma resposta é reforçada em relação às outras respostas possíveis diante daquele S mais ela ganhar r+)
    for item in self.antecedente_atual:
      if not item in self.antecedentes_e_respostas: #verifica se não existe o antecedente individual no dicionário
        self.antecedentes_e_respostas[item] = copy.deepcopy(self.antecedentes_e_respostas[""]) #cria o antecedente individual no dicionário a partir das respostas padrão
      
      self.antecedentes_e_respostas[item][acao][1] = max(self.antecedentes_e_respostas[item][acao][1] + magnitude, 0)
      #self.antecedentes_e_respostas[item][acao][1] += magnitude if self.antecedentes_e_respostas[item][acao][1] + magnitude > 0 else -self.antecedentes_e_respostas[item][acao][1]

  def _extincao(self):
    if self.taxa_extincao <= 0:
      return
    
    acao = self.acao_atual
    taxa = self.taxa_extincao
  
    #todos os antecedentes como um só em uma única string
    str_antecedente_atual = ",".join(self.antecedente_atual)
    if str_antecedente_atual in self.antecedentes_e_respostas:

      self.antecedentes_e_respostas[str_antecedente_atual][acao][1] = max(self.antecedentes_e_respostas[str_antecedente_atual][acao][1] * (1 - taxa), 0)
      #self.antecedentes_e_respostas[str_antecedente_atual][acao][1] *= (1 - taxa) if self.antecedentes_e_respostas[str_antecedente_atual][acao][1] * (1 - taxa) > 0 else 0
      #print("EXTINGUIU")
    for item in self.antecedente_atual:
      if item in self.antecedentes_e_respostas:

        self.antecedentes_e_respostas[item][acao][1] = max(self.antecedentes_e_respostas[item][acao][1] * (1 - taxa), 0)
        #self.antecedentes_e_respostas[item][acao][1] *= (1 - taxa) if self.antecedentes_e_respostas[item][acao][1] * (1 - taxa) > 0 else 0
        #print("EXTINGUIU")
        
  def _variacao(self):
    if self.variou_na_ultima_tentativa == True:
      self.variou_na_ultima_tentativa = False
      return None
    if random.random() < self.prob_variacao:
      novo_passo = self._definir_acao() 
      custo_da_variacao = self.respostas_atuais[self.acao_atual][0] + self.respostas_atuais[novo_passo][0]/2
      fator_da_variacao = self.respostas_atuais[self.acao_atual][1]*0.75
      # ainda precisa incluir nos antecedentes especificos onde a variação surgiu
      self.antecedentes_e_respostas[""][",,".join([self.acao_atual, novo_passo])] = [custo_da_variacao,fator_da_variacao] #Inclui a variação nas respostas padrão, mas está incluíndo com uma taxa de r+ mais alta
      self.variou_na_ultima_tentativa = True
      return ",,".join([self.acao_atual, novo_passo])
    
    else: return None
  
  def logs(self, aviso_adicional = "sem aviso"):
    print("#### LOGS #####\n")
    print(f"aviso adicional: {aviso_adicional} \n")
    print(f"antecedente: {self.antecedente_atual}")
    print(f"respostas atuais: {self.respostas_atuais}")
    print(f"ação atual: {self.acao_atual}")
    print(f"antecedentes e respostas: {self.antecedentes_e_respostas}")
    print("\n####Fim dos logs####")