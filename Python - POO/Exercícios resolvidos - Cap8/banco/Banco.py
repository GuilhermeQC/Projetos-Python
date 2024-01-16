from Clientes import Cliente
from Contas import Conta

cliente1 = Cliente('José Gomes', "(84) 3232-6655", "001.564.741-78")
cliente2 = Cliente("Júlia Dias", "(84) 99435-7228", "034.123.047-23")
cliente3 = Cliente("Luana Costa", "(84) 3272-5578", "033.654.401-80")
cliente4 = Cliente("Alex Saraiva", "(84) 3642-0278", "025.321.004-52")

conta1 = Conta(1, 100.0, cliente1)
conta1.exibirSaldo()
conta1.depositar(200)
conta1.exibirSaldo()
conta2 = Conta(2, 1500.50, cliente3)
conta2.exibirSaldo()
conta2.sacar(500)
conta2.exibirSaldo()