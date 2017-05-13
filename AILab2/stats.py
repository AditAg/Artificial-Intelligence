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
'''R=int(input())
for i in range(R):
	print(correct[i])
input()'''
fn={}
tp={}
fp={}
set_={}
Rav=0
Rc=0
Fav=0
Fc=0
for i in range(len(correct)):
	if correct[i] not in set_.keys():
		set_[correct[i]]=1
	if output[i] not in set_.keys():
		set_[output[i]]=1
	if correct[i]==output[i]:
		if correct[i] in tp.keys():
			tp[correct[i]]=tp[correct[i]]+1
		else:
			tp[correct[i]]=1
	else:
		if correct[i] in fn.keys():
			fn[correct[i]]=fn[correct[i]]+1
		else:
			fn[correct[i]]=1
		if output[i] in fp.keys():
			fp[output[i]]=fp[output[i]]+1
		else:
			fp[output[i]]=1
'''for i in tp.keys():
	print(tp[i])
input()
for i in range(10):
	print(correct[i]+","+output[i])
input();'''
print("Tag Wise Precision Recall and F-measure")
for j in set_.keys():
	print("Tag : ",j)
	TP,FN,FP=0,0,0
	if j in tp.keys():
		TP=tp[j]
	if j in fp.keys():
		FP=fp[j]
	if j in fn.keys():
		FN=fn[j]
	P=0
	F=0
	R=0
	try:
		P=(TP*1.0)/(TP+FP)
		print("Precision : ",P)
	except:
		print("Precision : Not defined")
	try:
		R=(TP*1.0)/(TP+FN)
		Rav+=R
		Rc+=1
		print("Recall : ",R)
	except:
		print("Recall : Not defined")
	try:
		F=(2*P*R)/(P+R)
		Fav+=F
		Fc+=1
		print("F-measure : ",F)
	except:
		print("F-measure : Not defined")
dict_fn=0
dict_tp=0
dict_fp=0
for i in range(len(correct)):
	if correct[i]==output[i]:
		dict_tp=dict_tp+1
	else:
		dict_fp=dict_fp+1
		dict_fn=dict_fn+1
Precision=dict_tp/(dict_tp+dict_fp*1.0);
Recall=dict_tp/(dict_tp+dict_fn*1.0);
F=2.0*Precision*Recall/(Precision+Recall);		
print ("Overvall Precision : " ,Precision)
print ("Overvall Recall : ", Recall)
print ("Overvall F-measure", F)
print ("Average Recall : ", Rav/Rc)
print ("Average F-measure: ",Fav/Fc)
