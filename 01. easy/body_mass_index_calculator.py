weight = float(input("What's your weight in kg? "))
height = float(input("What's your height in meters? "))
imc = weight / (height**2)

if imc < 18.5:
    print("You're underweight")
elif 18.6 < imc < 24.9:
    print("You're normal weight")
elif 25 < imc < 29.9:
    print("you're overweight")
elif 30 < imc < 34.9:
    print("you're obese class I")
elif 35 < imc < 39.9:
    print("you're obese class II")
else:
    print("you're obese class III")