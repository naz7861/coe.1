import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
mu, sigma = 150, 5
data = np.random.normal(mu, sigma, 10000)
#Plotting the z-scores

sns.histplot(data, bins=30, kde=True, stat='probability')
plt.xlabel('Height (Men)')
plt.ylabel('Probability')
plt.xticks(range(155,200,5))
plt.title("Normal Distribution of Men's Height")
plt.show()
from scipy.stats import norm

z = (140-mu)/sigma
p = norm.cdf(z)

print(f"Percentage of men shorter than 183 cm is: {round(p*100,2)}%")

def bayesTheorem(pA, pB, pBA):
    return pA * pBA / pB

pDisease = 1/100
pPositive = ((99/100)*(1/100))+((1/100)*(99/100))
pPositiveGivenDisease= 99/100

pDiseaseGivenPositive=bayesTheorem(pDisease, pPositive, pPositiveGivenDisease)

#Creating a 3x3 matrix
a=np.array([[1,4,5],[2,7,9],[6,8,3]])
print(a)
inva=np.linalg.inv(a)
print(inva)
deta=np.linalg.det(a)
print(deta)
print(eigenvectors)
eigenvalues,eigenvectors=np.linalg.eig(a)
print(eigenvalues)

