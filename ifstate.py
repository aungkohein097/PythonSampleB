#x = int(input("Please enter an integer: "))
#if x < 0:
#		x = 0
#		print('Negative changed to zero')
#elif x == 0:
#	print('Zero')
#elif x == 1:
#		print('Single')
#else:
#	print('More')
#x = int(input("Please enter an integer: "))
#if x < 60:
#	print('x is greater than 50')
#elif x > 40:
#	print('x is greater than 40')
#elif x > 30:
#	print('x is greater than 30')
#else:
#	print('Nothing')
#x = int(input("Please enter an integer: "))
#if x < 75 and x > 40 :
#	print('Go to Bagan')
#elif x < 40 and x > 10:
#	print('Youth go to beach')
#elif x < 10 and x > 0 :
#	print('Go to playground')
#elif x > 75
#	print('Unlisted')
#else:
#	print('Error')
x = int(input("Please enter an integer: "))
if x == 100:
	print('Scholar')
elif x >= 70 and x < 100:
	print('Distinction')
elif x >= 50 and x < 70:
	print('Excellent')
elif x <= 39 and x > 35:
	print('Moderation')
elif x  >= 40 and x > 10:
	print('Fail')
elif x <= 10 and x > 0:
	print('Warning')
else :
	print('Invalid mark')