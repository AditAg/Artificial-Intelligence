file=open('UD_English-master/dev.txt','r')
X=file.read()
file.close()
Z=X.strip().split('\n')
file=open('UD_English-master/devdata.txt','w')
y=0
for i in Z:
	R=i.strip().split('\t')

	if(len(R)):
		if(R[0]==""):
			file.write('\n')
		else:
	
			y+=1
			file.write(R[0]+'\n')
print(y)
file.close()
