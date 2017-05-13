file1=open('test.txt','r')
file2=open('test2.txt','w')
file3=open('testdatahunpos.txt','w')
file4=open('testlabels.txt','w')
file5=open('testdatacrf.txt','w')
X=file1.read()
file1.close()
Y=X.strip().split('\n')
for i in Y:
	R=i.strip().split(" ")
	if(len(R)!=1):
		file2.write(R[0]+"\t"+R[1]+"\t"+R[2]+"\n")
		file3.write(R[0]+"\n")
		file4.write(R[2]+"\n")
		file5.write(R[0]+'\t'+R[1]+'\n')
	else:
		file2.write(R[0]+"\n")
		file3.write(R[0]+"\n")
		file4.write(R[0]+"\n")
		file5.write(R[0]+"\n")

file2.close()
file3.close()
file4.close()
file5.close()


