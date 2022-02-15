arquivo01 = open('dados/contatos_escrita.csv', encoding='latin_1', mode='w')
arquivo02 = open('dados/contatos_escrita.csv', encoding='latin_1', mode='a+')

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

arquivo01.write(contato_carol)
arquivo02.write(contato_andreza)

arquivo01.close()
arquivo02.close()