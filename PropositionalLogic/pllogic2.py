import math
precedence={'~':5,'&':4,'|':3,'>':2,'=':1,'^':0,'(':-1}
prop_constants=[]
truth_values=[]
infix_expressions=[]
tautologies=[]
self_contradictions=[]
contingencies=[]
equivalent=[]
logical_entailment=[]
class myStack:
	def __init__(self):
		self.stack=[]
	def isEmpty(self):
		return self.size()==0
	def push(self,item):
		self.stack.append(item)
	def pop(self):
		if self.isEmpty():
			return NULL
		else:
			return self.stack.pop()
	def size(self):
		return len(self.stack)
	def top(self):
		z=self.pop()
		self.push(z)
		return z

def properInfix(infixchars):
	for i in range(len(infixchars)):
		if ((i<(len(infixchars)-1)) and (infixchars[i]=='o' or infixchars[i]=='O') and (infixchars[i+1]=='r' or infixchars[i+1]=='R')):
			infixchars[i]='|'
			infixchars.pop(i+1)
		elif ((i<(len(infixchars)-2)) and (infixchars[i]=='a' or infixchars[i]=='A') and (infixchars[i+1]=='n' or infixchars[i+1]=='N') and (infixchars[i+2]=='d' or infixchars[i+2]=='D')):
			infixchars[i]='&'
			infixchars.pop(i+1)
			infixchars.pop(i+1)
		elif ((i<(len(infixchars)-4)) and (infixchars[i]=='e' or infixchars[i]=='E') and (infixchars[i+1]=='q' or infixchars[i+1]=='Q') and (infixchars[i+2]=='u' or infixchars[i+2]=='U') and (infixchars[i+3]=='i' or infixchars[i+3]=='I') and (infixchars[i+4]=='v' or infixchars[i+4]=='V')):
			infixchars[i]='='
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
		elif ((i<(len(infixchars)-2)) and (infixchars[i]=='n' or infixchars[i]=='N') and (infixchars[i+1]=='o' or infixchars[i+1]=='O') and (infixchars[i+2]=='t' or infixchars[i+2]=='T')):
			infixchars[i]='~'
			infixchars.pop(i+1)
			infixchars.pop(i+1)
		elif ((i<(len(infixchars)-6)) and (infixchars[i]=='i' or infixchars[i]=='I') and (infixchars[i+1]=='m' or infixchars[i+1]=='M') and (infixchars[i+2]=='p' or infixchars[i+2]=='P') and (infixchars[i +3]=='l' or infixchars[i+3]=='L') and (infixchars[i+4]=='i' or infixchars[i+4]=='I') and (infixchars[i+5]=='e' or infixchars[i+5]=='E') and (infixchars[i+6]=='s' or infixchars[i+6]=='S')):
			infixchars[i]='>'
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
		elif ((i<(len(infixchars)-3)) and (infixchars[i]=='n' or infixchars[i]=='N') and (infixchars[i+1]=='a' or infixchars[i+1]=='A') and (infixchars[i+2]=='n' or infixchars[i+2]=='N') and (infixchars[i+3]=='d' or infixchars[i+3]=='D')):
			infixchars[i]='^'
			infixchars.pop(i+1)
			infixchars.pop(i+1)
			infixchars.pop(i+1)
		else:
			continue
	z=[]
	z.append('(')
	for i in range(len(infixchars)):
		if(infixchars[i]==' '):
			continue
		else:
			z.append(infixchars[i])
	z.append(')')
	return z

def ischaracter(x):
	if(((ord(x)>=65) and (ord(x)<=90)) or ((ord(x)>=97) and (ord(x)<=122))):
		return True
	else:
		return False
def isoperator(x):
	if(x in precedence.keys() and x!='(' and x!='~'):
		return True
	else:
		return False
def validateinfix(infixchars):
	noofconsts=0
	openingbraces,closingbraces=0,0
	for j in range(len(infixchars)):
		if(closingbraces > openingbraces):
			return False
		if((j<len(infixchars)-1) and ischaracter(infixchars[j]) and (ischaracter(infixchars[j+1]) or infixchars[j+1]=='(' or infixchars[j+1]=='~')):
			return False
		if((infixchars[j] not in precedence.keys()) and (not ischaracter(infixchars[j])) and (infixchars[j]!=')')):
			return False
		if((j<len(infixchars)-1) and isoperator(infixchars[j]) and (isoperator(infixchars[j+1]) or infixchars[j+1]==')')):
			return False
		if((j<len(infixchars)-1) and infixchars[j]==')' and (infixchars[j+1]=='(' or ischaracter(infixchars[j+1]) or infixchars[j+1]=='~')):
			return False
		if((j<len(infixchars)-1) and infixchars[j]=='(' and isoperator(infixchars[j+1])):
			return False
		if((j<len(infixchars)-1) and infixchars[j]=='~' and (not ischaracter(infixchars[j+1])) and (infixchars[j+1]!='(')):
			return False
		if(infixchars[j]=='('):
			openingbraces+=1
		elif(infixchars[j]==')'):
			closingbraces+=1
		
	if(openingbraces!=closingbraces):
		return False
	return True
		

def inftopost(infixchars):
	output=[]
	propconstants=set()
	opstack=myStack()
	for i in range(len(infixchars)):
		if(infixchars[i]==' '):
			continue
		if((ord(infixchars[i])>=65) and (ord(infixchars[i])<=90)):
			propconstants.add(infixchars[i])
			output.append(infixchars[i])	
		elif ((ord(infixchars[i])>=97) and (ord(infixchars[i])<=122)):
			propconstants.add(infixchars[i])	
			output.append(infixchars[i])
		elif (infixchars[i]=='('):
			opstack.push(infixchars[i])
		elif (infixchars[i]==')'):
			topelement=opstack.pop()
			while(topelement!='('):
				output.append(topelement)
				topelement=opstack.pop()
		else:
			while((not opstack.isEmpty()) and (precedence[infixchars[i]]<precedence[opstack.top()])):
				topelement=opstack.pop()
				output.append(topelement)
			opstack.push(infixchars[i])
	while (not opstack.isEmpty()):
		output.append(opstack.pop())
	return output,propconstants

def make_truth_assignments(propconsts,truth_assignments):
	n=2**(len(propconsts))
	ta=[1 for j in range(len(propconsts))]
	for i in range(n):
		truth_assignments.append({})
		j=1
		while(j<n):
			if(i%j==0):
				ta[int(math.log(j,2))]=(ta[int(math.log(j,2))]+1)%2
			j=j*2
		for j in range(len(propconsts)):
			truth_assignments[i][propconsts[j]]=ta[j]
	return truth_assignments				

def evalute(a,b,operator):
	if (operator=='&'):
		if ((a==1) and (b==1)):
			return 1
		else:
			return 0
	elif(operator=='|'):
		if ((a==0) and (b==0)):
			return 0
		else:
			return 1
	elif (operator=='>'):
		if ((a==1) and (b==0)):
			return 0
		else:
			return 1
	elif(operator=='='):
		if (((a==1) and (b==0)) or ((a==0) and (b==1))):
			return 0
		else:
			return 1
	elif(operator=='^'):
		if ((a==1) and (b==1)):
			return 0
		else:
			return 1

def negate(a):
	if(a==1):
		return 0
	else:
		return 1
	

def evaluatepost(output,truth_assignment):
	evaluatestack=myStack()
	for i in range(len(output)):
		if (ischaracter(output[i])):
			evaluatestack.push(truth_assignment[output[i]])
		elif (isoperator(output[i])):
			secondelem=evaluatestack.pop()
			firstelem=evaluatestack.pop()
			result=evalute(firstelem,secondelem,output[i])
			evaluatestack.push(result)
		elif(output[i]=='~'):
			firstelem=evaluatestack.pop()
			result=negate(firstelem)
			evaluatestack.push(result)
	if(evaluatestack.size()!=1):
		print "Sorry wrong postfix expression"
	else:
		return evaluatestack.pop()

no_statements=raw_input("Enter the no. of compound statements you wish to enter\n")
for r in range(int(no_statements)):
	print ("-------------------The controls for propositional logic are---------------------")
	print ("1)'equiv'or'=' to specify equivalence")
	print ("2)'or' or '|' to specify or")
	print ("3)'and' or '&' to specify and")
	print ("4)'implies' or '>' to specify an implication")
	print("5)'not' or '~' to specify negation")
	print("6)'nand' or '^' to specify nand")
	infix=raw_input("Please enter the infix expression(with or without parantheses)(use characters 	for denoting propositional constants)\n")
	infixchars=list(infix)
	truth_assignments=[]
	output=[]
	propconstants=set()
	
	infixchars=properInfix(infixchars)
	if(validateinfix(infixchars)):
		infix_expressions.append(infixchars)
		output,propconstants=inftopost(infixchars)
		print output
		propconstants=list(propconstants)
		prop_constants.append(propconstants)		
	else:	
		print "sorry the given expression is not a proper infix expression... try again"

consts=[]
for i in range(len(prop_constants)):
	for j in prop_constants[i]:
		if (j not in consts):
			consts.append(j)
truth_assignments=[]
truth_assignments=make_truth_assignments(consts,truth_assignments)
output=[]
propconstants=set()
for r in range(len(infix_expressions)):
	output,propconstants=inftopost(infix_expressions[r])
	table=[]
	table.append([])
	for i in consts:
		table[0].append(i)
	table[0].append(str(''.join(infix_expressions[r])))
	for i in range(len(truth_assignments)):
		table.append([])
		value_expr=evaluatepost(output,truth_assignments[i])
		for j in consts:
			table[i+1].append(truth_assignments[i][j])
		table[i+1].append(value_expr)
	truth_values.append(table)
def tautology(truth_values):
	for i in range(len(truth_values)):
		true=0
		for j in range(len(truth_values[i])):
			if(truth_values[i][j][-1]==1):
				true+=1
		if(true==len(truth_values[i])-1):
			tautologies.append(infix_expressions[i])

def contradiction(truth_values):
	for i in range(len(truth_values)):
		false=0
		for j in range(len(truth_values[i])):
			if(truth_values[i][j][-1]==0):
				false+=1
		if(false==len(truth_values[i])-1):
			self_contradictions.append(infix_expressions[i])
def contingency(truth_values):
	for i in range(len(truth_values)):
		false,true=0,0
		for j in range(len(truth_values[i])):
			if(truth_values[i][j][-1]==0):
				false+=1
			elif(truth_values[i][j][-1]==1):
				true+=1
		if(true>0 and false >0):
			contingencies.append(infix_expressions[i])

def equivalence(truth_values):
	for i in range(len(truth_values)):
		for j in range(i+1,len(truth_values)):
			if(len(truth_values[j])!=len(truth_values[i])):
				continue
			if(len(truth_values[j][0])!=len(truth_values[i][0])):
				continue
			notpresent=0
			for k in range(len(truth_values[i][0])-1):
				if (truth_values[i][0][k] not in truth_values[j][0]):
					notpresent+=1
			if(notpresent>0):
				continue
			equal=0
			for k in range(1,len(truth_values[i])):
				if(truth_values[j][k][-1]!=truth_values[i][k][-1]):
					equal=1
					break
			if(equal==0):
				equivalent.append([infix_expressions[i],infix_expressions[j]])

def entailment(truth_values):
	for i in range(len(truth_values)):
		for j in range(len(truth_values)):
			if(i==j):
				continue
			if(len(truth_values[j])!=len(truth_values[i])):
				continue
			if(len(truth_values[j][0])!=len(truth_values[i][0])):
				continue
			notpresent=0
			for k in range(len(truth_values[i][0])-1):
				if (truth_values[i][0][k] not in truth_values[j][0]):
					notpresent+=1
			if(notpresent>0):
				continue
			implies=0
			for k in range(1,len(truth_values[i])):
				if(truth_values[j][k][-1]==1 and truth_values[i][k][-1]==0):
					implies=1
					break
			if(implies==0):
				logical_entailment.append([infix_expressions[j],infix_expressions[i]])

def consistent(truth_values):
	if(len(self_contradictions)!=0):
		print "The given set of premises are not consistent"
		return
	a=0
	for i in range(len(truth_values)):
		if(infix_expressions[i] in tautologies):
			continue
		else:
			for j in range(i+1,len(truth_values)):
				if(infix_expressions[j] in tautologies):
					continue
				if(len(truth_values[j])!=len(truth_values[i])):
					a=1
					break
				if(len(truth_values[j][0])!=len(truth_values[i][0])):
					a=1
					break
				notpresent=0
				for k in range(len(truth_values[i][0])-1):
					if ((truth_values[i][0][k] not in truth_values[j][0]) or (truth_values[j][0][k] not in truth_values[i][0])):
						notpresent+=1
				if(notpresent>0):
					a=1
					break
				same_true=0
				for k in range(1,len(truth_values[i])):
					if(truth_values[i][k][-1]==1 and truth_values[j][k][-1]==1):
						same_true=1
						break
				if(same_true==0):
					a=1
					break
			if(a==1):
				break
	if(a==1):	
		print "The given set of premises is not consistent"
	if(a==0):
		print "The given set of premises is consistent"
	return
				
						
print "The truth tables for the valid expressions are:\n"
for i in range(len(truth_values)):
	for j in range(len(truth_values[i])):
		for k in range(len(truth_values[i][j])):
			if(k==len(truth_values[i][j])-1):
				print truth_values[i][j][k]
			else:
				print truth_values[i][j][k],
	print "\n"

tautology(truth_values)
print "The tautologies are:"
if(len(tautologies)==0):
	print "None"
for i in tautologies:
	print ''.join(i)

contradiction(truth_values)
print "The self-contradictions are:"
if(len(self_contradictions)==0):
	print "None"
for i in self_contradictions:
	print ''.join(i)

contingency(truth_values)
print "The contingencies are:"
if(len(contingencies)==0):
	print "None"
for i in contingencies:
	print ''.join(i)

equivalence(truth_values)
print "Consider tautologies and contradictions to be equiv. to each other respectively"
print "The equivalences are(other than the case of a C.S. being equivalent to itself):"
if(len(equivalent)==0 and len(tautologies)<=1 and len(self_contradictions)<=1):
	print "None"
for i in equivalent:
	print ''.join(i[0])+"and"+''.join(i[1])
for i in range(len(tautologies)):
	for j in range(i+1,len(tautologies)):
		if(([tautologies[i],tautologies[j]] not in equivalent) and ([tautologies[j],tautologies[i]] not in equivalent)):
			print ''.join(tautologies[i])+"and"+''.join(tautologies[j])
for i in range(len(self_contradictions)):
	for j in range(i+1,len(self_contradictions)):
		if(([self_contradictions[i],self_contradictions[j]] not in equivalent) and ([self_contradictions[j],self_contradictions[i]] not in equivalent)):
			print ''.join(self_contradictions[i])+"and"+''.join(self_contradictions[j])

entailment(truth_values)
print "Consider tautologies and contradictions to entail each other respectively"
print "The logical entailments are(except case of a C.S. logically entailing itself):"
if(len(logical_entailment)==0 and len(tautologies)<=1 and len(self_contradictions)<=1):
	print "None"
for i in logical_entailment:
	print ''.join(i[0])+" |= "+''.join(i[1])
for i in range(len(tautologies)):
	for j in range(len(infix_expressions)):
		if(tautologies[i]==infix_expressions[j]):
			continue
		if(([infix_expressions[j],tautologies[i]] not in logical_entailment)):
			print ''.join(infix_expressions[j])+" |= "+''.join(tautologies[i])
		
for i in range(len(self_contradictions)):
	for j in range(len(infix_expressions)):
		if(self_contradictions[i]==infix_expressions[j]):
			continue
		if([self_contradictions[i],infix_expressions[j]] not in logical_entailment):
			print ''.join(self_contradictions[i])+" |= "+''.join(infix_expressions[j])
		

consistent(truth_values)
