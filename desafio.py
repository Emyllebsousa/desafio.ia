def distancia_edicao(a, b):
    len_a = len(a)
    len_b = len(b)

    # Inicializar a matriz de distância
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    # Inicializar a primeira linha e a primeira coluna
    for i in range(len_a + 1):
        dp[i][0] = i
    for j in range(len_b + 1):
        dp[0][j] = j

    # Preencher a matriz de distância
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    # A última célula contém a distância de edição
    return dp[len_a][len_b]

# Exemplos de uso
a1 = "asar"
b1 = "casa"
print(distancia_edicao(a1, b1))  # Saída: 2

a2 = "inserir"
b2 = "inserção"
print(distancia_edicao(a2, b2))  # Saída: 3
