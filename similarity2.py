INDEL_SCORE = -8
SUB_SCORE = -1
ID_SCORE = 5

Table = {}
def GAlign(x,y,i,j):
	if (i,j) not in Table:
		if j == -1:
			Table[(i,j)] = INDEL_SCORE*(i+1)
		elif i == -1:
			Table[(i,j)] = INDEL_SCORE*(j+1)
		elif x[i] == y[j]:
			Table[(i,j)] = ID_SCORE + GAlign(x,y,i-1,j-1)
		else:
			Table[(i,j)] = max(SUB_SCORE + GAlign(x,y,i-1,j-1), INDEL_SCORE + GAlign(x,y,i-1,j), INDEL_SCORE + GAlign(x,y,i,j-1))
			
	return Table[(i,j)]

def LAlign(x,y,i,j):
	if (i,j) not in Table:
		if j == -1:
			Table[(i,j)] = 0
		elif i == -1:
			Table[(i,j)] = 0
		elif x[i] == y[j]:
			Table[(i,j)] = max(ID_SCORE + LAlign(x,y,i-1,j-1), 0)
		else:
			Table[(i,j)] = max(SUB_SCORE + LAlign(x,y,i-1,j-1), INDEL_SCORE + LAlign(x,y,i-1,j), INDEL_SCORE + LAlign(x,y,i,j-1), 0)
			
	return Table[(i,j)]

x = "AKJGT"
y = "DKLJT"
i, j = len(x)-1, len(y)-1
# print (GAlign(x,y,i,j))
print (LAlign(x,y,i,j))
# print (Table)
print (max(Table.values()))
