saldo = 1000
saque = 200
limites = 500

print(saldo >= saque and saque <= limites)
print(saldo >= saque or saque <= limites)

print(not (saldo >= saque and saque <= limites))
print(not (saldo >= saque or saque <= limites))

print(saldo >= saque and saque <= limites and saldo > 0)
print(saldo >= saque or saque <= limites or saldo > 0)
print(not (saldo >= saque and saque <= limites and saldo > 0))
print(not (saldo >= saque or saque <= limites or saldo > 0))
print(saldo >= saque and (saque <= limites or saldo > 0))


