import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, funcao):
    x = np.arange(-5, 5, 0.5)  # Corrigido para 0.5
    y = funcao(x)  # Aplica a função diretamente no array do Numpy
    plt.plot(x, y)
    plt.title(titulo)
    plt.grid(True)  # Adiciona uma grade para melhor visualização
    plt.xlabel('x')  # Rótulo do eixo X
    plt.ylabel('y')  # Rótulo do eixo Y
    plt.show()

# Função ReLU corrigida
def relu(x):
    return np.maximum(0.0, x)

# Função Sigmoid corrigida
def sigmoid(x, a=1):
    return 1 / (1 + np.exp(-a * x))

# Tangente Hiperbólica 
def tanh(x, a=1, b=1):
    return np.tanh(a * x + b) 

# Linear (não precisa de correção)
def linear(x):
    return x

# Plotando os gráficos
plot('ReLU', relu)
plot('Sigmoid', sigmoid)
plot('Tangente Hiperbólica', tanh)
plot('Linear', linear)
