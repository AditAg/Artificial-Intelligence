import re
from math import *
import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd

traindata=[]
trainlabels=[]
coeffmulti={}
testdata=[]
l_rate=0.01
iters=20000
colors=['r','b','g','c','m','y','k','w']
classvals=[]
delimiters=",",";","\t"
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
		traindata.append(Y[:-1])
		if(Y[-1]=="tested_positive"):
			trainlabels.append(1)
		elif(Y[-1]=="tested_negative"):
			trainlabels.append(0)
		else:	
			trainlabels.append(Y[-1])
	for i in range(len(traindata)):
		if(traindata[i][0]=='M'):
			traindata[i][0]=1
		elif(traindata[i][0]=='F'):
			traindata[i][0]=2
		elif(traindata[i][0]=='I'):
			traindata[i][0]=3;
		else:
			continue

def str_to_float(data):
	for row in data:
		for i in range(len(row)):
			try:
				row[i]=float(row[i].strip())
			except:
				continue
	for i in range(len(trainlabels)):
		trainlabels[i]=float(trainlabels[i])
		
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
			if(minmax[i][1]==0):
				continue
			else:
				row[i]=(row[i]-minmax[i][0])/(minmax[i][1])
def sigmoid_function(x):
	return (1.0)/(1.0+exp(-x))

def cost_function(coeff,labels):
	sums=0.0
	for i in range(len(traindata)):
		#ind=traindata.index(i)
		y=(float)(labels[i])
		sums+=((y*1.0*log(predict(i,traindata,coeff)))+((1-y)*1.0*log((1-predict(i,traindata,coeff)))))
	sums=(-1.0*sums)/(len(traindata))
	return sums
		
def predict(index,data,coeff):
	predictedvalue=coeff[0]
	for i in range(1,len(coeff)):
		predictedvalue+=coeff[i]*data[index][i-1]
	return sigmoid_function(predictedvalue)	

def coefficients_sgd(l_rate,no_iterations,coeff,classval):
	for x in range(len(traindata[0])+1):
		coeff.append(0.0)
	trainlabelsnew=trainlabels[:]
	for i in range(len(trainlabelsnew)):
		if(trainlabelsnew[i]==classval):
			trainlabelsnew[i]=1
		else:
			trainlabelsnew[i]=0
	print str(classval)+":"
	prevcostfunction=cost_function(coeff,trainlabelsnew)
	for x in range(no_iterations):
		print "Iteration ",x+1," : ",prevcostfunction
		m=len(traindata)
		for row in range(len(traindata)):
			ypred=predict(row,traindata,coeff)
			error=ypred-(float)(trainlabelsnew[row])
			coeff[0]=coeff[0]-((1.0/m)*l_rate*error)
			for i in range(1,len(coeff)):
				coeff[i]=coeff[i]-((1.0/m)*(l_rate*error*traindata[row][i-1]))
		newcostfunction=cost_function(coeff,trainlabelsnew)
		if((prevcostfunction-newcostfunction)<0.001):
			break
		prevcostfunction=newcostfunction
	return coeff

def coefficients_gd(l_rate,no_iterations,coeff,classval):
	for x in range(len(traindata[0])+1):
		coeff.append(0.0)
	trainlabelsnew=trainlabels[:]
	for i in range(len(trainlabelsnew)):
		if(trainlabelsnew[i]==classval):
			trainlabelsnew[i]=1
		else:
			trainlabelsnew[i]=0
	prevcostfunction=cost_function(coeff,trainlabelsnew)
	for x in range(no_iterations):
		#print "Iteration ",x+1," : ",prevcostfunction
		sum_error=[0.0 for i in range(len(coeff))]
		m=len(traindata)
		for row in range(len(traindata)):
			ypred=predict(row,traindata,coeff)
			error=ypred-(float)(trainlabelsnew[row])
			sum_error[0]+=l_rate*error
			for i in range(1,len(sum_error)):
				sum_error[i]+=(l_rate*error*traindata[row][i-1])
		for i in range(len(coeff)):
			coeff[i]=coeff[i]-((1.0/m)*sum_error[i])
		newcostfunction=cost_function(coeff,trainlabelsnew)
		if((prevcostfunction-newcostfunction)<0.0000001):
			break
		prevcostfunction=newcostfunction
	return coeff
	
def test(file_name):
	file1=open(file_name,'r')
	X=file1.read()
	file1.close()
	X=X.strip().split('\n')
	for i in X:
		if(i[0]=='%' or i[0]=='\n' or i[0]=='@'):
			continue
		Y=re.split(regexPattern,i)
		testdata.append(Y[:-1])
	for i in range(len(testdata)):
		if(testdata[i][0]=='M'):
			testdata[i][0]=1
		elif(testdata[i][0]=='F'):
			testdata[i][0]=2
		else:
			testdata[i][0]=3
	str_to_float(testdata)
	featurescaling(testdata)
	predictions=[]
	for row in range(len(testdata)):
		maximum=0.0
		classval=coeffmulti.keys()[0]
		for x in coeffmulti.keys():
			y=predict(row,testdata,coeffmulti[x])
			if y>=maximum:
				maximum=y
				classval=x
		predictions.append(classval)
	return predictions
		
plots=[]				
def logistic_regression():
	clean_data("diabetes.arff")
	nooffeatures=len(traindata[0])
	noofexamples=len(trainlabels)
	str_to_float(traindata)
	featurescaling(traindata)
	classes=[]
	for i in trainlabels:
		if(i in classes):
			continue
		else:
			classes.append(i)
	for i in range(len(classes)):
		if(classes[i] not in coeffmulti.keys()):
			coeffmulti[classes[i]]=[]
	for i in range(len(classes)):
		coeffmulti[classes[i]]=coefficients_sgd(l_rate,iters,coeffmulti[classes[i]],classes[i])
	print coeffmulti
	print("\n")
	predictions=test("diabetes.arff")
	correct=0
	for i in range(len(trainlabels)):
		print trainlabels[i],predictions[i]
		if(trainlabels[i]==predictions[i]):
			correct+=1
	print "Accuracy:",(correct*1.0)/(len(trainlabels))
	classvals=list(set(trainlabels))
	#minx1,minx2,maxx1,maxx2=traindata[0][0],traindata[0][1],traindata[0][0],traindata[0][1]
	#for i in range(len(traindata)):
	##	if(traindata[i][0]<minx1):
	#		minx1=traindata[i][0]
	#	if(traindata[i][1]<minx2):
	#		minx2=traindata[i][1]
	#	if(traindata[i][0]>maxx1):
	#		maxx1=traindata[i][0]
	#	if(traindata[i][1]>maxx2):
	#		maxx2=traindata[i][1]
	#for i in range(len(classvals)):
	#	x1=[]
	#	x2=[]
	#	for j in range(len(trainlabels)):
	#		if trainlabels[j]==classvals[i]:
	#			x1.append(traindata[j][0])
	#			x2.append(traindata[j][1])
	#	print len(x1),len(x2)
	#	plots.append(str("plot"+str(i+1)))
	#	plots[i]=pl.plot(x1,x2,str(colors[i]+'x'))
#
	#pl.title('LogisticRegression')
	#pl.xlabel('First Feature(X1)')
	#pl.ylabel('Second Feature(X2)')
	#pl.xlim(minx1,maxx1)
	#pl.ylim(minx2,maxx2)
	#pl.legend(plots,tuple(colors[:len(classvals)]),'best',numpoints=1)
	#pl.show()
	plt.figure(figsize=(30,30))
	df1=pd.DataFrame(traindata)
	df2=pd.DataFrame(traindata)
	df1['y']=trainlabels
	df2['y']=predictions
	z=1
	for i in range(df1.shape[1]-1):
		

		plt.subplot(df1.shape[1]-1,2,z)
		for j in range(len(classvals)):
			plt.scatter(df1[i][df1['y']==classvals[j]],df1['y'][df1['y']==classvals[j]],marker='x',color=colors[j],alpha=0.7,s=124,label=str(classvals[j]))
		plt.title('Logistic Regression'+'X'+str(i+1)+'vs y (Actual)')
		plt.xlabel('X'+str(i+1))
		plt.ylabel('Y')
		plt.legend(loc='upper right')
		plt.xlim([min(df1[i]),max(df1[i])])
		plt.ylim([min(df1['y'])-1.0,max(df1['y'])+1.0])
		z=z+1
		

		plt.subplot(df2.shape[1]-1,2,z)
		for j in range(len(classvals)):
			plt.scatter(df2[i][df2['y']==classvals[j]],df2['y'][df2['y']==classvals[j]],marker='x',color=colors[j],alpha=0.7,s=124,label=str(classvals[j]))
		plt.title('Logistic Regression'+'X'+str(i+1)+'vs y (Predicted)')
		plt.xlabel('X'+str(i+1))
		plt.ylabel('Y')
		plt.legend(loc='upper right')
		plt.xlim([min(df2[i]),max(df2[i])])
		plt.ylim([min(df2['y'])-1.0,max(df2['y'])+1.0])
		z=z+1
	plt.show()	

logistic_regression()		
