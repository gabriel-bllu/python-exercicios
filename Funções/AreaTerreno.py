def area(largura, comprimento):
    area = largura*comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {area:.1f}m².")

print(" Controla de Terrenos")
print("-" * 20)
area(float(input("Largura: ")), float(input("Comprimento: ")))