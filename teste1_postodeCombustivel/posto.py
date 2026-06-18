PRECO = {
    "G": 5.50,  # Gasolina
    "A": 4.20,  # Etanol
    "D": 6.80   # Diesel
}

tipoComb = input("""Selecione o tipo de combustível:
                 
G - Gasolina
A - Etanol
D - Diesel
""").upper()

litrosComb = float(input("Insira a quantidade de litros:\n"))

subtotal_bruto = PRECO[tipoComb] * litrosComb
subtotal = subtotal_bruto
print (f"Preço bruto: R${subtotal_bruto:.2f}")

cliente_fidelidade = input("O cliente participa do programa fidelidade? (S/N): ").upper()

percentual = 0;
if cliente_fidelidade == "S":
    if tipoComb == "G":
        percentual = 0.03
    elif tipoComb == "A":
        percentual = 0.05
    elif tipoComb == "D":
        percentual = 0.02

    subtotal = subtotal - (subtotal * percentual)
    print(f"Desconto de {percentual*100:.0f}% aplicado. Subtotal: R${subtotal:.2f}")

    if litrosComb >= 40:
        subtotal = subtotal - 5
        print("Desconto adicional de R$5,00 por volume aplicado.")



elif cliente_fidelidade == "N":
    print("Cliente não fidelidade. Nenhum desconto se aplica.")
else:
    print("Opção inválida.")
    exit()

print(f"\nValor total bruto:  R$ {subtotal_bruto:.2f}")
print(f"Valor total líquido: R$ {subtotal:.2f}")