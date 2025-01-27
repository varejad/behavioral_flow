import random

class Aprendente:

  # tem que validar se 'acoes' é um dicionario onde as chaves são tuplas e os valores são listas...
  def __init__(self, acoes:dict, variar=False):
    if not isinstance(acoes, dict):
      raise TypeError("O atributo 'acoes' deve ser uma dicionario onde as chaves são tuplas e os valores são listas...")

    self.variar = variar
    self._acao_atual = ()
    self._refocado = False
    self._ultima_acao = []
    self.respostas_padrao = acoes
    self._antecedentes_e_respostas = {():self.respostas_padrao}
    self.respostas_atuais = []
    self.antecedente_atual = []

  def proxima_acao(self, antecedente:list):
    # validar se 'antecedente' é uma lista
    if not isinstance(antecedente, list):
      raise TypeError("O atributo 'antecedente' deve ser uma lista.")
    
    # verifica se a ação atual não tem mais um passo a ser realizado, se tiver retorna a ação sem o passo já realizado
    if len(self._acao_atual) > 1:
      self._acao_atual = self._acao_atual.pop(0)
      return self._acao_atual
    
    # antes de definir a próxima ação, salva na variável _ultima_acao qual foi a ultima ação realizada
    # self._ultima_acao = self._acao_atual

    # define o antecedente atual como o parametro de antecedente recebido
    self.antecedente_atual = antecedente

    # resgata o aprendizado relacionado ao antecedente atual e passa para respostas_atuais, se não houver será definodo como respostas_padrao
    self.respostas_atuais = self.resgatar_aprendizado()

    # verifica se foi reforçado, caso não, entra na função de variação
    if not self._refocado:
      variacao = self.variacao()
      print(f"variação: {variacao}")
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
    #procurar o index na lista de todos os aprendizados onde o antecedente seja igual ao parametro recebido
    if tuple(self.antecedente_atual) in self._antecedentes_e_respostas.keys():
      return self._antecedentes_e_respostas[tuple(self.antecedente_atual)]
    else:
      return self.respostas_padrao

  def salvar_aprendizado(self):
    self._antecedentes_e_respostas[tuple(self.antecedente_atual)] = self.respostas_atuais

  def reforcar(self, magnitude=1, acao=None):
    self._refocado = True
    if acao == None: acao = self._acao_atual
    
    self.respostas_atuais[acao][1] += magnitude

    self.salvar_aprendizado()

  #do jeito que tá aqui vai variar 100% das vezes que for chamada essa função
  #falta definir o custo e ver sobre a parte de salvar
  def variacao(self):
    print("variação")
    # verifica se a opção de variar está True
    if self.variar:    
      #retornar isso abaixo e ver como finalizar a função que chamou essa
      #variacao = tuple(list(self._acao_atual) + list(self.definir_acao()))
      #self._acao_atual = variacao  
      return tuple(list(self._acao_atual) + list(self.definir_acao()))

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

"""