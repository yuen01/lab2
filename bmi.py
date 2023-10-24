def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    height2 = height * height
    bmi = weight / height2
    print(bmi)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 25.0:
        return "Normal Weight"
    else:
        return "Overweight"


print(calculate_bmi(weight=57, height=1.73))

