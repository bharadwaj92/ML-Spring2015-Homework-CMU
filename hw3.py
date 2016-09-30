import random
import math

pX = {}
pY = {}
pXgY = {}

def logProd(x):
    sum = 0.0
    for i in range(len(x)) :
        sum += math.log(float(x[i]))
    return sum

def NB_XGivenY(Xtrain , Ytrain):
	for j in range(0, len(Xtrain[1])):
		for i in range(0,len(Xtrain)):
			x = str(j) + str(Xtrain[i][j]) + str(Ytrain[i])
			if(Xtrain[i][j]):
				if j in pX:
					pX[j] = pX[j] +1 
				else:
					pX[j] = 1
			if x in pXgY:
				pXgY[x] += 1
			else :
				pXgY[x] = 1		
	for i in pX:
		pX[i] = pX[i]/100
	pY['1'] =0 
	pY['2'] =0
	for z in range(0,len(Ytrain)):
		if(Ytrain[z] ==1 ):
			pY['1'] += 1
		else:
			pY['2'] += 1
	for key in pXgY.keys():
		if(key[2:] == '1'):
			pXgY[key] = pXgY[key]/pY['1']
		elif(key[2:] == '2'):
			pXgY[key] = pXgY[key]/pY['2']
		
	pY['1'] = pY['1']/len(Ytrain)
	pY['2'] = pY['2']/len(Ytrain)
	return pX, pY, pXgY

def NBClassify(Xtrain , Ytrain, Xtest):
	(pX, pY, pXgY) = NB_XGivenY(Xtrain , Ytrain)
	plist = []
	for i in range(len(Xtest)):
		temp1 = 1.0
		temp2 = 1.0
		for j in range(len(Xtest[1])):
			for key in pY.keys():
				x = str(j) + str(Xtrain[i][j]) + str(key)
				if (key == '1'):
					if(Xtest[i][j]== 1):
						temp1 = temp1 * ((pX[j] * pXgY[x])/pY[key])
					else:
						temp1 = temp1 * (((1-pX[j]) * pXgY[x])/pY[key])
				elif(key == '2'):
					if(Xtest[i][j]== 1):
						temp2 = temp2 * ((pX[j] * pXgY[x])/pY[key])
					else:
						temp2 = temp2 * (((1-pX[j]) * pXgY[x])/pY[key])
			
		if (temp2 > temp1):
			plist.extend('2')
		else:
			plist.append('1')
	return plist
			
x = list(range(1,20))
Xtrain = []
Ytrain = []
x = [1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0]
y = list(range(1,3))
for i in range(1,100):
	Xtrain.append(random.sample(x,19))
	Ytrain.extend(random.sample(y,1))
Xtest =  [[1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1], [1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
predlist = NBClassify(Xtrain , Ytrain, Xtest)
print(predlist)		
				
