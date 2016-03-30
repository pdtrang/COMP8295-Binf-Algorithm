seq = 'THECATISINTHEHAT'
query = 'IN'


def Search_str(seq,query):
	idx = []
	for i in range(len(seq)-len(query)+1):
		if (query == seq[i:i+len(query)]):
			idx.append(i)
	
	return idx

def Search(seq, query):
	l, r = 0, len(SA)-1

	while l<=r:
		mid = (l+r)//2
		print(l, mid, r, seq[SA[mid]:])
		if seq[SA[mid]:].startswith(query):
			return SA[mid]
		if query < seq[SA[mid]:]:
			r = mid - 1
		else:
			l = mid + 1

	return -1

def BuildSA(seq):
	SA = []
	for i in range(len(seq)):
		SA.append(i)

	SA.sort(key=lambda k: seq[k:])
	return SA

def PrintSA(SA):
	for i in range(len(SA)):
		print('%3d %3d %s' %(i, SA[i], seq[SA[i]:]))

SA=BuildSA(seq)
PrintSA(SA)
print("query", query)
print(Search(seq, query))
