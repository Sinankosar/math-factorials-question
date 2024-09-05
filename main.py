import math
import string
def FirstFactorial(num):
    # code goes here
    #Sinan Koşar
    # import math ve math.factorial(num) komutu ile kısa yoldan cevaba ulaşabiliriz.
    # num =math.factorial(num)
    top=1

    if str(num) in string.digits: #int değer olmasını kontrol ettik float olamaz
        if num <= 18:
            for i in range(1,num+1):
                top *= i
    num = top
    return num


# keep this function call here
print(FirstFactorial(4))