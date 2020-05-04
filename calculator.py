income=int(input('what\'s your salary?'))
salary=0
shouldPay=0
tax=0
def calculator(num):
	shouldPay=num-5000
	if shouldPay<=0:
		tax=0
	elif 0<shouldPay <=3000:
		tax=shouldPay*0.03
	elif 3000 < shouldPay <=3000:
		tax=shouldPay*0.1-210
	elif 12000< shouldPay <=25000:
		tax=shouldPay<=0.2-1410
	elif 25000< shouldPay <=25000:
		tax=shouldPay*0.2 -1410
	elif 35000 <shouldPay <=55000:
		tax=shouldPay *0.3-4410
	elif 55000<shouldPay <=80000:
		tax=shouldPay*0.35-1760
	else:
		tax=shouldPay*0.45-15160
	salary=income-tax
	return '{:.2f}'.format(salary)
print('your income after taxed {}'.format(calculator(income)))
