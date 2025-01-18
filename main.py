import random

_acao_atual = []
_refocado = False
_ultima_acao = []
respostas_padrao = {}
_antecedentes_e_respostas = {}
respostas_atuais = []

class Aprendente:
  def __init__(self, acoes:dict):
    self.variar = True
    self._acao_atual = []
    self._refocado = False
    self._ultima_acao = []
    self.respostas_padrao = acoes
    self._antecedentes_e_respostas = {():self.respostas_padrao}
    self.respostas_atuais = []

  def proxima_acao(self, antecedente:list):
    # validar se 'antecedente' é uma lista
    if not isinstance(antecedente, list):
      raise TypeError("O atributo 'antecedente' deve ser uma lista.")
        
    # verifica se a ação atual não tem mais um passo a ser realizado, se tiver retorna a ação sem o passo já realizado
    if len(self._acao_atual) > 1:
      self._acao_atual = self._acao_atual.pop(0)
      return self._acao_atual
    
    # antes de definir a próxima ação, salva na variável _ultima_acao qual foi a ultima ação realizada
    self._ultima_acao = self._acao_atual

    # resgata o aprendizado relacionado ao antecedente atual e passa para respostas_atuais, se não houver será definodo como respostas_padrao
    self.respostas_atuais = self.resgatar_aprendizado(antecedente)
    print(self.respostas_atuais)

    self.definir_proxima_acao()  

  def resgatar_aprendizado(self, antecedente):
    #procurar o index na lista de todos os aprendizados onde o antecedente seja igual ao parametro recebido
    if tuple(antecedente) in self._antecedentes_e_respostas.keys():
      return _antecedentes_e_respostas[tuple(antecedente)]
    else:
      return self.respostas_padrao

  def definir_proxima_acao(self):
    total_soma_fatores_restantes = int
    respostas_e_probabilidades = {}
    numero_aleatorio = random.random()

    # subtrai todos os custos do fatores, depois soma todos esses resultados e defini a variável com essa soma
    for resposta in self.respostas_atuais:
      total_soma_fatores_restantes = total_soma_fatores_restantes + (resposta.fator - resposta.custo)
  
    # cria um dicionário com todas as respostas (chave) e probabilidades (valor). Essa probabilidade é obtida com a conta abaixo
    for resposta in self.respostas_atuais:
      respostas_e_probabilidades[resposta.acao] = (resposta.fator - resposta.custo) / total_soma_fatores_restantes

    #ordena as chaves-valores em ordem decrescente de acordo com o valor. Probabilidades vão de 0 a 1
    respostas_e_probabilidades = dict(sorted(respostas_e_probabilidades.items(), key=lambda item: item[1], reverse=True))

    # escolhe a resposta de acordo com o número aleatório
    for resposta in respostas_e_probabilidades:
      if respostas_e_probabilidades[resposta] <= numero_aleatorio:
        return resposta
    # em ocasiões específicas o numero aleatório pode dar maior que qualquer probabilidade, nesse caso retorna a resposta com a maior probabilidade (a ultima da lista)
    return list(self.respostas_atuais.keys())[-1]


class Acao:
  # abaixo lista para salvar objetos instanciados com essa classe
  _acoes = []

  def __init__(self, acao:str, custo:int, fator:int):
    #validando os tipos de variaveis
    if not isinstance(acao, list):
      raise TypeError("O atributo 'acao' deve ser uma lista.")
    if not isinstance(custo, int):
      raise TypeError("O atributo 'custo' deve ser um inteiro.")
    if not isinstance(fator, int):
      raise TypeError("O atributo 'fator' deve ser um inteiro.")
    
    self.acao = acao
    self.custo = custo
    self.fator = fator

    #salvando na lista os objetos instanciados nessa classe
    Acao._acoes.append(self)    

  @classmethod
  def get_acoes(cls):
    return cls._acoes

# vai receber como parâmetro o antecedente e vai retornar uma nova ação
def proxima_acao(antecedente):

  #validar se 'antecedente' é uma lista
  if not isinstance(antecedente, list):
      raise TypeError("O atributo 'antecedente' deve ser uma lista.")

  global _acao_atual, _ultima_acao, respostas_atuais

  # verifica se a ação atual não tem mais um passo a ser realizado, se tiver retorna a ação sem o passo já realizado
  if len(_acao_atual) > 1:
    _acao_atual = _acao_atual.pop(0)
    return _acao_atual
    
  # antes de definir a próxima ação, salva na variável _ultima_acao qual foi a ultima ação realizada
  _ultima_acao = _acao_atual

  #resgata o aprendizado relacionado ao antecedente atual e passa para respostas_atuais, se não houver será definodo como respostas_padrao
  respostas_atuais = resgatar_aprendizado(antecedente)

  definir_proxima_acao()  

def definir_proxima_acao():

  total_soma_fatores_restantes = int
  respostas_e_probabilidades = {}

  # subtrai todos os custos do fatores, depois soma todos esses resultados e defini a variável com essa soma
  for resposta in respostas_atuais:
    total_soma_fatores_restantes = total_soma_fatores_restantes + (resposta.fator - resposta.custo)
  
  # cria um dicionário com todas as respostas (chave) e probabilidades (valor). Essa probabilidade é obtida com a conta abaixo
  for resposta in respostas_atuais:
    respostas_e_probabilidades[resposta.acao] = (resposta.fator - resposta.custo) / total_soma_fatores_restantes

  #ordena as chaves-valores em ordem decrescente de acordo com o valor
  respostas_e_probabilidades = dict(sorted(respostas_e_probabilidades.items(), key=lambda item: item[1], reverse=True))


def resgatar_aprendizado(antecedente):
  #procurar o index na lista de todos os aprendizados onde o antecedente seja igual ao parametro recebido
  if antecedente in _antecedentes_e_respostas:
    return _antecedentes_e_respostas[antecedente]
  else:
    return Acao.get_acoes()
    #return respostas_padrao





"""
OKAY export var compAtual = {comp:[], fator: 0, custo: 0};
var listaDeComp = [];
OKAY export var i = 0;
OKAY var reforcado = true;
OKAY var ultimoComp;
var antecesdentesERespostas = [{antecedente: null, resposta: null}]
var antecedenteAtual
var respostasPadrao
var respostasAtuais
var executarVariacao = {variar: false, fator: 0.85};

export function novoComp(){
  ultimoComp = compAtual;
  resgatarAprendizado()
  if( i < compAtual.comp.length - 1){
    i++
  }
  else if (reforcado){
    criaListaEDefinirComp();
    //else if abaixo: extinção. se o comp existir dentro dos comp atuais (pode ser que não exista pq pode ser que tenha sido variação) entra no bloco
  }
  else if(respostasAtuais.findIndex(resposta => JSON.stringify(resposta) === JSON.stringify(compAtual)) !== -1){
    if (executarVariacao.variar && compAtual.fator/listaDeComp.length > Math.random() + executarVariacao.fator){
      variar()
    }
    else if (compAtual.fator > 4) {
      reforcar(-1)
    }
    else{
      criaListaEDefinirComp()}
  }
  else { 
    criaListaEDefinirComp(); 
  }

  reforcado = false;
  console.log(compAtual.comp + " " + compAtual.fator);
  
}

function criaListaEDefinirComp(){
  listaDeComp = []
  for (const element of respostasAtuais){
    let taxaDeProb = element.fator - element.custo;

    for (let i = taxaDeProb; i > 0; i--){
      listaDeComp.push(element);
    }
  }
  i = 0;
  atualizarCompAtual(JSON.stringify(listaDeComp[Math.floor(Math.random() * listaDeComp.length)]))  
}

export function variar(){
  let listaParaEscolherVariacao = listaDeComp.filter(comp => comp.comp[0] !== "variar");
  //a linha abaixo cria a variavel novoCompVariacao e define assim: seleciona um ítem aleatório da listaParaEscolherVariacao e transforma em string, depois pega a string e transforma em objeto e passa para a variavel criada
  let novoCompVariacao = JSON.parse(JSON.stringify(listaParaEscolherVariacao[Math.floor(Math.random() * listaParaEscolherVariacao.length)]));

  novoCompVariacao.comp = [...ultimoComp.comp, ...novoCompVariacao.comp];
  novoCompVariacao.fator = Math.max(2, compAtual.fator * 0.7) 
  novoCompVariacao.custo = compAtual.custo + novoCompVariacao.custo/2;

  atualizarCompAtual(JSON.stringify(novoCompVariacao))
  i++
  console.log(compAtual.comp);

  //algo dando errado com essa variação, especificamente no calculo do fator. (1)Não ta gerando um fator do tamanho esperado. (2)na lista imprime o fator de um tamanho e depois quando o comportamento variado é chamado imprime de outro jeito

}

export function reforcar(fatorDeIncremento = 3){
  reforcado = true;
  let index = respostasAtuais.findIndex(resposta => JSON.stringify(resposta.comp) === JSON.stringify(compAtual.comp))
  if (index === -1){
    respostasAtuais.push(compAtual);
    index = respostasAtuais.length - 1;
  }
  respostasAtuais[index].fator += fatorDeIncremento
}

export function atualizarAntecedenteAtual(valor){
  antecedenteAtual = valor;
}

export function resgatarAprendizado(){
  let index = antecesdentesERespostas.findIndex(aprendizado => JSON.stringify(aprendizado.antecedente) === JSON.stringify(antecedenteAtual))
  if (index === -1){ 
    respostasAtuais = JSON.parse(JSON.stringify(respostasPadrao));
    console.log(antecedenteAtual)
    salvarAprendizado()
  } else {
    respostasAtuais = antecesdentesERespostas[index].resposta;
  }
}

export function salvarAprendizado(){
  let index = antecesdentesERespostas.findIndex(aprendizado => JSON.stringify(aprendizado.antecedente) === JSON.stringify(antecedenteAtual))
  if (index === -1){ 
    antecesdentesERespostas.push({antecedente: antecedenteAtual, resposta: respostasAtuais})
  }
}

export function atualizarCompAtual(valor){
  compAtual = JSON.parse(valor)
}

export function definirRespostasPadrao(valor){
  respostasPadrao = JSON.parse(valor)
}

----------


"""