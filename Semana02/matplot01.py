import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Redimenciona grafico
plt.figure(figsize=(8,5), dpi=100)

# Primeira linha
plt.plot(x,y, label='2x', color='blue', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

# notação simplificada
# plt.plot(x,y, 'b^--', label='2x')

## Segunda Linha

# determina intervalo e passo
x2 = np.arange(0,4.5,0.5)

# Plota parte do grafico em linha
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

# Plota a outra parte em ponto
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Titulo
plt.title('Primeiro Grafico!', fontdict={'fontname': 'consolas', 'fontsize': 15})

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Define escala do gráfico
plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# Legenda
plt.legend()

# Salva imagem com 300 dpis para uma boa qualidade
plt.savefig('mygraph.png', dpi=300)

# Mostra o plot
plt.show()