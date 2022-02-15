try:
    arquivos_contatos = open('dados/nocontatos.csv', encoding='latin_1')

    for linha in arquivos_contatos:
        print(linha, end="")
    
except FileNotFoundError:
    print("Arquivo n�o encontrado")

except PermissionError:
    print("N�o possui permiss�o de escrita no arquivo")
        
finally:
    arquivos_contatos.close()

