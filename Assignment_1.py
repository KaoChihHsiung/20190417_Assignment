# 作業 1 : 輸入2019年要請假的日期，月份與日期，系統輸出請假日為禮拜幾？
off_month = int(input("請輸入2019年您請假的月份(1~12)："))    # 輸入整數月份
off_date = int(input("請輸入2019年您請假的日期(1~31)："))     # 輸入整數日期
monthday = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  # 2019年1~12月每月依序累積天數
sum_date = monthday[(off_month) - 1] + (off_date)    # 計算所輸入的請假日為一年中的第幾天
week_day = sum_date % 7      # 請假日為一年的第幾天除以7取餘數
if week_day == 1:            # 2019年1月1日第1天為禮拜二，sum_date除7餘數1對應星期二，餘數2對應星期三...
    print("您請假的日期是：星期二")
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