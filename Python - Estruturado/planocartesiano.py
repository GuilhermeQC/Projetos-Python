import matplotlib.pyplot as plt

# Dados para o plano cartesiano
x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

# Criar o gráfico
# Conecta os pontos com linhas e adiciona marcadores
plt.plot(x, y, marker='o')

# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar título ao gráfico
plt.title('Plano Cartesiano Simples')

# Exibir o gráfico
plt.grid(True)  # Adicionar a grade ao plano cartesiano
plt.show()


