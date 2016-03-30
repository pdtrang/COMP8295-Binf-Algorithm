def BWT(seq):
	SA = []
	M = []
	for i in range(len(seq)):
		M.append(seq[i:]+seq[:i])
		SA.append(i)

	SA.sort(key=lambda k: seq[k:])
	M.sort()

	L = ""
	for i in range(len(M)):
		if (M[i] == seq):
			idx = i
		s = M[i]
		L = L + s[len(s)-1]

	return L, idx

def Reconstruct(L,idx):
	F = ['']*len(L)
	
	for i in range(len(L)):
		for j in range(len(F)):
			F[j] = L[j]+F[j]
		F.sort()

	return F[idx]



seq = 'THECATISINTHEHAT'
print ("Sequence:", seq)
L,idx = BWT(seq)

print ("BWT:", L)
print ("index:", idx)

print ("Reconstruct BWT: ", Reconstruct(L, idx))
