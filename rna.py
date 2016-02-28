# x = 'ACCAGGU'
#    (((.)))
'''
(1) Find optimal structure for ACCAGGU
(2) Pair A and U, find optimal structure for CCAGG

(1) Find optimal structure for ACCAGGUC
(2) Skip C, find optimal structure for ACCAGGU

(1) Find optimal structure for CACCAGGU
(2) Skip C, find optimal structure for ACCAGGU


(1) Find optimal alignment for CAAT and HAT
(2) Align T, T then find optimal alignment for CAA and HA

(1) Find optimal alignment for CAATR and HAT
(2) Delete R then find optimal alignment for CAAT and HAT

'''

def complement(a,b):
	return (a,b) in [('A','U'),('U','A'),('C','G'),('G','C')]

# returns the max number of pairs in the optimal structure of x_i,...,x_j
#Table = {}
def Structure(x,S,i,j):
	if (i,j) not in Table:
		if j-i <= 1:
			return 0
		m,m1 = 0,0
		if complement(x[i],x[j]):
			m = 1 + Structure(x, S, i+1, j-1)
			m1 = m
			# if (x[i], x[j]) in [('A','U'),('U','A')]:
			# 	m = 2 + Structure(x, S, i+1, j-1)
			# else:
			# 	m = 3 + Structure(x, S, i+1, j-1)

		if m < Structure(x,S,i+1,j):
			m = Structure(x,S,i+1,j)

		if m < Structure(x,S,i,j-1):
			m = Structure(x,S,i,j-1)
		
		for k in range(i+1,j):
			if m < (Structure(x, S, i, k) + Structure(x, S, k+1,j)):
				m = Structure(x, S, i, k) + Structure(x, S, k+1,j)

		Table[(i,j)] = m
		if m1 == m and complement(x[i],x[j]):
			S[i], S[j] = '(', ')'
	return Table[(i,j)]

rnas = ['ACCAGGU', 'ACCUACCU', 'ACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCU']
#rnas = ['ACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCUACCU']
for x in rnas:
	Table = {}
	S = ['.']*len(x)
	print(Structure(x,S,0,len(x)-1))
	print(x)
	print(''.join(S))
