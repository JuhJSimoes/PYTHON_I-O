arquivos_contatos = open('dados/contatos_escrita.csv', encoding= 'latin_1', mode = 'a')
contato = '11,Carol,carol@carol.com.br\n'
arquivos_contatos.write(contato)