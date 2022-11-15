from random import randint

cpf_digitado = str(randint(100000000, 999999999))

primeiros_nove_digitos_cpf = cpf_digitado

count_primeiro_digito = 10
soma_total = 0
for valor in primeiros_nove_digitos_cpf:
    soma_total = soma_total+(int(valor)*count_primeiro_digito)
    count_primeiro_digito = count_primeiro_digito - 1

digito1 = 0 if((11 - (soma_total % 11)) > 9) else 11 - (soma_total % 11)
primeiros_nove_digitos_cpf += str(digito1)

count_segundo_digito = 11
soma_total = 0
for valor in primeiros_nove_digitos_cpf:
    soma_total = soma_total+(int(valor)*count_segundo_digito)
    count_segundo_digito = count_segundo_digito - 1

digito2 = 9 if((11-(soma_total % 11)) == 9) else 11 - (soma_total % 11)

primeiros_nove_digitos_cpf += str(digito2)

primeiros_nove_digitos_cpf = (''.join(map(str, primeiros_nove_digitos_cpf)))
print(primeiros_nove_digitos_cpf)

