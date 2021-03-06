print(''' 作業2:系統一開始會要求你輸入你三角形三邊的長度，
      接著系統會判斷你輸入的邊長是否可形成三角形
      假設不能形成三角形，出現「輸入錯誤」。假設
      能形成三角形，則繼續檢查是否是等腰三角形、
      還是正三角形，並輸出判斷結果。若什麼都不是
      ，就輸出一般的三角形。\n''')
a = float(input('請輸入三角形三邊長度之第一邊長度(單位：公分)為:'))
b = float(input('請輸入三角形三邊長度之第二邊長度(單位：公分)為:'))
c = float(input('請輸入三角形三邊長度之第三邊長度(單位：公分)為:'))
'''
   判斷使用者輸入的三個邊長是否能夠形成一個三角形，必須符合「任意兩邊之和大於第三邊」
   先用if判斷三個邊任意兩邊和是否小於等於第三邊，若有一不符合則不能形成三角形，印出「輸入錯誤」
   若if不成立False再用elif來分別判斷是三邊相等的正三角形或任兩邊相等但不等於第三邊的等腰三角形。
'''
if a+b<=c or b+c<=a or c+a<=b:                  #判斷是否可以形成三角形
    print('輸入錯誤！你輸入的三邊長為：', a, '、', b, '、', c, '公分，無法形成三角形!')
elif a==b!=c or b==c!=a or c==a!=b:        #判斷是否可以形成等腰三角形但非正三角形
    print('你輸入的三邊長為：', a, '、', b, '、', c, '公分，是一個等腰三角形!')
elif a==b==c:                              #判斷是否可以形成正三角形
    print('你輸入的三邊長為：', a,'、', b,'、', c, '公分，是一個正三角形!')
else:                                      #若上述條件都不符合則輸出一般三角形
    print('你輸入的三邊長為：', a,'、', b,'、', c, '公分，是個一般三角形!')