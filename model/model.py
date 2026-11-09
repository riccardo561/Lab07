from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        return self._libro_dao.ottieni_libri_filtrati(biblioteca,genere)

    def get_generi(self):
        risultato=self.get_libri()
        self.lista_generi=[]
        for libro in risultato:
            if libro.genere not in self.lista_generi:
                self.lista_generi.append(libro.genere)
        return self.lista_generi
    def get_libri(self):
        return self._libro_dao.ottieni_libri()


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        biblioteca_dao= BibliotecaDAO()
        return biblioteca_dao.ottieni_biblioteca()





