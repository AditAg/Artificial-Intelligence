import math

file1=open('train.txt','r')
X=file1.read()
file1.close()
X=X.strip().split('\n')

tags=[]
transitionprobs={}
emissionprobs={}
priorprobs={}
y=0
for i in X:
	Y=i.strip().split('\t')
	if (len(Y)==1):
		y+=1
		continue
	else:
		if(Y[1] not in tags):
			tags.append(Y[1])

for i in range(len(X)):
	Y=X[i].strip().split('\t')
	if(len(Y[0].strip())==0 or len(Y)==1):
		continue
	if(i==0 or len(X[i-1].strip())==0):
		if(Y[1] not in priorprobs.keys()):
			priorprobs[Y[1]]=1
		else:
			priorprobs[Y[1]]+=1
		if(Y[1] not in emissionprobs.keys()):
			emissionprobs[Y[1]]={}
			emissionprobs[Y[1]][Y[0]]=1
		else:
			if(Y[0] not in emissionprobs[Y[1]].keys()):
				emissionprobs[Y[1]][Y[0]]=1
			else:
				emissionprobs[Y[1]][Y[0]]+=1
	else:
		Y2=X[i-1].strip().split('\t')
		if(len(Y2)==1):
			continue
		if(Y2[1] not in transitionprobs.keys()):
			transitionprobs[Y2[1]]={}
			transitionprobs[Y2[1]][Y[1]]=1
		else:
			if(Y[1] not in transitionprobs[Y2[1]].keys()):
				transitionprobs[Y2[1]][Y[1]]=1

			else:
				transitionprobs[Y2[1]][Y[1]]+=1
		
		if(Y[1] not in emissionprobs.keys()):
			emissionprobs[Y[1]]={}
			emissionprobs[Y[1]][Y[0]]=1
		else:
			if(Y[0] not in emissionprobs[Y[1]].keys()):
				emissionprobs[Y[1]][Y[0]]=1
			else:
				emissionprobs[Y[1]][Y[0]]+=1

z=sum(priorprobs.values())
assert ((z-1)==y)
for i in priorprobs.keys():
	priorprobs[i]=(priorprobs[i])/(1.0*z)


for i in transitionprobs.keys():
	z=sum(transitionprobs[i].values())
	for j in transitionprobs[i].keys():
		transitionprobs[i][j]=(transitionprobs[i][j])/(1.0*z)

for i in emissionprobs.keys():
	z=sum(emissionprobs[i].values())
	for j in emissionprobs[i].keys():
		emissionprobs[i][j]=(emissionprobs[i][j])/(1.0*z)

for i in transitionprobs.keys():
	for j in tags:
		if(j not in transitionprobs[i].keys()):
			transitionprobs[i][j]=0.0

#print emissionprobs[tags[0]]
#print emissionprobs[tags[1]]
#print transitionprobs[tags[0]]
#print transitionprobs[tags[1]]
#print tags
#print tags[0]+":", transitionprobs[tags[0]]
#print (sum(transitionprobs[tags[0]].values()))

#Viterbi Algorithm

file1=open('testexample.txt','r')
X=file1.read()
file1.close()
Z=X.strip().split('\n\n')
file2=open('output.txt','w')
for r in Z:
	test=[]
	Y=r.strip().split('\n')
	for i in Y:
		if(len(i.strip())==0):
			continue
		test.append(i)
	#print test[0]
	#print emissionprobs['X'][test[0]]
	#print emissionprobs['PROPN'][test[0]]
	bestpaths={}
	for i in tags:
		bestpaths[i]=[]
		bestpaths[i].append(i)
		if(test[0] in emissionprobs[i].keys() and priorprobs[i]!=0.0):
			bestpaths[i].append((-1.0)*((math.log(priorprobs[i]))+(math.log(emissionprobs[i][test[0]]))))
		else:
			bestpaths[i].append(10000.0)	
	#print bestpaths
	l={}
	for i in range(1,len(test)):
		for j in tags:
			maxprob=10000.0
			tag=j
			for k in bestpaths.keys():
				if(transitionprobs[k][j]!=0.0 and (test[i] in emissionprobs[j].keys())):
					prob=bestpaths[k][-1]+(-1.0)*math.log(transitionprobs[k][j])
					prob=prob+(-1.0)*math.log(emissionprobs[j][test[i]])
				else:
					prob=bestpaths[k][-1]+10000.0
				if(prob<maxprob):
					maxprob=prob
					tag=k
			#print j,"  :  ",tag,maxprob
			#del(bestpaths[j][-1])
			l[j]=[]
			l[j].append(tag)
			if(maxprob==10000.0):
				l[j].append(10000.0)
			else:
				l[j].append(maxprob)
		for j in tags:
			del(bestpaths[j][-1])
			bestpaths[j].append(l[j][0])
			bestpaths[j].append(l[j][1])
	
	#print bestpaths
	minimum=10000
	tag=bestpaths.keys()[0]
	for i in bestpaths.keys():
		if(bestpaths[i][-1]<minimum):
			minimum=bestpaths[i][-1]
			tag=i
	
	length=len(bestpaths[tag])-2
	output=[]
	while(length>=0):
		output.append(bestpaths[tag][0])
		tag=bestpaths[tag][length]
		length-=1
	
	for i in range(len(test)):
		print test[i],"\t",output[len(test)-1-i]
		file2.write(test[i]+'\t'+output[len(test)-1-i]+'\n')
	print "\n"
	file2.write('\n')
file2.close()							
				
	
