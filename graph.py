class Graph: 
      
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
        self.adjacency_matrix = []
    
    def get_coloring(self):
        black_list = {}
        coloring = {}
        for i in range(len(self.adj)):
            colored = False
            for c in list(coloring.keys()):
                if c in black_list:
                    if not i in black_list[c]:
                        coloring[c].append(i)
                        colored = True
            if not colored:
                new_color = str(len(list(coloring.keys())) + 1)
                coloring[new_color] = []
                coloring[new_color].append(i)
                black_list[new_color] = self.adj[i]
        return coloring

    def is_eurelian(self):
        cc = self.connected_components()
        for v in self.adj:
            if len(v) % 2 != 0:
                return False
        return True

    @staticmethod
    def _do_mycielski(matrix):
        new_matrix = []
        new_lenght = len(matrix) * 2 + 1
        for i in range(new_lenght):
            new_matrix.append([0]*new_lenght)
        

        m = 0
        n = 0
        for i in range(new_lenght):
            for k in range(new_lenght):
                if n == len(matrix):
                    n = 0
                if m == len(matrix):
                    m = 0
                new_matrix[i][k] = matrix[m][n]
                n = n + 1
            m = m + 1

        for i in range(new_lenght):
            for k in range(new_lenght):
                if (new_lenght - 1) == i and  k < new_lenght // 2:
                    new_matrix[i][k] = 0
                elif (new_lenght - 1) == i and  k >= new_lenght // 2:
                    new_matrix[i][k] = 1
                elif (new_lenght - 1) == k and  i < new_lenght // 2:
                    new_matrix[i][k] = 0
                elif (new_lenght - 1) == k and  i >= new_lenght // 2:
                    new_matrix[i][k] = 1
                
        
        new_matrix[new_lenght - 1][new_lenght - 1] = 0
        return new_matrix

    @staticmethod
    def create_mycielski_matrix(clique=2, coloring=2):
        new_matrix = []
        if coloring == 2:
            for i in range(2):
                new_matrix.append([0]*2)
            new_matrix[0][0] = 0
            new_matrix[0][1] = 1
            new_matrix[1][0] = 1
            new_matrix[1][1] = 0
            return new_matrix

        return Graph._do_mycielski(Graph.create_mycielski_matrix(clique, coloring - 1))

    @staticmethod
    def get_from_adjacency_matrix(d):
 
        graph = Graph(len(d))
        graph.adjacency_matrix = d
        for k,line in enumerate(graph.adjacency_matrix):
            for i,v in enumerate(line):
                if int(v) == 1:
                    graph.add_edge(k,i)
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
  


def print_matriz(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))

def save_matrix(matrix, filename):
    f = open(filename, "w")
    line = ""
    lines = ""
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            line = line + str(matrix[i][k]) + " "
        lines = lines + (line + "\n")
        line = ""
    f.write(lines)
    f.close()

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
     ___ 
    | __|
    |__ \\
    |___/  - Coloração e número gastos de cores
    ''')

    print('''
      __ 
     / / 
    / _ \\
    \___/ - Gerar grafo Mycielski
    ''')

    print('''
     ____ 
    |__  |
      / / 
     /_/  - Verificar se um grafo é Eureliano
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
        filename = None
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
            n = int(input("Digite o tamanho do n da matriz completa: "))
            m = [[0]*n  for i in range(n)]
            filename = "cubo" + str(n)
            for i in range(n):
                for k in range(n):
                    if i != k:
                        m[i][k] = 1

        elif graph_type == "b":
            n1 = int(input("Digite o tamanho do n1: "))
            n2 = int(input("Digite o tamanho do n2: "))
            m = [[0]*(n1+n2)  for i in range(n1+n2)]
            filename = "bipartido" + str(n1) + "_" + str(n2)
            for i in range(n2):
                for k in range(n2, n2+n1):
                    m[i][k] = 1
            for i in range(n1, n1+n2):
                for k in range(n1):
                    m[i][k] = 1

        elif graph_type == "d":
            n = int(input("Digite o tamanho do n: "))
            filename = "ciclo" + str(n)
            m = [[0]*n  for i in range(n)]

            m[0][n-1] = 1
            m[n-1][0] = 1

            for i in range(n):
                for k in range(n):
                    if i == (k - 1) or k == (i - 1):
                        m[i][k] = 1

        elif graph_type == "c":
            n = int(input("Digite o tamanho do n: "))
            filename = "estrela" + str(n)
            m = [[0]*n  for i in range(n)]

            for i in range(n):
                for k in range(n):
                    if (i == (n - 1) or k == (n - 1)) and i != k:
                        m[i][k] = 1
                        
        elif graph_type == "e":
            n = int(input("Digite o tamanho do n: "))
            m = [[0]*(n+1)  for i in range(n+1)]
            filename = "roda" + str(n)
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
            filename = "caminho" + str(n)
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
        # save_matrix(m, filename)
        print_matriz(graphs[graph_name].adjacency_matrix)
    
    elif option == "5":
        graph_name = input("Digite o nome do grafo: ")
        g = graphs[graph_name]
        print("No formato color: [vertices]")
        coloring = g.get_coloring()
        for color in coloring:
            print(f"{color}: {coloring[color]}")

    elif option == "6":
        graph_name = input("Digite o nome do grafo: ")
        cliques = int(input("Digite o número de cliques: "))
        coloring = int(input("Digite o número de chi: "))
        m_matrix = Graph.create_mycielski_matrix(cliques, coloring)
        g = Graph.get_from_adjacency_matrix(m_matrix)
        graphs[graph_name] = g
        print_matriz(m_matrix)

    elif option == "7":
        graph_name = input("Digite o nome do grafo: ")
        is_e = graphs[graph_name].is_eurelian()
        msg = "O grafo é Eureliano" if is_e else "O grafo não é Eureliano"
        print("Resposta: " + msg)


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

# 0 1 0