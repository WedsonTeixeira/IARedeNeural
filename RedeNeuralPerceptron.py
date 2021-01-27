quantidadeTerminais = 9
quantidadePadroes = 2
taxaAprendizado = 0.4

limiar = 1
caracterT = 1
caracterH = -1

padroes = [[limiar,1,1,1,0,1,0,0,1,0,caracterT], 
           [limiar,1,0,1,1,1,1,1,0,1,caracterH]]

'''[[
        1,1,1,
        0,1,0,      caractere T
        0,1,0
    ], 
    [
        1,0,1,
        1,1,1,      caracter H
        1,0,1
    ]]'''

pesos = []
pesos.append(0)             #limiar
pesos.append(1)             #w1
pesos.append(0.5)           #w2
pesos.append(1)             #w3
pesos.append(0.5)           #w4
pesos.append(1)             #w5
pesos.append(0.5)           #w6
pesos.append(0.5)           #w7
pesos.append(0.5)           #w8
pesos.append(0.5)           #w9

#Treinamento
isTreined = False

while(not isTreined):
    contador = 0
    for indexPadroes in range(quantidadePadroes):
        v = 0
        for indexTerminais in range(quantidadeTerminais+1):
            v = v + padroes[indexPadroes][indexTerminais] * pesos[indexTerminais]
        v = round(v, 2)
    
        if v >= 0 :
            y = 1
        else:
            y = -1
        
        if(y != padroes[indexPadroes][quantidadeTerminais+1]):
            for indexPesos in range(len(pesos)):
                pesos[indexPesos] = round(pesos[indexPesos] + (taxaAprendizado * padroes[indexPadroes][indexPesos]) * (padroes[indexPadroes][quantidadeTerminais+1] - (y)),2)
        else:
            contador = contador + 1
    if(contador == quantidadePadroes):
        isTreined = True

print(pesos)

#Testes
teste = []

indefinido = 0
                                              
teste = [[limiar,1,1,1,
                 0,1,0,
                 0,1,0,indefinido],     #letra T

         [limiar,1,0,1,
                 1,1,1,
                 1,0,1,indefinido],     #letra H 

         [limiar,0,0,0,
                 1,0,1,                 #letra not T
                 1,0,1,indefinido],

         [limiar,0,1,0,
                 0,0,0,                 #letra not H
                 0,1,0,indefinido]]

                 

for indexTeste in range(len(teste)):
    v = 0
    for indexTerminais in range(quantidadeTerminais+1):
        v = v + teste[indexTeste][indexTerminais] * pesos[indexTerminais]
    v = round(v, 2)

    if v >= 0 :
        teste[indexTeste][quantidadeTerminais+1] = 1
    else:
        teste[indexTeste][quantidadeTerminais+1] = -1

for index in range(len(teste)):

    if(teste[index][quantidadeTerminais+1] == 1):
        clasificacao = 'Letra T'
    else:
        clasificacao = 'Letra H'
    
    print(clasificacao)