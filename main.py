print('Calculadora de IMC')
print('⚠️  O peso e altura devem ser informados com "." \n Exemplo: 1.50✅ 1,50❌')
nome = input('Digite o seu nome: ')
while True:
    try:
        peso = float(input(f"{nome}, informe o seu peso (kg): "))
        break 
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números (ex: 10 ou 5.7).")
while True:
    try:
        altura = float(input("Agora informe a sua altura (m): "))
        break 
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números (ex: 10 ou 5.7).")
resultado_imc = peso / (altura * altura)
print(f"IMC = {resultado_imc}")
if resultado_imc < 18.5:
    print("😞 Abaixo do peso")
elif 18.5 <= resultado_imc < 24.9:
    print("😀 Peso normal")
elif 25 <= resultado_imc < 29.9:
    print("🙁 Sobrepeso")
else:
    print("😢 Obesidade")
