ans=input("Enter the no of grid(type \'m\' for manual else default board) :").strip().lower()
if ans=='m':
    n=int(input("Enter the number of grids : "))
    board=[]
    print("Enter the elements row-wise (\"0\" for empty cells):")
    for i in range(3*n):
        print("Enter the row {} elements :".format(i+1))
        a=list(map(int,input().split()))
        board.append(a)
else:
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
def printboard(l):
    for i in range(len(l)):
        if i%3==0 and i!=0:
            print("-"*20)
        for j in range(len(l[0])):
            if j%3==0 and j!=0:
                print('|',end=" ")
            if l[i][j]==0:
                print("?",end=" ")
            else:
                print(l[i][j],end=" ")
        print()

def valid(l,r,c,ele):
    for i in range(len(l)):
        if l[r][i]==ele and i!=c:
            return 0
    for i in range(len(l)):
        if l[i][c]==ele and i!=c:
            return 0
    x=r//3
    y=c//3
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if l[i][j]==ele and [i,j]!=[r,c]:
                return 0
    return 1
def solve(l):
    if not empty(l):
        return True
    r,c=empty(l)
    for i in range(1,10):
        if valid(l,r,c,i): 
            l[r][c]=i
            if solve(l):
                return True
            l[r][c]=0
    return False           
def empty(l):
    for i in range(len(l[0])):
        for j in range(len(l[0])):
            if l[i][j]==0:
                return i,j
    return None
print("QUESTION :\n")
printboard(board)
solve(board)
print("\n")
print("ANSWER :\n")
printboard(board) 
