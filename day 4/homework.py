#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
#აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს ჯამი

number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
number3 = int(input("enter number3: "))

#საინკრემენტაციო ცვლადი 
#13, 20, 7 ავიღოთ მაგალითად
my_sum = 0
if number1 % 2 == 1:
    my_sum += number1   #my_sum-ი გაუტოლდა 13-ს
if number2 % 2 == 1:
    my_sum += number2  #არაფერი არ შეიცვალა
if number3 % 2 == 1:
    my_sum += number3 #my_sum გაუტოლდა 13+7 =20
print("the sum of odd numbers is {}".format(my_sum))

#შევიყვანეთ სამი რიცხვი ტერმინალში, რის შემდეგაც შევკრიბეთ ორი კენტი რიცხვი და ჯამი მივიღეთ 20