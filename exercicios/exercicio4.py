'''
Crie um algoritmo em PYTHON que leia a idade de uma pessoa e informe a sua classe eleitoral:
- não eleitor (abaixo de 16 anos);
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);

'''

#lendo idades 

idade = int(input('informe sua idade : '))

#definindo que vota ou nao
if idade < 16 :
    print ('nao eleitor')
    
elif idade > 18 and idade < 65 :
    print ('eleitor obrigatorio')
    
elif idade == 16 or idade >= 18  or idade >65 :
    print ('eleitor facultativo')