def calculadigito(digitos_cpf):
    count = len(digitos_cpf) + 1
    soma = 0
    for i in digitos_cpf:
        soma = soma + (int(i) * count)
        count -= 1
    return soma


def adicionadigito(soma, cpf):
    if len(cpf) + 1 == 10:
        cpf += str(0 if ((11 - (soma % 11)) > 9) else 11 - (soma % 11))
        return cpf
    else:
        cpf += str(9 if ((11 - (soma % 11)) == 9) else 11 - (soma % 11))
        return cpf


def cpfigual(cpf_digitado, cpf):
    cpf = (''.join(map(str, cpf)))
    print('CPF Valido' if str(cpf).strip('[]') == cpf_digitado else 'CPF Inválido')


def iniciar():
    cpf_digitado = input('Digite um CPF: ')
    cpf = cpf_digitado[:-2]
    soma_total = calculadigito(cpf)
    cpf = adicionadigito(soma_total, cpf)
    soma_total = calculadigito(cpf)
    cpf = adicionadigito(soma_total, cpf)
    cpfigual(cpf_digitado, cpf)


iniciar()
