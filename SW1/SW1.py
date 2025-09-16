def convert_currency(dollar):
    peso = dollar * 57.17
    yen = dollar * 146.67
    return peso, yen

amount = input("Enter currency in ($): ")
parts = amount.split(",")

print("\nDollar($)\tPhil Peso(P)\tJpn Yen(Y)")

for p in parts:
    dollar = float(p)
    peso, yen = convert_currency(dollar)
    print(f"{dollar:<12}{peso:<15.2f}{yen:.2f}")