class Graph: 
      
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
        self.adjacency_matrix = []
    
    @staticmethod
    def get_from_adjacency_matrix(d):
 
        graph = Graph(len(d))
        graph.adjacency_matrix = d
        for k,line in enumerate(graph.adjacency_matrix):
            for v in line:
                if int(v) == 1:
                    graph.add_edge(k,int(v))
        return graph

    @staticmethod
    def get_adjacency_matrix_from_top_diagonal(top_diagonal):
        matrix_len = len(top_diagonal)
        matrix = [[0 for x in range(matrix_len)] for y in range(matrix_len)] 

        for l_index, line in enumerate(top_diagonal):
            for c_index, columm in enumerate(line):
                new_c_index = c_index + (matrix_len - len(line))
                matrix[l_index][new_c_index] = top_diagonal[l_index][c_index]
                matrix[new_c_index][l_index] = top_diagonal[l_index][c_index]

        return matrix

    def DFSUtil(self, temp, v, visited): 
  
        visited[v] = True
  
        temp.append(v) 
  
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    def add_edge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    def connected_components(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 
  


def print_matriz(matriz):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matriz]))


print("\n\n")

trabalho = '''
$$$$$$$$\                 $$\                 $$\ $$\                 
\__$$  __|                $$ |                $$ |$$ |                
   $$ | $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\  $$ |$$$$$$$\   $$$$$$\  
   $$ |$$  __$$\ \____$$\ $$  __$$\  \____$$\ $$ |$$  __$$\ $$  __$$\ 
   $$ |$$ |  \__|$$$$$$$ |$$ |  $$ | $$$$$$$ |$$ |$$ |  $$ |$$ /  $$ |
   $$ |$$ |     $$  __$$ |$$ |  $$ |$$  __$$ |$$ |$$ |  $$ |$$ |  $$ |
   $$ |$$ |     \$$$$$$$ |$$$$$$$  |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$  |
   \__|\__|      \_______|\_______/  \_______|\__|\__|  \__| \______/ 
                                                                      
'''
de = '''
      $$\           
      $$ |          
 $$$$$$$ | $$$$$$\  
$$  __$$ |$$  __$$\ 
$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$   ____|
\$$$$$$$ |\$$$$$$$\ 
 \_______| \_______
 '''

grafos = '''
 $$$$$$\                      $$$$$$\                     
$$  __$$\                    $$  __$$\                    
$$ /  \__| $$$$$$\  $$$$$$\  $$ /  \__|$$$$$$\   $$$$$$$\ 
$$ |$$$$\ $$  __$$\ \____$$\ $$$$\    $$  __$$\ $$  _____|
$$ |\_$$ |$$ |  \__|$$$$$$$ |$$  _|   $$ /  $$ |\$$$$$$\  
$$ |  $$ |$$ |     $$  __$$ |$$ |     $$ |  $$ | \____$$\ 
\$$$$$$  |$$ |     \$$$$$$$ |$$ |     \$$$$$$  |$$$$$$$  |
 \______/ \__|      \_______|\__|      \______/ \_______/ 
 '''

print(trabalho)
print(de)
print(grafos)

graphs = {}
option = None

while option != "0":
    print('''
   ___             /\/|         
  / _ \  _ __  __ |/\/  ___  ___
 | (_) || '_ \/ _|/ _ \/ -_)(_-<
  \___/ | .__/\__|\___/\___|/__/
        |_|    )_)              
    '''
)
    print('''
     _ 
    / |
    | |
    |_| - Para carregar um grafo
    ''')

    print('''
     ___ 
    |_  )
     / / 
    /___| - Para criar um novo grafo
    ''')

    print('''
     ____
    |__ /
     |_ \\
    |___/  - Número de componentes conexas
    ''')

    print('''
     _ _  
    | | | 
    |_  _|
      |_|  - Grafos já conhecidos
    ''')
    
    print('''
      __  
     /  \ 
    | () |
     \__/  - sair
    ''')

    print("\n")
    option = input("Digite sua opção:  ")
    print("\n")

    if option == "1":
        graph_name = input("Digite o nome do grafo:  ")
        print("\n")
        print(f"Matriz {graph_name} é:\n")
        print_matriz(graphs[graph_name].adjacency_matrix)

    elif option == "2":
        graph_name = input("Digite o nome do grafo:  ")
        print("\n")

        number_of_vertices = int(input("Digite o número de vertices:  "))
        print("\n")

        lines_of_diagonal_superior = []

        print("Agora será necessário digitar as linhas da diagonal superior, uma a uma!\n\n")
        print("A linha terá que ter o formato => n1;n2;n3 \n\n")

        for i in range(number_of_vertices):

            line = input(f"Digite os elementos da linha {i+1} da diagonal superior, separados por ;(ponto e vírgula):  ")
            print("\n")

            lines_of_diagonal_superior.append(line.split(";"))
        
        m = Graph.get_adjacency_matrix_from_top_diagonal(lines_of_diagonal_superior)
        g = Graph.get_from_adjacency_matrix(m)
        
        graphs[graph_name] = g

        print("A matriz adjavente desse grafo é:\n")
        print_matriz(graphs[graph_name].adjacency_matrix)

        print("\n\n")

    elif option == "3":
        graph_name = input("Digite o nome do grafo: ")
        print("\n")
        print("Número de componentes conexos do grafo escolhido: ", len(graphs[graph_name].connected_components()))
        print("\n")

    elif option == "4":
        graph_name = input("Digite o nome do grafo: ")
        m = None
        graph_type = input('''
            Escolhe qual grafo deseja gerar a matriz de adjacencia
                a - Completo K(n) x
                b - Bipartido completo K(n1,n2) x
                c - Estrela S(n) x
                d - Ciclo C(n) n>=3 x
                e - Roda W(n) n>=3 x
                f - Caminho P(n) x
                g - Cubo Q(n) 
            ''')
        if graph_type == "a":
            n = int(input("Digite o tamanho do n da matriz completa"))
            m = [[0]*n  for i in range(n)]
            for i in range(n):
                for k in range(n):
                    if i != k:
                        m[i][k] = 1

        elif graph_type == "b":
            n1 = int(input("Digite o tamanho do n1: "))
            n2 = int(input("Digite o tamanho do n2: "))
            m = [[0]*(n1+n2)  for i in range(n1+n2)]
            for i in range(n2):
                for k in range(n2, n2+n1):
                    m[i][k] = 1
            for i in range(n1, n1+n2):
                for k in range(n1):
                    m[i][k] = 1

        elif graph_type == "d":
            n = int(input("Digite o tamanho do n: "))
            m = [[0]*n  for i in range(n)]

            m[0][n-1] = 1
            m[n-1][0] = 1

            for i in range(n):
                for k in range(n):
                    if i == (k - 1) or k == (i - 1):
                        m[i][k] = 1

        elif graph_type == "c":
            n = int(input("Digite o tamanho do n: "))
            m = [[0]*n  for i in range(n)]

            for i in range(n):
                for k in range(n):
                    if (i == (n - 1) or k == (n - 1)) and i != k:
                        m[i][k] = 1
                        
        elif graph_type == "e":
            n = int(input("Digite o tamanho do n: "))
            m = [[0]*(n+1)  for i in range(n+1)]

            m[0][n-1] = 1
            m[n-1][0] = 1

            for i in range(n+1):
                for k in range(n+1):
                    if i == (k - 1) or k == (i - 1):
                        m[i][k] = 1
                    if (i == n or k == n) and i != k:
                        m[i][k] = 1

        elif graph_type == "f":
            n = int(input("Digite o tamanho do n: "))
            m = [[0]*n  for i in range(n)]
            for i in range(n):
                for k in range(n):
                    if i == (k - 1) or k == (i - 1):
                        m[i][k] = 1

        elif graph_type == "g":
            n = int(input("Digite o tamanho do n: "))
            m = [[0]*n  for i in range(n)]
            for i in range(n):
                for k in range(n):
                    if i == (k - 1) or k == (i - 1):
                        m[i][k] = 1

        g = Graph.get_from_adjacency_matrix(m)
        graphs[graph_name] = g

        print("A matriz adjavente desse grafo é:\n")
        print_matriz(graphs[graph_name].adjacency_matrix)


# k 2,3

#   0 1 2 3 4
# 0 0 0 1 1 1 
# 1 0 0 1 1 1 
# 2 1 1 0 0 0 
# 3 1 1 0 0 0 
# 4 1 1 0 0 0 

# 0;1;0
# 0;1
# 0