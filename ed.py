x = "yeellow"
y = "fellow"

Table = {}
def D1(x,y,i,j):
	if (i,j) not in Table:
		if j == -1:
			Table[(i,j)] = i+1
		elif i == -1:
			Table[(i,j)] = j+1
		elif x[i] == y[j]:
			Table[(i,j)] = D1(x,y,i-1,j-1)
		else:
			Table[(i,j)] = min(1 + D1(x,y,i-1,j-1), 1 + D1(x,y,i-1,j), 1 + D1(x,y,i,j-1))

	return Table[(i,j)]


i, j = len(x)-1, len(y)-1
print (D1(x,y,i,j))
