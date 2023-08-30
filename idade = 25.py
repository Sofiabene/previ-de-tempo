altura= float(input("digite sua altura:"))
peso= float(input("digite seu peso:"))

print("resultado do imc:")
imc =peso/ (altura * altura)
print (imc)

if(imc < 18.5):
    print("abaixo do peso")
elif(imc < 25):
    print("peso normal")
elif(imc < 30):
    print("sobrepeso")
elif(imc < 35):
    print("obesidade grau 1")
elif(imc < 40):
    print("obesidade grau 2")