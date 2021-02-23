##Desafio 2 Operadores lógicos
 
'''
um determinado trabalhador possui duas entrevistas, um na terça
outro na quinta e prometeu a família uma promessa:
se os dois trabalhos derem certo, vai comprar uma TV de 50 e tomar sorvete com a família
se apenas um der certo, vai comprar uma TV de 32 e tomar sorvere com a família
se nenhum der certo, terá apenas mais saúde!!
'''

trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
saude = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}".format(tv_50, tv_32, sorvete, saude))



