from time import process_time 
import BubbleSort, InsetionSort, QuickSort, CriandoDB, shelve

def Escreve(alg,tbase, dado, aux='CompTroca'):
    
    arquivo_out = open(f'{alg}_{tbase}.txt','a')

    if aux != 'tempo':
        arquivo_out.write(f'Número médio de comparações do {alg} com base {tbase} em vetores de:\n500 elementos:\n')
        arquivo_out.write(f'comparações: {dado[0][0]:.1f}      Trocas: {dado[0][1]:.1f}\n')
        arquivo_out.write(f'1000 elementos:\n')
        arquivo_out.write(f'comparações: {dado[1][0]:.1f}      Trocas: {dado[1][1]:.1f}\n')
        arquivo_out.write(f'10000 elementos:\n')
        arquivo_out.write(f'comparações: {dado[2][0]:.1f}      Trocas: {dado[2][1]:.1f}\n')

    else:
        arquivo_out.write(f'\nTempo médio da ordenação do {alg} com base {tbase} em vetores de:\n500 elementos:\n')
        arquivo_out.write(f'{dado[0]}\n')
        arquivo_out.write(f'1000 elementos:\n')
        arquivo_out.write(f'{dado[1]}\n')
        arquivo_out.write(f'10000 elementos:\n')
        arquivo_out.write(f'{dado[2]}\n')

    arquivo_out.close()
        




def Conta_CT(DB, alg):
    resultado = []

    comp = 0
    trocas = 0
    for i in range(1,50+1):
        i = str(i)
        #print(DB[i])
        c, t = alg(DB[i])    
        comp += c
        trocas += t
    #print((comp/50, trocas/50))
    resultado.append((comp/50, trocas/50))

    comp = 0
    trocas = 0
    for i in range(51,80+1):
        i = str(i)
        c, t = alg(DB[i])    
        comp += c
        trocas += t
    #print((comp/30, trocas/30))
    resultado.append((comp/30, trocas/30))

    comp = 0
    trocas = 0
    for i in range(81,83+1):
        i = str(i)
        c, t = alg(DB[i])    
        comp += c
        trocas += t
    #print((comp/3, trocas/3))
    resultado.append((comp/3, trocas/3))

    return resultado


def main():
    base = input('Base: ').strip().capitalize()

    if base == 'Ordenada':
        CriandoDB.CreateDBOrdenada() #Cria o data base
        DataBase = shelve.open('DBOrdenada')

    elif base == 'Inversa':
        CriandoDB.CreateDBInversa() #Cria o data base
        DataBase = shelve.open('DBInversa')
    
    elif base == 'Aleatoria':
        CriandoDB.CreateDBAleatoria() #Cria o data base
        DataBase = shelve.open('DBAleatoria')

    
    valores_comp_trocas_b = Conta_CT(DataBase, BubbleSort.bubblesort_regitros)
    Escreve('bubble',base,valores_comp_trocas_b)
    tempo = BubbleSort.Calcula_Tempo_Bubble(DataBase)
    Escreve('bubble',base,tempo,"tempo")
    
    valores_comp_trocas_i =  Conta_CT(DataBase, InsetionSort.insertionsort_registros)
    Escreve('insertion',base,valores_comp_trocas_i)
    tempo = InsetionSort.Calcula_Tempo_insertion(DataBase)
    Escreve('insertion',base,tempo,"tempo")

    valores_comp_trocas_q = Conta_CT(DataBase, QuickSort.quickSort_registros)
    Escreve('quick',base,valores_comp_trocas_q)
    tempo = QuickSort.Calcula_Tempo_Quick(DataBase)
    Escreve('quick',base,tempo,"tempo")

    DataBase.close()
    return None

if __name__ == '__main__':
    main()
    