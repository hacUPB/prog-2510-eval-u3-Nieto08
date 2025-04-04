def mcd(num, den):
    if num <= den:
        menor= num
    else:
        menor= den
    for divisor in range(menor, 0, -1):
        if num % divisor == 0 and den % divisor == 0:
            maxi_com_div= divisor
            break
    return maxi_com_div
def imprime_fraccion(num, den, nuevon, nuevod):
    acomodo= print(f"{int(num)}/{int(den)}= {int(nuevon)}/{int(nuevod)}")
    return acomodo
def main():
    nume= 10
    denom= 20
    maximo= mcd(nume,denom)
    print (maximo)
    nuev= (nume/maximo)
    nuevd= (denom/maximo)
    impri= imprime_fraccion(nume, denom, nuev,nuevd)
    print(impri)
if __name__== "__main__":
    main()
    
