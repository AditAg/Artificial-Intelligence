file1=open('train.txt','r')
file2=open('train2.txt','w')
X=file1.read()
file1.close()
Y=X.strip().split('\n')
for i in Y:
	R=i.strip().split(" ")
	if(len(R)!=1):
		print R
		file2.write(R[0]+"\t"+R[1]+"\t"+R[2]+"\n")
	else:
		print R
		file2.write(R[0]+"\n")
file2.close()
file1=open('train2.txt','r')
X=file1.read()
file1.close()
file2=open('training.txt','w')
Y=X.strip().split('\n')
for i in Y:
	R=i.strip().split('\t')
	if(len(R)!=1):
		#if(R[2]=='O' or len(R[2])==1):
		#	file2.write(R[0]+'\t'+R[2]+'\n')
		#else:
		#	file2.write(R[0]+'\t'+R[2][2:]+'\n')
		file2.write(R[0]+'\t'+R[2]+'\n')
	else:
		file2.write(R[0]+"\n")
file2.close()
		


