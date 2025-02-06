import random, copy

class Aprendente:
  # tem que validar se 'acoes' é um dicionario onde as chaves são tuplas e os valores são listas...
  def __init__(self, acoes:dict, variar=False, prob_variacao=0.25):
    if not isinstance(acoes, dict):
      raise TypeError("O atributo 'acoes' deve ser uma dicionario onde as chaves são tuplas e os valores são listas...")
    
    self.prob_variacao = prob_variacao
    self.variar = variar
    self._acao_atual = tuple
    self._refocado = True
    self._variou_na_ultima_tentativa = False
    self._antecedentes_e_respostas = {():acoes}
    self.respostas_atuais = []
    self.antecedente_atual = ()

  def proxima_acao(self, antecedente:tuple):
    if not isinstance(antecedente, tuple) or antecedente == ():
      raise TypeError("O atributo 'antecedente' deve ser uma tupla e deve ser diferente de ().")

    # define o antecedente atual como o parametro de antecedente recebido
    self.antecedente_atual = antecedente

    # resgata o aprendizado relacionado ao antecedente atual e passa para respostas_atuais, se não houver será definodo como respostas_padrao
    self.respostas_atuais = self.resgatar_aprendizado()

    # verifica se foi reforçado, caso não, entra na função de variação
    if not self._refocado:
      variacao = self.variacao()
      if variacao is not None:
        self._acao_atual = variacao
        return self._acao_atual

    self._refocado = False
    self._acao_atual = self.definir_acao()
    return self._acao_atual

  def definir_acao(self):
    # define os parametro para a funcao choices(), no caso a lista de opções a serem escolhidas e os pesos relativos
    opcoes = list(self.respostas_atuais.keys())
    pesos_das_opcoes = [valor[1] - valor[0] for valor in list(self.respostas_atuais.values())]

    return random.choices(opcoes, weights=pesos_das_opcoes)[0]

  def resgatar_aprendizado(self):
    if self.antecedente_atual in self._antecedentes_e_respostas.keys():
      return self._antecedentes_e_respostas[self.antecedente_atual]
    else:
      return copy.deepcopy(self._antecedentes_e_respostas[()])

  def salvar_aprendizado(self):
    self._antecedentes_e_respostas[self.antecedente_atual] = self.respostas_atuais

  def reforcar(self, magnitude=1, acao=tuple):
    self._refocado = True
    if acao == tuple: acao = self._acao_atual #quando o parametro 'acao' não é passado
    self.respostas_atuais[acao][1] += magnitude if self.respostas_atuais[acao][1] + magnitude >= 0 else -self.respostas_atuais[acao][1] #garantindo que o fator não seja < 0
    self.salvar_aprendizado()

  def variacao(self):
    if self._variou_na_ultima_tentativa == True:
      self._variou_na_ultima_tentativa = False
      return None
    if self.variar and random.random() <= self.prob_variacao:
      novo_passo = self.definir_acao() 
      custo_da_variacao = self.respostas_atuais[self._acao_atual][0] + self.respostas_atuais[novo_passo][0]/2
      fator_da_variacao = self.respostas_atuais[self._acao_atual][1]*0.75
      #incluir nas respostas atuais, se for reforcado vai salvar, se não não salva
      self.respostas_atuais[tuple(list(self._acao_atual) + list(novo_passo))] = [custo_da_variacao,fator_da_variacao]
      self._variou_na_ultima_tentativa = True
      return tuple(list(self._acao_atual) + list(novo_passo))