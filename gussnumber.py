import random
num = random.randint(0, 100) #產生隨機數字
count = 0
while True:
	user = int(input('請猜數字(1-100): '))
	count += 1
	if user == num:
		print ('恭喜猜對了!')
		break
	elif user > num:
		print('比答案大')
	elif user < num:
		print('比答案小')
	print('已猜測第', count, '次')
