x = "AKJGTA"
y = "DKLJTA"

'''
AK-JGT
DKLJ-T
'''

INDEL_SCORE = -8
SUB_SCORE = -1
ID_SCORE = 20

Table = {}
A = {}
def S1(x,y,i,j):
	if (i,j) not in Table:
		if j == -1:
			Table[(i,j)] = INDEL_SCORE*(i+1)
			for k in range(i+1):
				A[i,j] = 'd'
		elif i == -1:
			Table[(i,j)] = INDEL_SCORE*(j+1)
			for k in range(j+1):
				A[i,j] = 'i'
		elif x[i] == y[j]:
			Table[(i,j)] = ID_SCORE + S1(x,y,i-1,j-1)
			A[i,j] = 'm'
		else:
			Table[(i,j)] = max(SUB_SCORE + S1(x,y,i-1,j-1), INDEL_SCORE + S1(x,y,i-1,j), INDEL_SCORE + S1(x,y,i,j-1))
			if Table[(i,j)] == SUB_SCORE + S1(x,y,i-1,j-1):
				A[i,j] = 's'
			elif Table[(i,j)] == INDEL_SCORE + S1(x,y,i-1,j):
				A[i,j] = 'd'
			else:
				A[i,j] = 'i'

	return Table[(i,j)]

F, S = '',''
def Trace(x,y,i,j):
	global F,S
	if (i,j) in A:
		if A[i,j] == 'm':
			print(x[i],"matches",y[j])
			F, S = x[i] + F, y[j] + S
			Trace(x,y,i-1,j-1)
		elif A[i,j] == 's':
			print(x[i],"substituted by",y[j])
			F, S = x[i] + F, y[j] + S
			Trace(x,y,i-1,j-1)
		elif A[i,j] == 'd':
			print(x[i],"is aligned to a gap")
			F, S = x[i] + F, '-' + S
			Trace(x,y,i-1,j)
		else:
			print(y[j],"is aligned to a gap")
			F, S = '-' + F, y[j] + S
			Trace(x,y,i,j-1)

i, j = len(x)-1, len(y)-1
print (S1(x,y,i,j))
Trace(x,y,i,j)
# print (A)

print(F)
print(S)
