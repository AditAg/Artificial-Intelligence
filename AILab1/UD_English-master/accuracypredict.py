#from sklearn.metrics import confusion_matrix,classification_report
file1=open('outputlabels.txt','r')
predicted=file1.read()
file1.close()
file2=open('testlabels.txt','r')
actual=file2.read()
file2.close()
predict=predicted.strip().split('\n')
actualvalue=actual.strip().split('\n')
pred=[]
act=[]
for i in predict:
	R=i.strip().split('\t')
	if(R[0]==""):
		continue
	pred.append(R[1])
	
for i in actualvalue:
	if(i==""):
		continue
	act.append(i)
	
labels=set(act)
labels=list(labels)
truepositives={}
truenegatives={}
falsepositives={}
falsenegatives={}
accuracy={}
precision={}
recall={}
specificity={}
for i in range(len(labels)):
	TP,TN,FP,FN=0.0,0.0,0.0,0.0
	for j in range(len(pred)):
		if((act[j]==labels[i]) and (pred[j]==labels[i])):
			TP+=1
		elif((act[j]==labels[i]) and (pred[j]!=labels[i])):
			FN+=1
		elif((act[j]!=labels[i]) and (pred[j]==labels[i])):
			FP+=1
		else:
			TN+=1
	truepositives[labels[i]]=TP
	truenegatives[labels[i]]=TN
	falsepositives[labels[i]]=FP
	falsenegatives[labels[i]]=FN
	accuracy[labels[i]]=(TP+TN)/(TP+TN+FP+FN)
	precision[labels[i]]=(TP)/(TP+FP)
	recall[labels[i]]=(TP)/(TP+FN)
	specificity[labels[i]]=(TN)/(TN+FP)
#print("Accuracy:")
#print(accuracy)
#print("Precision:")
#print(precision)
#print("Recall:")
#print(recall)
#print("Specificity:")
#print(specificity)
avgacc,microprecision,macroprecision,microrecall,macrorecall=0.0,0.0,0.0,0.0,0.0
microfscore,macrofscore=0.0,0.0
beta=1.0
t1,t2,t3=0.0,0.0,0.0
for i in range(len(labels)):
	avgacc+=accuracy[labels[i]]
	macroprecision+=precision[labels[i]]
	macrorecall+=recall[labels[i]]
	t1+=truepositives[labels[i]]
	t2+=(truepositives[labels[i]]+falsepositives[labels[i]])
	t3+=(truepositives[labels[i]]+falsenegatives[labels[i]])

avgacc=(avgacc)/(len(labels))
macroprecision=(macroprecision)/(len(labels))
macrorecall=(macrorecall)/(len(labels))
macrofscore=(((beta*beta)+1)*macroprecision*macrorecall)/(((beta*beta)*macroprecision)+macrorecall)
microprecision=(t1)/(t2)
microrecall=(t1)/(t3)
microfscore=(((beta*beta)+1)*microprecision*microrecall)/((beta*beta*microprecision)+microrecall)

print("Average accuracy:", avgacc)
print("Microprecision:" ,microprecision)
print("Microrecall:" ,microrecall)
print("Microfscore:" ,microfscore)
print("Macroprecision:",macroprecision)
print("Macrorecall:",macrorecall)
print("Macrofscore:",macrofscore)
	
	
	




