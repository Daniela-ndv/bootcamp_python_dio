# Árvore de decisões que retorne qual é a fruta com base no peso e no tipo de casca.

from sklearn import tree 

# Considerando: 
# Em X [peso em gramas, tipo de casca (1=lisa ou 0=irregular)]
# Em Y [5=maçã e 10=laranja]

# Dados para o aprendizado: 
X = [[140,1], [130,1], [150,0], [170,0]]
Y = [5, 5, 10, 10]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# Entrada de [gramas, tipo de casca]
print(clf.predict([[100,0]]))
