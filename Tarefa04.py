#1

def separaStr(s1):
    s1=s1.split(' ')
    print(s1)

separaStr('Miritiba 339')




#2
def ehNumero(x):
    if x in '0123456789':
        return True
    else:
        return False


def enderecosStrSeparados(endereco):
    num=''
    nome=''
    l=[]

    for el in endereco:
        if ehNumero(el)== True:
            num+=el
        else:
            nome+=el
    print(endereco)

    l.append(nome)
    l.append(num)
    print(l)

enderecosStrSeparados('Rio Branco 23')
                



#3-a,b,c
def ehNumero(x):
    if x in '0123456789':
        return True
    else:
        return False


def enderecosStrSeparados(endereco):
    num=''
    nome=''
    l=[]

    endereco = endereco.replace(",", "")

    for el in endereco:
        
        if ehNumero(el)== True:
            num+=el
        else:
            nome+=el
        
    print(endereco)

    l.append(nome)
    l.append(num)
    print(l)

enderecosStrSeparados('4, Rue de la République')





#3-d

def ehNo(endereco):  
    l=[] 
    if 'No' in endereco:
      endereco = endereco.split('No')
      rua= endereco[0]
      num = "No" + endereco[1]
      l.append(rua)
      l.append(num)
      print(l)
    else:
       enderecosStrSeparados(endereco)


ehNo('Calle 44 No 1991')   
    
     
    

        


