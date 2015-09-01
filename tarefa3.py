nome_numeros = "zero um dois tres quatro cinco seis sete oito nove".split(" ")

def num_texto(num):
    aux = ''
    for x in str(num):
        aux += nome_numeros[int(x)] + ', '
    return aux[:-2]
        
def texto_num(texto):
    aux=''
    texto = texto.split(', ')
    for x in texto:
        aux += str(nome_numeros.index(x))
    return int(aux)

#assert 123065789008 == texto_num('um, dois, tres, zero, seis, cinco, sete, oito, nove, zero, zero, oito')
#assert 'um, dois, tres, zero, seis, cinco, sete, oito, nove, zero, zero, oito' == num_texto(123065789008)
