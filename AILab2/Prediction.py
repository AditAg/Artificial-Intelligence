import sys
import pandas as pd
f=open('testlabels.txt','r')
f2=open('output.txt','r')
L1=f.read().strip().split('\n')
correct=[]
output=[]
for i in L1:
	if len(i):
		correct.append((i.split('\t'))[0])
predct=f2.read().strip().split('\n')
for i in predct:
	if len(i):
		output.append((i.split('\t'))[1])

labels=set(correct)
labels=list(labels)
from sklearn.metrics import accuracy_score
print "Accuracy is: "+str(accuracy_score(correct, output))

from sklearn.metrics import confusion_matrix
ans1 = confusion_matrix(correct, output, labels=labels)
d=pd.DataFrame(columns=labels,index=labels)
d[:]=ans1[:]
print d
from sklearn.metrics import classification_report

print classification_report(correct, output, target_names=labels)

f.close()
f2.close()
