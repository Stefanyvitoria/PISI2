import time, shelve, CriandoDB
import BubbleSort, InsetionSort, QuickSort

def Escreve(Dic_infor, Alg, Base, v,e):
    dados = open(f'Dados_{Alg}_{Base}.txt', 'a', encoding='UTF-8')
    dados.write(f'\nTeste dos {v} vetores com {e}.\n')
    for i in Dic_infor:
        if i == 'Dados_individual':
            print(Dic_infor[i])
        else:
            dados.write(i+'='+str(Dic_infor[i])+'\n')
    dados.close()

def Calcula(DB,com,ate, f,alg,algr, vetor):
    vetor = {}

    valores, comp, trocas, t_total = [], 0, 0, 0
    for c in range(int(f'{com}'),int(f'{ate}')):
        c = str(c)
        #Marca o tempo tempo de ordenação de cada vetor 
        T1 = time.time()
        alg(DB[c])
        T2 = time.time()
        t_total += T2-T1
        #Marca o número de trocas e comparações
        val = algr(DB[c]) 
        comp += val[0]
        trocas += val[1]

        valores.append([T2-T1, val[0], val[1]])

        if len(valores) == f:
            vetor['Dados_individual'] = valores.copy()
            vetor['Tempo_PorVetor'] = t_total/f
            vetor['Comparacao_PorVetor'] = comp/f
            vetor['Trocas_PorVetor'] = trocas/f
            vetor['Tempo_total'] = t_total
            vetor['Comparacao_total'] = comp
            vetor['Troca_total'] = trocas
            break
    return vetor

def main():
    base = input('Base: ').strip().capitalize()
    if base == 'Ordenada':
        CriandoDB.CreateDBOrdenada()
        DB = shelve.open('DBOrdenada')
    elif base == 'Inversa':
        CriandoDB.CreateDBInversa()
        DB = shelve.open('DBInversa')
    elif base == 'Aleatoria':
        CriandoDB.CreateDBOrdenada()
        DB = shelve.open('DBAleatoria')

    algoritmo = input('Algoritmo: ').strip().capitalize()
    if algoritmo == 'Bubble':
        alg = BubbleSort.bubblesort
        algr = BubbleSort.bubblesort_regitros
    elif algoritmo == 'Insertion':
        alg = InsetionSort.insertionsort
        algr = InsetionSort.insertionsort_registros
    elif algoritmo == 'Quick':
        alg = QuickSort.quicksort
        algr = QuickSort.quicksort_registros

    vetor500 = Calcula(DB, 1, 51, 50,alg, algr,'vetor500x50')
    Escreve(vetor500, algoritmo, base,50, 500)
    vetor100 = Calcula(DB, 51, 81, 30,alg, algr,'vetor100x30')
    Escreve(vetor100, algoritmo, base, 30, 1000)
    vetor10000 = Calcula(DB, 81, 84, 3,alg, algr,'vetor10000x3')
    Escreve(vetor10000, algoritmo, base, 3, 10000)
    
    DB.close()
    return None

if __name__ == '__main__':
    main()