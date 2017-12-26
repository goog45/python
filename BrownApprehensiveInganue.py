n = input()
mult = 1
summa = 0
for i in n:
	if i in ['1','2','3','4','5','6','7','8','9']: # или '1' <= i <= '9'
		summa += int(i)
		if int(i) != 0:
			mult *= int(i)
 
print("Сумма цифр:", summa)
print("Произведение значащих цифр:", mult)