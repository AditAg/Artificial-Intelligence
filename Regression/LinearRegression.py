import re
from math import sqrt
traindata=[]
trainlabels=[]
coeff=[]
testdata=[]
l_rate=0.000001
iters=30000
delimiters=",",";","\t"," "
regexPattern='|'.join(map(re.escape,delimiters))
def clean_data(file_name):
	file1=open(file_name,'r')
	X=file1.read()
	file1.close()
	X=X.strip().split('\n')
	for i in X:
		if(len(i)==0):
			continue 
		if(i[0]=='%' or i[0]=='\n' or i[0]=='@'):
			continue
		Y=re.split(regexPattern,i)
		Y=list(Y)
		Z=[]
		for j in range(len(Y)):
			if(Y[j]==''):
				continue
			else:
				Z.append(Y[j])
		Y=Z
		if(file_name=="data1.txt"):		
			traindata.append(list(Y[1:-1]))
		else:
			traindata.append(list(Y[:-1]))		
		trainlabels.append(Y[-1])
	for i in range(len(traindata)):
		if(traindata[i][0]=='M'):
			traindata[i][0]=1
		elif(traindata[i][0]=='F'):
			traindata[i][0]=2
		elif(traindata[i][0]=='I'):
			traindata[i][0]=3
		else:
			continue

def str_to_float():
	for row in traindata:
		for i in range(len(row)):
			try:
				row[i]=float(row[i].strip())
			except:
				continue
	for i in range(len(trainlabels)):
		trainlabels[i]=float(trainlabels[i].strip())
		
def featurescaling(data):
	minmax=[]
	for i in range(len(data[0])):
		col_values=[row[i] for row in data]
		mean=(sum(col_values)*1.0)/len(col_values)
		standev=0.0
		for x in col_values:
			standev+=((x-mean)*(x-mean))
		standev=(standev)/(len(col_values))
		standev=sqrt(standev)
		minmax.append([mean,standev])
	for row in data:
		for i in range(len(row)):
			row[i]=(row[i]-minmax[i][0])/(minmax[i][1])
def cost_function():
	sums=0.0
	for i in range(len(traindata)):
		#ind=traindata.index(i)
		error=(predict(i,traindata))-(float)(trainlabels[i])
		sums+=(error*error)
	sums=(sums)/(2*len(traindata))
	return sums
		
def predict(index,data):
	predictedvalue=coeff[0]
	for i in range(1,len(coeff)):
		predictedvalue+=coeff[i]*data[index][i-1]
	return predictedvalue	

def coefficients_sgd(l_rate,no_iterations):
	for x in range(len(traindata[0])+1):
		coeff.append(0.0)
	prevcostfunction=cost_function()
	for x in range(no_iterations):
		print "Iteration ",x+1," : ",prevcostfunction
		m=len(traindata)
		for row in range(len(traindata)):
			ypred=predict(row,traindata)
			error=ypred-(float)(trainlabels[row])
			coeff[0]=coeff[0]-((1.0/m)*l_rate*error)
			for i in range(1,len(coeff)):
				coeff[i]=coeff[i]-((1.0/m)*(l_rate*error*traindata[row][i-1]))
		newcostfunction=cost_function()
		if((prevcostfunction-newcostfunction)<0.000001):
			break
		prevcostfunction=newcostfunction

def coefficients_gd(l_rate,no_iterations):
	for x in range(len(traindata[0])+1):
		coeff.append(0.0)
	prevcostfunction=cost_function()
	for x in range(no_iterations):
		print "Iteration ",x+1," : ",prevcostfunction
		sum_error=[0.0 for i in range(len(coeff))]
		m=len(traindata)
		for row in range(len(traindata)):
			ypred=predict(row,traindata)
			error=ypred-(float)(trainlabels[row])
			sum_error[0]+=l_rate*error
			for i in range(1,len(sum_error)):
				sum_error[i]+=(l_rate*error*traindata[row][i-1])
		for i in range(len(coeff)):
			coeff[i]=coeff[i]-(1.0/m)*sum_error[i]
		newcostfunction=cost_function()
		if((prevcostfunction-newcostfunction)<0.0001):
			break
		prevcostfunction=newcostfunction
	
def print_line():
	for i in range(len(coeff)):
		if(i==0):
			print (str(coeff[0])),
		else:
			if(coeff[i]>=0):
				print "+"+str(coeff[i])+"* X"+str(i),
			else:
				print "-"+str(abs(coeff[i]))+"* X"+str(i),
	
def test(file_name):
	file1=open(file_name,'r')
	X=file1.read()
	file1.close()
	X=X.strip().split('\n')
	for i in X:
		if(i[0]=='%' or i[0]=='\n' or i[0]=='@'):
			continue
		Y=re.split(regexPattern,i)
		testdata.append(Y[:])
	for i in range(len(testdata)):
		if(testdata[i][0]=='M'):
			testdata[i][0]=1
		elif(testdata[i][0]=='F'):
			testdata[i][0]=2
		else:
			testdata[i][0]=3
	featurescaling(testdata)
	predictions=[]
	for row in range(len(testdata)):
		y=predict(row,testdata)
		predictions.append(y)
	return predictions
		
				
def linear_regression():
	clean_data("quake.arff")
	nooffeatures=len(traindata[0])
	noofexamples=len(trainlabels)
	str_to_float()
	print traindata
	print trainlabels 
	#featurescaling(traindata)
	coefficients_sgd(l_rate,iters)
	print_line()
	print("\n")
	testdata=traindata
	for row in range(len(testdata)):
		y=predict(row,testdata)
		print trainlabels[row],y
	
	#predictions=test("testdata.txt")
	#print predictions

linear_regression()		
