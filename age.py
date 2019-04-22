#if_1練習

#age = input('請輸入年齡: ')
#age = int(age)
#if age >= 20:
#	print('你可以投票了!')
#else:
#	print('你還不能投票!')


#if_2練習
age = input('請輸入年齡: ')
age = int(age)
if age < 13:
	print('Hi,小朋友')
elif age >= 13 and age < 18:
	print('Hi,中二生')
elif age >= 18 and age < 22:
	print('Hi,大學生')
elif age >= 22 and age < 30:
	print('你已經是社會人士囉!')
elif age >= 30 and age < 45:
	print('大叔你好!')
else:
	print('老伯你好!')