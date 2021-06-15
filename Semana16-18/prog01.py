
def sequencia_c(tamanho):
    sequencia = []
    i = 1
    while i <= tamanho:
        r = i*i
        sequencia.append(r)
        i +=1
    return sequencia 

# Cria lista vazio
seq = []

# a)
val = 1 # valor Inicial
for i in range(20):
    seq.append(val)
    val += 2
print('Sequencia para letra a)')
print(seq)

# zera lista
seq.clear()

# b)
val = 0 # valor Inicial
for j in range(20):
    val += j + 1
    seq.append(val)
print('Sequencia para letra b)')
print(seq)

# zera lista
seq.clear()

# c)
val = 1 # valor Inicial
for k in range(20):
    val = (k + 1)*(k + 1)
    seq.append(val)
print('Sequencia para letra c)')
print(seq)

