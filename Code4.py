# 4. Faça um programa que transforma uma temperatura fornecida em Celsius para a correspondente em Fahrenheit. Faça uma pesquisa para encontrar a fóruma de conversão. C=9/5+(F−32)

print('Programa de Converção de °C em °F')
tempCelcius = float(input('Digite a temperatura em Celcius: '))
tempFahrenheit = (1.8*tempCelcius + 32)
print('A temperatura de %.2f°C equivale a %.2f°F'%(tempCelcius, tempFahrenheit))