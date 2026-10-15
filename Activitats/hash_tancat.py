# Estats d'una posició de la taula (hash tancat). NO canvieu aquests valors.
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for _ in range(cap)]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        pos=self.__find(key)
        if pos is not None:
            self._table[pos][1]=value
        else:
            j = self._hash_function(key)
            inici=j
            while self._table [j][2] != LLIURE and self._table [j][2] != ESBORRAT:
                j=(j+1)%len(self._table)
                if inici==j:
                    break

            if self._table[j][2] != OCUPAT:
                self._table[j][0] = key
                self._table[j][1] = value
                self._table[j][2] = OCUPAT
                self._n += 1 
            if self._n > len(self._table) // 2:
                self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        pos=self.__find(key)
        if pos is not None:
            return self._table[pos][1]
        return -1

    def remove(self, key: int) -> None:
        pos=self.__find(key)
        if pos is not None:
            self._table[pos] = [None,None,ESBORRAT]
            self._n -= 1 

    def _resize(self, c: int):
        taulavella=self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0
        for casella in taulavella:
            if casella is not None and casella[2] == OCUPAT:
                self.put(casella[0], casella[1])
        

    def __len__(self):
        return self._n
    
    def __find(self, key: int): #retorna la posicio on es la clau o None
        j = self._hash_function(key)
        inici=j
        while self._table [j][2] != LLIURE:
            if (self._table[j][2] == OCUPAT and self._table[j][0] == key):
                return j
            else:
                j=(j+1)%len(self._table)

            if inici==j:
                return None
        return None
        
