KM_Digitado = float(input("Quantos Km são? "))

if KM_Digitado < 0:
    print("Que viajem é essa véi")
elif KM_Digitado <= 200:
    print(f"Você irá pagar {KM_Digitado*0.50}")
elif KM_Digitado > 200:
    print(f"Você irá pagar {KM_Digitado*0.45}")