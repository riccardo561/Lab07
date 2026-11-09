import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd.value=''
        self._view.dd1.value=''
        self.biblioteche=self._model.get_biblioteche()
        for biblioteca in self.biblioteche:
            self._view.dd.options.append(ft.DropdownOption(key=f'{biblioteca.nome}',text=f'{biblioteca.nome}'))
        self._view.update()
        self._view.dd.options.append(ft.DropdownOption(key='Nessun filtro',text='Nessun filtro'))
        self.generi=self._model.get_generi()
        for generi in self.generi:
            self._view.dd1.options.append(ft.DropdownOption(key=f'{generi}', text=f'{generi}'))
        self._view.dd1.options.append(ft.DropdownOption(key='Nessun filtro',text='Nessun filtro'))
        self._view.dd.value = 'Nessun filtro'
        self._view.dd1.value = 'Nessun filtro' #Queste due operazioni sono state messe dal momento in cui inserendo un on_select
                                            # l'alert si avviava ancor prima di finire di compilare tutti i campi perché risultavano vuoti o None
        self._view.update()

    # CALLBACKS DROPDOWN
    def seleziona_filtro(self,e):
        self.mostra_libri(e)


    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self,e):
        self._view.mylistview_filtro.controls.clear()
        self.lista_libri_filtrati=[]
        if (self._view.dd.value is None or self._view.dd.value=='') or (self._view.dd1.value is None or self._view.dd1.value==''):
            self._view.show_alert('Devi inserire un valore valido per i campi corrispondenti, se non desideri filtri, prego selezionare nessun filtro')
        else:
            self.lista_libri_filtrati=self._model.get_libri_filtrati(self._view.dd.value,self._view.dd1.value)
            if self.lista_libri_filtrati == []:
                    self._view.show_alert('Putroppo non ci sono corrispondenze tra il libro e la biblioteca')
            else:
                for libri_filtrati in self.lista_libri_filtrati:
                    self._view.mylistview_filtro.controls.append(ft.Text(f'{libri_filtrati.titolo},{libri_filtrati.autore},{libri_filtrati.genere},{libri_filtrati.anno_pubblicazione}'))
        self._view.update()
