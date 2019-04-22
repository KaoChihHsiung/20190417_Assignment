# 呈現 作業1題目 : 輸入2019年要請假的日期，月份與日期，系統輸出請假日為禮拜幾？
print('作業1:系統一開始要求你輸入你2019年要請假的日期，輸入後系統會輸出你請假的日期為禮拜幾？\n')
off_month = int(input("請輸入2019年您請假的月份(1~12)："))   # 輸入月份值儲存在off_month數值變數中
off_date = int(input("請輸入2019年您請假的日期(1~31)："))    # 輸入日期值儲存在off_date數值變數中
monthday = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] # 2019年1~12月每月依序累積天數
sum_date = monthday[(off_month) - 1] + (off_date) #算輸入請假日為一年中第幾天，減1取list從0開始的第幾個
week_day = sum_date % 7           # 請假日為一年的第幾天，除以7取餘數，存於week_day變數中
if week_day == 1:                 # 判定星期幾？2019年1月1日第1天為禮拜二，sum_date除7餘數1對應星期二..
    print("您請假的日期是：星期二")    #比較請假日除以的7餘數等於1為星期二，以此類推...，因一月一日星期二
elif week_day == 2:
    print("您請假的日期是：星期三")
elif week_day == 3:
    print("您請假的日期是：星期四")
elif week_day == 4:
    print("您請假的日期是：星期五")
elif week_day == 5:
    print("您請假的日期是：星期六")
elif week_day == 6:
    print("您請假的日期是：星期日")
elif week_day == 0:
    print("您請假的日期是：星期一")
else:
    print('輸入錯誤')