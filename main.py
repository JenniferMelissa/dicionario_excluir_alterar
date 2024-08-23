#dicionario
#é o terceiro tipo de colecoes
#ele é uma lista, só que cada valor da lista tem uma chave e essa "chave" é uma especie de palavra que representa aquele valor da lista
#dicionario usa chaves 
#o usuario é um objeto e esse objeto ele tem atributos e cada atributo na verdade é uma chave que representa o valor do objeto (esse atriuto tem significado)
#o valor é representado por uma chave(string)
#é mais util que uma lista, se quer guardar varios dados de um usuario, você usa o dicionario, e assim os valores estarao relacionados, mas é um banco de dados nao relacional, somente os atributos dentro da chave que sao relacionados com a chave
#chave possibilita guardar varios atributos de varios tipos
#imita a mesma estrutura do json
#consegue fazer as mesmas operacoes feitas em uma lista


usuario = {
#objeto     
    'nome':'Alex Machado',
     #chave  #valor
    'idade':'39',
    'profissao':'programador'
} 

#adicionar umam nova chave
#usuario['email'] = 'alex@gmail.com'
usuario['email'] = input('Informe email: ')

#alterar novo valor da chave
usuario['nome'] = input('Informe novo nome: ')

#excluir a chave, e automaticamente exclui o valor
del usuario['idade']



#exibir valores do dicionario na tela
#1 -melhor forma pois ela nao costuma dar erro se voce chamar a chave caso nao exista
# print(usuario.get('nome'))
# print(usuario.get('idade'))
# print(usuario.get('profissao'))
# print(usuario.get('email')) 


#2 - pior forma de mostrar os valores, se voce chamar uma chave que nao existe o seu programa vai crachar e dar erro 
# print(usuario['nome'])
# print(usuario['idade'])
# print(usuario['profissao'])


#3 - outra forma de exibir, mais usada
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')

