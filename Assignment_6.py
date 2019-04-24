print('''作業6:猜數字實作，系統隨機產生一個1~100的目標值，
     接著在每一輪遊戲中，你會隨機猜一個數值，看是否能猜到該數值。
     若猜中，則系統回傳恭喜你猜中了，若你猜的數值比目標值大，
     則系統會回傳目前目標值的範圍為「前一輪最低值範圍,你所猜的數值」
     。反之，若你猜的數值比目標值小，則系統會回傳目前目標值的範圍
     為「你所猜的數值,前一輪最高值範圍」。''')
import random                             # 導入random隨機模組，用內建函式庫randint()功能
target = random.randint(1, 101)           # 從1到100中隨機取出一個整數為目標值target
print('請猜一個0~100的數，看看是否能猜中？\n') # 遊戲提示
play = True                               # 作為循環條件的變量，True則繼續執行
times = 0                                 # 將猜測次數存到times計數變量
guessNumber = [1,100]       #創建一個guessNumber包含1和100的List，並用於儲存plays所輸入的猜測數
while play:                            #猜數為不固定次數的回圈用while，由回圈中的測試條件是否成立決定是否跳出
    guess = input('請從1~100整數中，隨機猜一個數值輸入: ')  #guess為使用者猜數所輸入的數值，轉型為整數
    times = times + 1                     # 每猜一次計數加1
    print('你這次猜的數字是：',guess)
    try:                                  # 檢查輸入的內容是否為數字
        guess = int(guess)                # 把guess輸入字串轉換成整數
    except ValueError:                    # 若數值轉換失敗，便要求player重新再輸入數字
        print('格式錯誤，請輸入數字\n')
        continue
    if guess > 100:                       # 檢查輸入的數字是否介於規定範圍內
        print('數字超出範圍，請輸入[1~100]之間的整數!') #輸入錯誤，便要求重新輸入數字
    elif guess > target:                  # 判斷輸入值與目標值條件式:當猜測值>目標值時
        guessNumber.append(int(guess))    # 先將所輸入值存入guessNumber List中
        print('喔!你猜得太大囉。目標值範圍為:[',min(guessNumber),'~',str(guess),']')
        # 輸出“你猜得太大囉。提示：目標值之範圍為最小值之初始值1~輸入值guess。
        guessNumber.remove(max(guessNumber)) #刪除guessNumber列表中之最大值，由輸入值guess取代為最大值
    elif guess < target:                  # 判斷輸入值與目標值條件式:當猜測值<目標值時
        guessNumber.append(int(guess))    # 先將所輸入的值存入guessNumber List中
        print('喔!你猜得太小囉。目標值範圍為:[',str(guess),'~',max(guessNumber),']')
        # 輸出“你猜得太小囉。提示：目標值之範圍為輸入值guess~最小值(初始值1)。
        guessNumber.remove(min(guessNumber)) # 刪除guessNumber列表中之最小值，由輸入值guess取代
    else:
        print('恭喜你猜中了！你共猜了',str(times),'次') # 不符上面><條件，表示＝目標值，輸出猜中了
        play = False                    # 將循環條件的變量賦值為假false時，停止猜數字退出while循環