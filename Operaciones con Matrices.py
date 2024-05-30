class mathrixpy:
    def __init__(self, datos: list):  # Inicializa la clase, tomando atributos para definir matriz.
        '''
        Convierte una lista de lista a matriz
        '''
        self.datos = datos  # Se ingresa una lista de listas
        self.filas = len(datos)  # El número de elementos de las lista de datos es igual a el numero de filas
        self.columnas = len(datos[0])  # El número de elementos de cada fila es igual al número de columnas
        # En este caso, se toma a la primer fila de la matriz.

        if not self.verificar_matriz():
            raise ValueError("Todas las filas deben tener la misma longitud")

    def verificar_matriz(self) -> bool:
        '''
        Comprueba que la longitud de todas las filas sea la misma
        '''
        return all(len(fila) == self.columnas for fila in self.datos)  # Aquí toma el tamaño de las filas que hay en la matriz
        # y las mide con la medida inicial de las columnas existentes en la primer fila.

    def dimension_igual(self, other) -> bool:
        '''
        Verifica si dos matrices tienen la misma dimensión
        '''
        return self.filas == other.filas and self.columnas == other.columnas
        # Verifica si las filas de una matriz son iguales, lo mismo con las columnas.

    def __add__(self, other) -> object:  # Entra como la operación + , puesto que ya redefinimos suma
        '''
        Suma dos matrices (Tienen que tener las mismas dimensiones)
        '''
        if not self.dimension_igual(other):  # Verifica si las dimensiones de las dos matrices son iguales llamando
            # a la función "dimension_igual" anteriormente definida.
            raise ValueError('Las matrices tienen que tener las mismas dimensiones')

        matrix = [[0] * self.columnas for _ in range(self.filas)]  # primero expande la lista con el total de espacios de la columna
        # y genera listas a lo largo de las filas.
        # Ejemplo:
        # [[0,0,0,0]] paso 1.
        # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] paso 2

        for i in range((self.filas)):  # Varia sobre las filas de la matriz
            for j in range((self.columnas)):  # Varia sobre las columnas de la matriz
                matrix[i][j] = self.datos[i][j] + other.datos[i][j]  # Definición de suma de matrices y la almacena en matrix

        return mathrixpy(matrix)  # Devuelve la matriz

    def __sub__(self, other) -> object:  # Definición de resta
        '''
        Resta de dos matrices (Tienen que tener las mismas dimensiones)
        '''
        if not self.dimension_igual(other):
            raise ValueError('Las matrices tienen que tener las mismas dimensiones')

        matrix = [[0] * self.columnas for _ in range(self.filas)]

        for i in range((self.filas)):
            for j in range((self.columnas)):
                matrix[i][j] = self.datos[i][j] - other.datos[i][j]  # Definición de resta de matrices, opera igual que la suma

        return mathrixpy(matrix)

    def prod(self, *args) -> object:  # Se define a la función producto con args, un número variable de argumentos.
        '''
        Multiplica una matriz por otra u otras matrices
        '''
        original = self  # Fija a la matriz con la que va a operar.

        for matriz in args:  # Varia sobre los argumentos
            if original.columnas != matriz.filas:
                raise ValueError('El número de columnas de la matriz de la izquierda debe coincidir con el número de filas de la columna de la derecha')
            # Condición necesaria para la multiplicación de matrices.
            resultado = [[0] * matriz.columnas for _ in range(original.filas)]
            # Expande la matriz resultado con el número de columnas de la otra matriz con el número de filas
            # De la matriz original
            for i in range(original.filas):
                for j in range(matriz.columnas):  # Varia sobre filas y columnas
                    suma = 0  # Acumulador
                    for k in range(original.columnas):  # Operación suma por definición de producto matricial
                        # Es decir, los Cij
                        suma += original.datos[i][k] * matriz.datos[k][j]  # Definición de producto de matrices
                    resultado[i][j] = suma  # Al elemento Cij le asigna el valor de la suma
            original = mathrixpy(resultado)  # Convierte la lista de listas en una matriz
        return mathrixpy(resultado)  # Regresa el producto en forma de matriz

    def scalar_mul(self, scalar: float) -> object:  # Define la multiplicación de una matriz por un escalar
        '''
        Multiplica una matriz por un escalar
        '''
        matrix = [[0] * self.columnas for _ in range(self.filas)]  # Extiende la matrix en el número de filas y columnas
        # De la matriz original

        for i in range(self.filas):
            for j in range(self.columnas):  # Varia sobre los Aij de la matriz
                matrix[i][j] = self.datos[i][j] * scalar  # Multiplica cada Aij elemento de la matriz original
                # Y se lo asigna al elemento ij-esimo de la lista matrix

        return mathrixpy(matrix)  # Nos regresa la matriz de la lista matrix

    def tr(self) -> float:  # Nos devuelve un número
        '''
        Devuelve la suma de los elementos diagonales de una matriz cuadrada
        '''
        if not self.filas == self.columnas:  # Verifica si la matriz es cuadrada o no
            raise ValueError('La matriz tiene que ser cuadrada')

        traza = 0  # Contador

        for i in range(self.filas):  # Varia el total de filas
            traza += self.datos[i][i]  # Toma el elemento diagonal de cada columna

        return traza  # Devuelve la traza de la matriz

    def transpuesta(self) -> object:
        '''
        Devuelve una matriz con los índices al revés
        '''
        matrix = [[0] * self.filas for _ in range(self.columnas)]  # Genera una lista de listas de las dimensiones de la matriz

        for i in range(self.filas):
            for j in range(self.columnas):  # Corre sobre los elementos Cij
                matrix[j][i] = self.datos[i][j]  # Asigna el valor Aij a Cji

        return mathrixpy(matrix)

   
    def mIdentidad(numFila: int) -> object:  # Creador de matriz identidad
        '''
        Crea una matriz diagonal con solo números 1 de dimensiones numFila x numFila
        '''
        M = [[0] * numFila for _ in range(numFila)]  # Crea una lista de listas con el tamaño cuadrado que selecciones

        for i in range(numFila):
            M[i][i] = 1  # Asigna a cada elemento de la diagonal el 1
            # Automáticamente los demás elementos tienen el cero
        return mathrixpy(M)  # Crea una matriz con los elementos de la lista de listas

    def potencia(self, potencia: int) -> object:  # Multiplica una matriz por izquierda una n-esima cantidad de veces
        '''
        Eleva una matriz cuadrada a una potencia
        '''
        if potencia < 1:
            raise ValueError('La potencia tiene que ser mayor o igual que 1')  # Debe ser mayor que 1 el exponente
        original = self  # Nos regresa la matriz original

        for _ in range(1, potencia):  # Itera una n-esima cantidad de veces
            original = original.prod(self)  # Transforma la matriz original en el producto con ella misma mediante
            # La función producto antes definida
        return original

    @staticmethod
    def listaToMatriz(datos: list, numFilas: int, numColumnas: int) -> object:  # Crea una matriz mediante listas
        '''
        Genera una matriz de dimensiones deseadas a partir de una lista de números
        '''
        if numFilas * numColumnas != len(datos):
            raise ValueError('Verificar dimensiones')  # Verifica que el producto de filas con columnas sea el número de datos

        M = [[0] * numColumnas for _ in range(numFilas)]  # Expande una lista con el número de filas y columnas

        for i in range(numFilas):
            for j in range(numColumnas):
                M[i][j] = datos[(numColumnas * i) + j]  # Varia sobre los elementos de una lista para cierta columna

        return mathrixpy(M)

    def determinante(self) -> float:
        '''
        Calcula el determinante de una matriz, esta matriz tiene que ser cuadrada
        '''
        if self.filas != self.columnas:
            raise ValueError('La matriz tiene que ser cuadrada')

        if self.filas == 1:
            return self.datos[0][0]

        if self.filas == 2:
            return self.datos[0][0] * self.datos[1][1] - self.datos[0][1] * self.datos[1][0]

        # Para matrices de tamaño mayor a 2x2, usar expansión de cofactores
        det = 0
        for c in range(self.columnas):
            det += ((-1) ** c) * self.datos[0][c] * self.submatriz(0, c).determinante()  # Aplica la definición por cofactores
        return det

    def submatriz(self, fila, columna):
        '''
        Devuelve una submatriz excluyendo la fila y columna especificada
        '''
        submat = [row[:columna] + row[columna + 1:] for row in (self.datos[:fila] + self.datos[fila + 1:])]
        return mathrixpy(submat)

    def cofactor(self, fila, columna):
        '''
        Calcula el cofactor de un elemento en la fila y columna especificada
        '''
        submat = self.submatriz(fila, columna)
        return ((-1) ** (fila + columna)) * submat.determinante()

    def adjunta(self):
        '''
        Devuelve la matriz adjunta de una matriz
        '''
        if self.columnas != self.filas:
                raise ValueError('La matriz debe ser cuadrada')
        Matrizp = [[self.cofactor(i, j) for j in range(self.columnas)] for i in range(self.filas)]
        Adj = mathrixpy(Matrizp).transpuesta()
        Adj.operada = True  # Añadir un atributo para marcar que esta es la adjunta
        return Adj

    def inversa(self):
        Adjunta=self.adjunta()
        DeterminanteI=(1/self.determinante())
        Inversa=Adjunta.scalar_mul(DeterminanteI)
        Inversa.operada=True
        return Inversa
        

    def __str__(self) -> str:
        '''
        Regresa una representación en cadena de la matriz
        '''
        if hasattr(self, 'operada') and self.operada:
            label = "Matriz Operada"
        else:
            label = "Matriz"
    
        mathrixpySTR = '\n'.join('\t'.join(map(str, fila)) for fila in self.datos)
        return f'{label} {self.filas}x{self.columnas}:\n{mathrixpySTR}'


if __name__ == "__main__":
    v = mathrixpy([[1, 2, 7, 5], 
                   [4, 6, 4, 7], 
                   [1, 4, 6, 3],
                   [3,5,7,9]
                   
                   ])
    z = mathrixpy([[1], 
                   [2], 
                   [3]])
    Adjun = v.inversa()
    print(Adjun)
