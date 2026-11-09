from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def ottieni_biblioteca(self):
        self.biblioteche=[]
        cnx=DBConnect.get_connection()
        cursore=cnx.cursor(dictionary=True)
        query='''SELECT b.*
                 FROM biblioteca b'''
        cursore.execute(query)
        for riga in cursore:
            biblioteca=Biblioteca(riga['id'],riga['nome'],riga['indirizzo'])
            self.biblioteche.append(biblioteca)
        cnx.close()
        cursore.close()
        return self.biblioteche





