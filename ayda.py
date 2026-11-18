توی فایل پایتونه اینو بنویسید 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر امکان‌پذیر نیست!"
    return x / y

print("ماشین حساب ساده 🧮")
print("عملیات‌های موجود: 1(جمع) - 2(تفریق) - 3(ضرب) - 4(تقسیم)")

while True:
    choice = input("\nشماره عملیات مورد نظر را وارد کنید (1/2/3/4) یا 'q' برای خروج: ")
    
    if choice.lower() == 'q':
        break
        
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("عدد اول را وارد کنید: "))
            num2 = float(input("عدد دوم را وارد کنید: "))
        except ValueError:
            print("لطفاً یک عدد معتبر وارد کنید!")
            continue

        if choice == '1':
            print(f"نتیجه: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"نتیجه: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"نتیجه: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"نتیجه: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("ورودی نامعتبر است. لطفاً بین 1 تا 4 انتخاب کنید.")
