# -*- coding: utf-8 -*-
"""Mod1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YUGATpF5K3ACaZD4D_IHAW1AZEObEJbr
"""

idade=30
print(idade)
idade=27
print(idade)
name='antonio'
print(name)

preco_banana = 1000
tipo_preco_banana = type(preco_banana)
print(preco_banana)
print(tipo_preco_banana)

juros = 0.05
tipo_juros = type(juros)
print(juros)
print(tipo_juros)

primeiro_nome = 'antonio'
print(primeiro_nome)
print(type(primeiro_nome))

usuario_maior_de_idade = True
print(usuario_maior_de_idade)
print(type(usuario_maior_de_idade))

telefone_fixo = None
print(telefone_fixo)
print(type(telefone_fixo))

print(type(37))
print(type(0.03))
print(type(1+2j))

itens = 1
print(itens)
itens += 2
print(itens)
itens += 10
print(itens)

preco = 47
qtd = 2
total = preco // qtd
print(total)
print(type(total))

print(int(3.3))
print(float(20))
print(complex(1))

svv = 153.98
sqv = 3
tkt = svv / sqv
print(tkt)
print(int(tkt))

nome = 'antonio'
sobrenome = 'andrade'
print(nome + ' ' + sobrenome)

apresentacao = 'olá, meu nome é' + ' ' + nome + ' ' + sobrenome + '.'
print(apresentacao)
print(type(apresentacao))

apresentacao_final = f'olá, meu nome é {nome} {sobrenome}.'
print(apresentacao_final)

email = 'antoniocmajr@gmail.com'
print('-1: ' + (email[-1]))
print('-3: ' + (email[-3]))

usuario = (email[0:12])
print(usuario)

provedor = (email[12:22])
print(provedor)

endereco = 'Servidão Antônio Cipriano Pereira, 168 - Itacorubi, Florianópolis - SC, 88034-280'
print(endereco)
print(endereco.upper())
print(endereco.find('SC'))
print(endereco.replace('Servidão','Rua'))

idade = 26
print(type(idade))

idade = str(idade)
print(idade)
print(type(idade))

faturamento = 'R$ 35 mi'
print(faturamento)
print(type(faturamento))

faturamento = (faturamento[3:5])
valor = int(faturamento)
print(valor)
print(type(valor))

# startup adquirida
latlon = '-22.005320;-47.891040'
posicao_char_divisao = latlon.find(';')
print(posicao_char_divisao)
lat = (latlon[0:posicao_char_divisao])
print(lat)
lon = (latlon[posicao_char_divisao+1:len(latlon)])
print(lon)
print(len('10'))

verdadeiro = True
print(verdadeiro)
print(type(verdadeiro))

saldo_conta = 200
saque = 100

pode_executar_saque = saque <= saldo_conta
print(pode_executar_saque)

cod_seguranca = '852'
cod_seguranca_cadastro = '851'

pode_efetuar_pagamento = cod_seguranca == cod_seguranca_cadastro
print(pode_efetuar_pagamento)

# tabela da verdade

print(True | True)
print(True | False)
print(False | False)
print(False | True)

print(True & True)
print(True & False)
print(False & False)
print(False & True)

print(not True)
print(not False)

idade = 19
tipo_sangue = 'O-'
filhos = 0
tel_fixo = None
tel_fixo = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(tel_fixo))

usuario = 'andre.perez'
senha = 'andre123'

usuario_cadastro = 'andre.perez'
senha_cadastro = 'andre321'

pode_entrar_usuario = usuario == usuario_cadastro
pode_entrar_senha = senha == senha_cadastro
print(pode_entrar_usuario)
print(pode_entrar_senha)

pode_entrar = pode_entrar_usuario & pode_entrar_senha
print(pode_entrar)