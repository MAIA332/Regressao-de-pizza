import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

Diametros = [[7],[10],[15],[30],[45]]
precos = [[8],[11],[16],[38.5],[52]]

def analise_exploratoria():
    plt.figure()
    plt.xlabel('Diametro (cm)')
    plt.ylabel('Preco (R$)')
    plt.title('Diametro x preco')
    plt.plot(Diametros,precos,'k.')
    plt.axis([0,60,0,60])
    plt.grid(True)
    plt.show()

def model(diametro):
   # Preparando os dados de treino

    # Vamos chamar de X os dados de diâmetro da Pizza.
    X = [[7], [10], [15], [30], [45]]

    # Vamos chamar de Y os dados de preço da Pizza.
    Y = [[8], [11], [16], [38.5], [52]]

    modelo = LinearRegression()

    modelo.fit(X,Y)

    mp = modelo.predict([[diametro]])
    cf = modelo.coef_
    
    print("Uma pizza de x cm de diâmetro deve custar: R$%.2f" % mp)
    return mp,cf

diam = int(input('Digite o diametro que deseja prever o valor: '))
predict,coef = model(diam)
analise_exploratoria()
print(coef)
print(predict)

