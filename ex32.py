# Praticando POO - Contas 

from ex31 import Conta

conta1 = Conta(1, 'Guilherme', 300, 1000)
conta2 = Conta(2,'jucelio', 10000, 50000)
conta3 = Conta(3, 'Norma', 50000, 100000)
conta4 = Conta(4,'Julia', 100, 500)

conta1.extrato()
conta1.deposita(300)
conta1.extrato()
conta2.extrato()
conta2.transfere(5000,conta1)
conta1.extrato()
conta2.extrato()
conta1.limite = 2000
conta1.saca(8000)
conta1.extrato()
