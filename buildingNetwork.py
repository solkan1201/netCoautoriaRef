print("estou dentro")
#import numpy  as np
import csv

# funcion para preencher o diccionario
def comporDict (ddd):
    dictTemp = {}
    for ii in range(1, len(ddd)):
        dictTemp[ii] = ddd[ii]
    return dictTemp

def imprimir(mdict, ite):
    for ii in range(1, ite + 1):
        print(mdict[ii][3])
def preencherList(mlist):
    temp = list()
    if type(mlist) == list:
        for ii in range(len(mlist)):
            temp.append(mlist[ii])
    else:
        temp.append(mlist)
    return temp
# criar os pares de autores
def secuencias(dd):
    tt = list()
    if type(dd) == list:
        for ii in range(len(dd)-1):
            for jj in range(ii + 1,len(dd)):
                tt.append([dd[ii], dd[jj]])
    else:
        tt.append([dd , dd])
    return tt
# alinhas as listas
def alinhar(l):
    ext = list()
    for ele in l:
        #print(ele)
        linha = str(ele[0])
        for gg in range(1, len(ele)):
            linha = linha + ';' + ele[gg]
        print(linha)
        ext.append(linha)
    return ext

#dados = open('production.csv', 'r')
with open('intelectualproduction2013_2016.csv', 'r') as f:
    dados = list(csv.reader(f, delimiter=';'))
    titul = ''
    conta = 0
    bancDict = {}
    for kk in range(0, len(dados)):
        dd = dados[kk]
        #print(dd)
        if conta < 2:
            if conta == 0:
                #print("contador ", conta)
                nn = 0
                dictKey = {}
                for ii in dd:
                    dictKey[nn] = ii
                    nn += 1
                #print(dictKey)
                conta += 1
            else:
                #print("contador ", conta)
                dictT = comporDict(dd)
                #print(dictT)
                bancDict[conta] = dictT
                print("elemento %d do dict"%(conta))
                imprimir(bancDict, conta)
                conta += 1
        else:
            titul = dd[2]
            print(titul)
            print(bancDict[conta -1][2])
            #letor = dd[3]
            # cont representa cada artigo ou livro na tabela
            if (titul == bancDict[conta - 1][2]):
                tempAut = preencherList(bancDict[conta - 1][3])
                print("autores ", tempAut)
                if dd[3] not in tempAut:
                    tempAut.append(dd[3])
                bancDict[conta-1][3] = tempAut
                print(bancDict[conta-1][3])
            else:
                dictT = comporDict(dd)
                print("adicionando")
                bancDict[conta] = dictT
                print("elemento %d do dict"%(conta))
                imprimir(bancDict, conta)
                conta += 1
                #dictT = comporDict(dd, dictKey)
                #bancDict[cont] = dictT
# ate aqui diccionario pronto

listOut = list()
# construir o head
elem = [str(dictKey[3]) + '1']
elem.append(str(dictKey[3]) + '2')
elem.append(dictKey[1])
elem.append(dictKey[2])
elem.append(dictKey[4])
elem.append(dictKey[5])
elem.append(dictKey[6])
print(elem)
listOut.append(elem)

for prod in range(1, conta):
    temp = secuencias(bancDict[prod][3])
    for ii in range(len(temp)):
        elem = temp[ii]
        elem.append(bancDict[prod][1])
        elem.append(bancDict[prod][2])
        elem.append(bancDict[prod][4])
        elem.append(bancDict[prod][5])
        elem.append(bancDict[prod][6])
        print(elem)
        listOut.append(elem)
#ate aqui lista de coautores pronta
with open("coautoriaBDPub2013_2016.csv","w") as f:
    wr = csv.writer(f,delimiter="\n")
    ext = alinhar(listOut)
    wr.writerow(ext)
print("guardado")