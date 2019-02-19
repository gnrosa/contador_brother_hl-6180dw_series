import requests
import re
import time

print('Lendo lista...')
lista = ['192.168.0.51',
'192.168.0.52',
'192.168.0.53',
'192.168.0.54',
'192.168.0.55',
'192.168.0.56',
'192.168.0.57',
'192.168.0.58',
'192.168.0.61',
'192.168.0.63',
'192.168.0.64',
'192.168.0.65',
'192.168.0.66',
'192.168.0.67',]

print('Configurando nome do arquivo...')
agora = time.ctime()
agora = agora.split()
nome_arquivo = 'Contador_Brother_HL-6180DW_series_{}_{}_{}_{}.csv'.format(agora[1], agora[2], agora[4], agora[3].replace(':','-'))
data = str('{}/{}/{}'.format(agora[2], agora[1], agora[4]))

print('Criando arquivo...')
ref_arquivo = open(nome_arquivo, 'w')

print('Exportando dados...')
ref_arquivo.write('date;{}\ntime;{}\n'.format(data, agora[3]))
for impressora in lista:
    try:
        requisicao = requests.get('http://{}/general/information.html?kind=item'.format(impressora))
        procura_contador = re.findall(r'Counter</dt><dd>\w+</dd>', requisicao.text)
        conversor = ''.join(str(e) for e in procura_contador)
        contador_final = re.findall(r'\d+', conversor)
        #print('{};{}'.format(impressora, contador_final[0]))
        ref_arquivo.write('{};{}\n'.format(impressora, contador_final[0]))

        #print('Impressora: {}\nStatus: {}\n'.format(impressora, requisicao))
    except Exception as erro:
        print(erro)
print('Finalizado')
