try:
    arquivos_contatos = open('dados/nocontatos.csv', encoding='latin_1')

    for linha in arquivos_contatos:
        print(linha, end="")
    
except FileNotFoundError:
    print("Arquivo não encontrado")

except PermissionError:
    print("Não possui permissão de escrita no arquivo")
        
finally:
    arquivos_contatos.close()

