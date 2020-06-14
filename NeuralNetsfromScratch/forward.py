import numpy as np
from activation_fns import sigmoid,relu
def forward_node(X,W,b):
    Z = np.dot(W,X)+b
    cache = (X,W,b)
    return Z,cache

def forward_layer(Alminus,W,b,activation):
    Z,lincache = forward_node(Alminus,W,b)
    if(activation=='sigmoid'):
        Al,actcache = sigmoid(Z)
    else:
        Al,actcache = relu(Z)
    cache = (lincache,actcache)
    return Al,cache
def forward_model(X,parameters):
    L=len(parameters)//2
    caches = []
    A = X
    for i in range(1,L):
        Aprev = A
        A,cache = forward_layer(Aprev,parameters['W'+str(i)],parameters['b'+str(i)],activation='relu')
        caches.append(cache)
    AL,cache = forward_layer(A,parameters['W'+str(L)],parameters['b'+str(L)],activation='sigmoid')
    caches.append(cache)
    return AL,caches