#Comissão vendedores

vendedor = str(input("Informe o nome do vendedor(a)! \n"))
codigo_peça = int(input("Informe o código da peça! \n"))
precoUN = float(input("Informe o valor da peça! \n"))
qtd = int(input("Informe a quantidade de pelas vendidas!"))
comissão = ((precoUN*qtd)*0.05)

print (f"#Confirmação#")
print (f"Vendedor(a): {vendedor}")
print (f"Preço total: {precoUN*qtd}")

print (f"A comissão a ser recebida pelo(a) vendedor(a) {vendedor} é de: {comissão}")
