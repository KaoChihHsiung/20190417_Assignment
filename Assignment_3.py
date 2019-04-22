print(''' 作業3:給予兩個矩陣 MatrixA = [0,2,4,6,8]，
      以及MatrixB =[1,3,5,7,9]，請一一列出這兩個矩陣
      任兩數相乘的結果。例如：0*1=0,0*3=0,...''')
MatrixA = [0,2,4,6,8]          #創建表列List，MartixA，相當於range(0,10,2)
MatrixB = [1,3,5,7,9]          #創建表列List，MartixB，相當於range(1,10,2)
for A in range(0, 10,2):       #用for控制矩陣中的變數Ａ與range函數，range(start,end,step)
    for B in range(1, 10 ,2):
        print(A,'*',B,'=',A*B)