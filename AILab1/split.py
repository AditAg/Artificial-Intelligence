file=open('UD_English-master/en-ud-train.conllu','r')
X=file.read()
file.close()
#file=open('UD_English-master/en-ud-test.conllu','r')
#X2=file.read()
#file.close()
#file=open('UD_English-master/en-ud-dev.conllu','r')
#X3=file.read()
#file.close()
file2=open('UD_English-master/trainsplit.txt','w')
file3=open('UD_English-master/testsplit.txt','w')
Z=X.strip().split('\n')
#Z2=X2.strip().split('\n')
#Z3=X3.strip().split('\n')
y=0
#for i in Z2:
#	Z.append(i)
#for i in Z3:
#	Z.append(i)
for i in Z:
	if(len(i)):
		if(i[0]=="#"):	
			y+=1


train=(80*y)/100
test=y-train
y=0
for i in Z:
	R=i.strip().split('\t')
	if(len(R)):
		if((R[0][:1]!="#")):
			if(R[0]==""):
				if(y<train):
					file2.write("\n")
				else:
					file3.write("\n")
			else:
				A=R[1].lower()
				if(y<train):
					
					file2.write(A+'\t'+R[3]+'\n')
				else:
					
					file3.write(A+'\t'+R[3]+'\n')
		else:
			#if(y<train):
			#	print("Hello",y)
			#else:
			#	print("ABC",y)
			y+=1
	

file2.close()
file3.close()
