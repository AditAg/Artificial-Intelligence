from sklearn.metrics import classification_report,confusion_matrix
act=[]
pred=[]
file1=open('UD_English-master/outputlabels.txt','r')
predicted=file1.read()
file1.close()
file2=open('UD_English-master/testlabels.txt','r')
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

confusion_matrix(act,pred)
conf=list(confusion_matrix)
for i in conf:
	i=list(i)
print (conf)

