#test = 5

#print(test)
#экранирование
#print("Он \"bad\" человек" )


#Перевод строки
#print('Перевод \n строки')

#Конкатенация
#print('Привет это число ' + str(test)  )

#дебильный калькуялятор версия 1

what = input("Что делаем? (+, -): ")

a= float(input("Введи первое число: "))
b= float(input("Введи второе число: "))

if what == "+":
	c = a+b
	print("Результат: "+ str(c))
elif what == "-":
	c = a-b
	print("Результат: "+ str(c))
else:
	print("Введена неверная операция!" )

