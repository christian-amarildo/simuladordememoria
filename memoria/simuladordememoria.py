# Inicializa a memória com 16 espaços vazios (cada espaço tem 8 bits)
memoria = ["00000000"] * 16

# Loop para interação com o usuário
while True:
    entrada = input("Digite w para escrever, R para ler, L para listar toda a memória e qualquer tecla para parar: ").upper()
    
    if entrada == "W":
        endereco = int(input("Digite o endereço de 4 bits: "))
        if endereco < 0 or endereco > 4:
            print("Endereço inválido!")
            continue
        dado = input("Digite o dado de 8 bits: ")
        if len(dado) != 8:
            print("Dado inválido!")
            continue
        memoria[endereco] = dado
    
    elif entrada == "R":
        endereco = int(input("Digite o endereço: "))
        dado = memoria[endereco]
        print(dado)
    
    elif entrada == "L":
        print("Todos os estados:")
        for i in range(16):
            print(f"{memoria[i]}")
    
    else:
        break

print("Programa encerrado.")


