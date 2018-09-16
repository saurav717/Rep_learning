import numpy as np
import scipy as sp
import scipy
import matplotlib.pyplot as plt
import subprocess

def dist(A,B):
    return np.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)

def centroid(G1):
    x = 0
    y = 0
    for i in range(0,len(G1)):
        x += G1[i][0]
        y += G1[i][1]
    x = x/len(G1)
    y = y/len(G1)
    Cen = [x , y]
    return Cen

def total(G,X,K):



########################################################
####### This is for generating points

K = input('enter number of clusters')
X = np.random.random(500)
X = np.reshape(X,(250,2))

threshold = 0.015

k = 250/K
G = []

#print(X[1])
#print(X[1][1] - X[1][0])
#print(X[2][1] - X[2][0])

for i in range(0,K):
    #print(X[k*i])
    G = np.append(G,X[k*i])

G = np.reshape(G,(K,2))
#G = np.hstack((G,np.zeros((K,1))))
print(G)

#dist(X[0], X[1])
dst = 0
Ind = []
for i in range(0,250):
    D = []   # keep this temporary
    for j in range(0,K):
        D = np.append(D,dist(X[i],G[j]))
    Ind = np.append(Ind,int(np.argmin(D,0)))
    #D1.append(D1,D[D.index(min(D))])

print(Ind)
#print(len(Ind))
Ind = np.reshape(Ind,(250,1))
X = np.hstack((X,Ind))
#print(X)
Kl = []
for i in range(0,K):
    GS = []
    for j in range(0,250):
            if(int(X[j][2]) == i):
                GS = np.append(GS,X[j])
                GS = np.reshape(GS,(len(GS)/3,3))
    Kl = np.append(Kl,centroid(GS))

Kl = np.reshape(Kl,(K,2))
for i in range (0,K):
    dst += dist(Kl[i],G[i])
G = Kl
print(G)
print(dst)
