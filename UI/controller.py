import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        try:
            durata_min = float(self._view.txt_durata.value)
        except ValueError:
            self._view.show_alert("Inserire un numero valido per la durata")
            return
        print("Inizio creazione grafo...")
        self._model.build_graph(durata_min)
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(
            f"Grafo creato: {self._model.get_num_of_nodes()} Album, {self._model.get_num_of_edges()} Archi"))

        album_filtrati = self._model.get_album()  # Metodo nel model
        self._view.dd_album.options.clear()
        for a in album_filtrati:
            self._view.dd_album.options.append(ft.dropdown.Option(a))

        self._view.update()

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        self._view.lista_visualizzazione_2.controls.append(ft.Text(
            f"Dimensione componente: {self._model.get_component(self._view.dd_album.value)}"))
        """self._view.lista_visualizzazione_2.controls.append(ft.Text(
            f"Durata totale: {self._model.calcolo_drata_totale()} minuti"))"""


    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO