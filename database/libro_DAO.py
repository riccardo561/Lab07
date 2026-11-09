from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def ottieni_libri(self):
        self.libri = []
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor(dictionary=True)
        query = '''SELECT l.*
                   FROM libro l'''
        cursore.execute(query)
        for riga in cursore:
            libro = Libro(riga['id'], riga['titolo'], riga['autore'],riga['genere'],riga['anno_pubblicazione'],riga['id_biblioteca'])
            self.libri.append(libro)
        cursore.close()
        cnx.close()
        return self.libri
    def ottieni_libri_filtrati(self,biblioteca,genere):
        self.libri_filtrati = []
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor(dictionary=True)
        if genere=='Nessun filtro' and biblioteca=='Nessun filtro':
            query = '''SELECT DISTINCT l.*
                       FROM libro l,biblioteca b
                       WHERE l.id_biblioteca=b.id'''
            cursore.execute(query)
        elif biblioteca=='Nessun filtro' and genere!='Nessun filtro':
            query = '''SELECT DISTINCT l.*
                       FROM libro l,biblioteca b
                       WHERE l.genere=%s AND l.id_biblioteca=b.id'''
            cursore.execute(query,(genere,))
        elif genere=='Nessun filtro' and biblioteca!='Nessun filtro':
            query = '''SELECT DISTINCT l.*
                       FROM libro l,biblioteca b
                       WHERE l.id_biblioteca=b.id
                       AND b.nome=%s'''
            cursore.execute(query,(biblioteca,))
        else:
            query = '''SELECT DISTINCT l.*
                       FROM libro l,biblioteca b
                       WHERE l.genere=%s
                       AND l.id_biblioteca=b.id
                       AND b.nome=%s'''
            cursore.execute(query,(genere,biblioteca))
        for riga in cursore:
            libro = Libro(riga['id'], riga['titolo'], riga['autore'],riga['genere'],riga['anno_pubblicazione'],riga['id_biblioteca'])
            self.libri_filtrati.append(libro)
        cursore.close()
        cnx.close()
        return self.libri_filtrati
