def calculate_bmi(height, weight):
    print("Height = "+str(height))
    print("Weight = "+str(weight))

    #Calculating BMI
    bmi = weight / (height * height)

    #Display BMI
    print("Your BMI is "+str(bmi))

    #BMI Classification
    if bmi < 18.5 :
     print("Under Weight")
     return -1
    elif bmi <= 25.0 and bmi >= 18.5 :
     print("Normal Weight")
     return 0
    else :
      print("Overweight")
      return 1
      

calculate_bmi(weight = 50, height = 1.71)