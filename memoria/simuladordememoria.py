# Inicializa a memória com 16 espaços vazios (cada espaço tem 8 bits)
memoria = ["00000000"] * 16

# Loop para interação com o usuário
while True:
    # Lê a entrada do usuário e converte para maiúsculas
    entrada = input("Digite w para escrever, R para ler, L para listar toda a memória e qualquer tecla para parar: ").upper()
    
    # Se a entrada for "W" (escrever):
    if entrada == "W":
        # Lê o endereço de 4 bits
        endereco = int(input("Digite o endereço de 4 bits: "))
        # Verifica se o endereço é válido
        if endereco != 4:
            print("Endereço inválido!")
            continue
        # Lê o dado de 8 bits a ser armazenado na memória
        dado = input("Digite o dado de 8 bits: ")
        # Verifica se o dado é válido
        if len(dado) != 8:
            print("Dado inválido!")
            continue
        # Armazena o dado na posição de memória indicada pelo endereço
        memoria[endereco] = dado
    
    # Se a entrada for "R" (ler):
    elif entrada == "R":
        # Lê o endereço de memória a ser lido
        endereco = int(input("Digite o endereço: "))
        # Lê o dado da posição de memória indicada pelo endereço
        dado = memoria[endereco]
        # Imprime o dado na tela
        print(dado)
    
    # Se a entrada for "L" (listar):
    elif entrada == "L":
        # Imprime todos os estados da memória
        print("Todos os estados:")
        #O loop "for i in range(16)" executa o bloco de código nele contido 16 vezes, com a variável i assumindo valores de 0 a 15 
        # Dentro do loop, a instrução "print(f"{memoria[i]}")" é executada para cada valor de i, exibindo o conteúdo armazenado em cada um dos 16 endereços de memória da variável "memoria".
        for i in range(16):
            print(f"{memoria[i]}")
    
    # Se a entrada for qualquer outra tecla, encerra o programa
    else:
        break

# Imprime mensagem de encerramento do programa
print("Programa encerrado.")
