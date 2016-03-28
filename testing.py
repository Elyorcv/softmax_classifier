import numpy as np
from softmax import Softmax
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target
reg_strength = 1e-4
batch_size = 50
epochs = 1000
learning_rate = 1
sm = Softmax(batch_size=batch_size, epochs=epochs, learning_rate=learning_rate, reg_strength=reg_strength)
sm.train(X, y)
pred = sm.predict(X)
print np.mean(np.equal(y, pred))
