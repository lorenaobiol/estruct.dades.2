class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades
        self.bucket= cap*[None]

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        self._bucket_put(j, key,value)
        if self._n > len(self._table)//2:
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        j = self._hash_function(key)
        return self._bucket_get(j, key)

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        self._bucket_remove(j, key) 

    def __len__(self):
        return self._n
    
    def _bucket_put(self, j, key:int, value:int):
        if self._table[j] is None:             # posició lliure
            self._table[j]=[[key, value]]  #hi assignes una llista que contingui aquesta parella.
            self._n += 1
        else:
            for k in self._table[j]:
                if k[0] == key:
                    k[1]=value
                    return None
            self._table[j].append([key, value])
            self._n+=1
        if self._n > len(self._table)//2:
            self._resize(2 * len(self._table) - 1)
            
    def _bucket_get(self,j, key: int) -> int:
        if self._table[j] is not None:
            for k in self._table[j]:
                if k[0] == key:
                    return k[1]
        return -1    

    def _bucket_remove(self, j, key: int) -> None:
        if self._table[j] is not None:
            for k in self._table[j]:
                if k[0] == key:
                    self._table[j].remove(k)
                    self._n -= 1
    
    def _resize(self, c):

        taulavella=self._table
        self._table=c*[None]
        self._n=0
        for k in taulavella:
            if k is not None:
                for i in k:
                    self.put(i[0],i[1])
            