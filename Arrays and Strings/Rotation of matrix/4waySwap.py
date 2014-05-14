def FourWaySwap(s):
	temp = s[3]
	s[3] = s[2]
	s[2] = s[1]
	s[1] = s[0]
	s[0] = temp
	return s

def RotateMatrix(Matrix):
        NumberOfRows = len(Matrix)
        NumberOfColumns = len(Matrix[0])
        if(NumberOfColumns != NumberOfColumns):
                return Matrix
        n = NumberOfColumns
        for layer in xrange(n):
                first = layer
                last = n - 1 - layer
                for i in xrange(layer,n - layer-1):
                        offset = i - first
                        top = Matrix[first][i]
                        Matrix[first][i] = Matrix[last-offset][first]
                        Matrix[last-offset][first] = Matrix[last][last - offset]
                        Matrix[last][last - offset] = Matrix[i][last]
                        Matrix[i][last] = top
        return Matrix         

                

print FourWaySwap([1,2,3,4])
Matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Matrix = RotateMatrix(Matrix)
for i in range(len(Matrix)):
        print str(Matrix[i][0])+"  " +str(Matrix[i][1])+"  " +str(Matrix[i][2])+"  " +str(Matrix[i][3])+"  " 
