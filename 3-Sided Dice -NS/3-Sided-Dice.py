from math import copysign

def mvmult(M, v):
    b_1 = M[0][0]*v[0][0] + M[1][0]*v[1][0] + M[2][0]*v[2][0]
    b_2 = M[0][1]*v[0][0] + M[1][1]*v[1][0] + M[2][1]*v[2][0]
    b_3 = M[0][2]*v[0][0] + M[1][2]*v[1][0] + M[2][2]*v[2][0]
    return (b_1, b_2, b_3)
def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)

    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
def main():
    x_1,y_1,z_1 = map(int, input().split(' '))
    if x_1==y_1==z_1==0:
        return
    x_2,y_2,z_2 = map(int, input().split(' '))
    x_3,y_3,z_3 = map(int, input().split(' '))
    b_1,b_2,b_3 = map(int, input().split(' '))


    A = [[x_1,x_2,x_3], [y_1,y_2,y_3], [z_1,z_2,z_3]]
    b = [[b_1],[b_2],[b_3]]
    if getMatrixDeternminant(A) != 0:
        print("YES")
        # Ai = getMatrixInverse(A)
        # b_1, b_2, b_3 = mvmult(Ai, b)
        # print("NO" if copysign(1, b_1) < 0 or copysign(1, b_2) < 0 or copysign(1, b_3) < 0 else "YES")
    else:
        print("NO")
    input()
    main()
# Change the way the probabilities are interpeted.
if __name__ == "__main__":
    main()