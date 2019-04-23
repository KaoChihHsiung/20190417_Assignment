print('''作業5:給予一組學生成績 MatrixA=[100,20,84,96,78,60,55,99,90]，
      請用for迴圈與if-else判斷式決定每個人是否合格。輸出格式如下：1號 100分
      及格、2號 20分 不及格、''')
MatrixA = [100,20,84,96,78,60,55,99,90]     #定義學生成績為MatrixA列表List
Len_Score = len(MatrixA)                    #計算MatrixA長度為Len_Score
for i in range(0,Len_Score):                #用for迴圈產生(0~Len_Score長度)的數,List位置數
    if MatrixA[i] >= 60:                    #判斷分數，若依索引值i取出學生成績>=60，則輸出及格
        print(i+1,'號',MatrixA[i],'及格')    #輸出號碼為i+1，因為索引值從0開始，第一個數編號需加1
    else:                                   #判斷if條件式的分數，若非>=60，則輸出不及格
        print(i+1,'號',MatrixA[i],'不及格')  #輸出號碼為i+1，因為索引值從0開始，第一個數編號需加1