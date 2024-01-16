from clientes import Cliente
from contas import ContaInvestimento

cliente1 = Cliente("Jonas", "93 92391-2341", "032.421.312-12")
conta1 = ContaInvestimento(cliente1, 1000, 10)

conta1.aumentarJuros()
conta1.aumentarJuros()
conta1.aumentarJuros()
conta1.aumentarJuros()
conta1.aumentarJuros()

conta1.exibirExtrato()
