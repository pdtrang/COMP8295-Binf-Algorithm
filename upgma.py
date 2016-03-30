# phylogenetic tree

def Initialize(distance_file):
	Trees = []
	D = {}
	with open(distance_file) as f:
		for line in f:
			items = line.strip().split(" ")
			Trees.append(Node(items[0]))
			for i, node in enumerate(Trees):
				if i<len(Trees)-1:
					D[node.label,items[0]] = D[items[0],node.label] = float(items[i+1])
	return D, Trees


class Node(object):
	def __init__(self, label, left=None, right=None):
		self.label = label
		self.left = left
		self.right = right
		if left is not None and right is not None:
			self.size = left.size + right.size
		else:
			self.size = 1
		self.dist2parent = 0
		self.h = 0

	def Newick(self):
		if self.left is None and self.right is None:
			print('%s:%.2f' % (self.label,self.dist2parent), end="")
		else:
			print("(", end="")
			self.left.Newick()
			print(",", end="")
			self.right.Newick()
			print('):%.2f' % self.dist2parent, end="")


def Merge(D, T, i, j):
	i, j = min(i,j), max(i,j)
	label = T[i].label + ':' + T[j].label
	ck = Node(label, T[i], T[j])
	ck.h = D[T[i].label, T[j].label] / 2
	T[i].dist2parent = ck.h - T[i].h
	T[j].dist2parent = ck.h - T[j].h
	for l,node in enumerate(T):
		if l!=i and l!=j:
			dkl=(D[T[i].label,T[l].label]*T[i].size + D[T[j].label,T[l].label]*T[j].size)/(T[i].size + T[j].size)
			D[label,T[l].label] = D[T[l].label,label] = dkl
	T.pop(i)
	T.pop(j-1)
	T.append(ck)


def ClosestPair(D, T):
	if len(T)<=1 :
		return None,None
	m, mi, mj = D[T[0].label,T[1].label],0,1
	for i in range(len(T)):
		for j in range(i+1, len(T)):
			if m > D[T[i].label, T[j].label]:
				m, mi, mj = D[T[i].label, T[j].label], i, j
	return mi, mj


def UPGMA(distance_file):
	Distance, Trees = Initialize(distance_file)
	while len(Trees) > 1:
		i, j = ClosestPair(Distance, Trees)
		Merge(Distance,Trees,i,j)
	Trees[0].Newick()

UPGMA("phylo_distance.txt")
