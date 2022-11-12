import pyfiglet
from termcolor2  import colored
esm = "calculator"
mse = pyfiglet.figlet_format(esm)
mse = colored(mse , color="red")
print(mse)
print(colored("wellcom to my calculator! \n" , color = "red"))
select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')
ask = True
while ask:
 if select == "1":
    print('insert first number :')
    number_1 = float(input())
    print("insert secent number")
    number_2 = float(input())
    x = number_1 + number_2
    print(f"your solve is : {x} \n")
    color1 = "SELECT NEW OPTION :"
    msa_color = colored(color1 , color="red")
    print(msa_color)
    soal = input(" n : braek \n y : again \n m : main menu \n")
    if soal =="n" or soal == "N":
      break
    elif soal == "m" or soal == "M":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')

      print(select)
    elif soal == "y" or soal == "Y":
      continue
    else:
      print("your select number not availebale! app exit automatic")
      break

 elif select == "2":
    print('insert first number :')
    number_1 = float(input())
    print("insert secent number")
    number_2 = float(input())
    x = number_1 * number_2
    print(f"your solve is : {x}")
    color2 = "SELECT NEW OPTION :"
    msa_color = colored(color2 , color="red")
    print(msa_color)
    soal = input(" n : braek \n y : again \n m : main menu \n")
    if soal == "n" or soal == "N":
      break
    elif soal == "m" or soal == "M":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')

      print(select)
    elif soal == "y" or soal == "Y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break

 elif select == "3":
    print('insert first number :')
    number_1 = float(input())
    print("insert secent number")
    number_2 = float(input())
    x = number_1 / number_2
    print(f"your solve is : {x}")
    color3 = "SELECT NEW OPTION :"
    msa_color = colored(color3, color="red")
    print(msa_color)
    soal = input(" n : braek \n y : again \n m : main menu \n")
    if soal == "n" or soal == "N":
      break
    elif soal == "m":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')

      print(select)
    elif soal == "y" or soal == "Y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break

 elif select == "4":
    print('insert first number :')
    number_1 = float(input())
    print("insert secent number")
    number_2 = float(input())
    x = number_1 - number_2
    print(f"your solve is : {x}")
    color4 = "SELECT NEW OPTION :"
    msa_color = colored(color4 , color="red")
    print(msa_color)
    soal = input(" n : braek \n y : again \n m : main menu \n")
    if soal == "n" or soal == "N":
      break
    elif soal == "m" or soal == "M":
      select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')

      print(select)
    elif soal == "y" or soal == "Y":
      continue
    else:
      print("your select number not avalebale! app exit automatic")
      break
 elif select == "5":
      def tavan(adad , tavan1):
       x = 1
       for i in range(tavan1):
        x = x * adad
       return x

      adad = int(input("insert base number : "))
      tavan1 = int(input("insert power number : "))
      print("you answer is : ")
      print(tavan(adad , tavan1))
      color4 = "SELECT NEW OPTION :"
      msa_color = colored(color4 , color="red")
      print(msa_color)
      soal = input(" n : braek \n y : again \n m : main menu \n")
      if soal == "n" or soal == "N":
       break
      elif soal == "m" or soal == "M":
       select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')
 elif select == "6":
        print("select average ")
        adad = []
        c = int(input("how many number calcute average :"))
        for x in range(c):
    
          mark = float(input("number : "))
          adad.append(mark)
          sum = 0
        for x in range(len(adad)):
           sum = sum + adad[x]
    
        print("average is :", sum/c)
        color4 = "SELECT NEW OPTION :"
        msa_color = colored(color4 , color="red")
        print(msa_color)
        soal = input(" n : braek \n y : again \n m : main menu \n")
        if soal == "n" or soal == "N":
         break
        elif soal == "m" or soal == "M":
         select = input('please select option: \n [1]: sum(+) \n [2]: multiplication(*) \n [3]: divide(/) \n [4]: subtraction(-) \n [5]: power \n [6]: average \n [7]: exit \n select option:')

         print(select)
        elif soal == "y" or soal == "Y":
          continue
        else:
          print("your select number not avalebale! app exit automatic")
        break
        


        

 elif select == "7" or select == "q":
    print("okey! see you later!")
    break
 else:
    print("your select number not avalebale! app exit automatic")
    break



print(select)
