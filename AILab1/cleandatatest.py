file=open('UD_English-master/en-ud-test.conllu','r')
X=file.read()
file.close()
Z=X.strip().split('\n')
file=open('UD_English-master/test.txt','w')
y=0
for i in Z:
	
	R=i.strip().split('\t')
	if(len(R)):
		if((R[0][:1]!="#")):
			if(R[0]==""):
				file.write('\n')
			else:
				y+=1
				A=R[1].lower()
				B=R[2].lower()
				file.write(A+'\t'+R[3]+'\n')
				
print(y)
file.close()