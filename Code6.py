# 6. Após a queda de um raio um observador anotou o tempo, em segundos, entre a luz e o som do raio. Considerando a velocidade do som igual a 340 m/s, faça um programa que receba o tempo medido por um observador e imprima a distância, em kilometros, do observador até o ponto de queda do raio.

tempo = float(input('Digite o tempo, em segundos, do som propagado: '))
metros = 340 * tempo
kilometros = metros // 1000

print('A distacia do observador em relação ao raio é %.2f km'%(kilometros))