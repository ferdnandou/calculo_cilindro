# Definição da constante
PI = 3.14159

# Entrada de dados
raio = float(input("Digite o valor do raio do cilindro: "))
altura = float(input("Digite o valor da altura do cilindro: "))

# Cálculo do volume do cilindro
volume = PI * (raio ** 2) * altura

# Cálculo da área da base do cilindro
area_base = PI * (raio ** 2)

# Exibição dos resultados
print(f"\nVolume do cilindro: {volume:.2f}")
print(f"Área da base do cilindro: {area_base:.2f}")
