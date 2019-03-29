import random
start = int(input('請決定隨機數字開始值: '))
end = int(input('請決定隨機數字結束值: '))
num = random.randint(start, end) #產生隨機數字
count = 0
while True:
	user = int(input('請猜數字: '))
	count += 1
	if user == num:
		print ('恭喜猜對了!!!!共猜測', count, '次')
		break
	elif user > num:
		print('比答案大')
	elif user < num:
		print('比答案小')
	print('已猜測第', count, '次')
