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
    elif bmi <= 25.0 and bmi >= 18.5 :
     print("Normal Weight")
    else :
      print("Overweight");
      

calculate_bmi(weight = 50, height = 1.71)