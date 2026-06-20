import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDPaese(self):
        #chiamo funzione nel model
        paese = self._model.getPaese()
        paeseDD = list(map(lambda x: ft.dropdown.Option(x), paese))
        self._view._ddPaese.options = paeseDD
        self._view.update_page()

    def handleCreaGrafo(self, e):
        if self._view._ddPaese.value is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un paese dal menu", color="red"))
        self._model.creaGrafo(self._view._ddPaese.value)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente!", color="green"))
        self._view.txt_result.controls.append(ft.Text(f"Per il paese {self._view._ddPaese.value} ci sono {len(self._model._grafo.nodes)} nodi e {len(self._model._grafo.edges)} archi", color="green"))
        primi5 = self._model.getPrimi5()
        self._view.txt_result.controls.append(ft.Text("I primi 5 archi con peso peso maggiore sono:", color="green"))
        for u, v, data in primi5:
            self._view.txt_result.controls.append(ft.Text(f"{u}, {v}, {data['weight']}", color="green"))
        self._view.update_page()

    def handleAlbumSelection(self, e):
        paese_selezionato = self._view._ddPaese.value
        listaAlbum = self._model.getListaAlbum(paese_selezionato)
        self.fillDDAlbum(listaAlbum) #questo dal paese dovra trovare gli album per ddalbum1 e 2

    def fillDDAlbum(self, listaAlbum):
        listaAlbumDD = list(map(lambda x: ft.dropdown.Option(x), listaAlbum))
        self._view._ddAlbum1.options = listaAlbumDD
        self._view._ddAlbum2.options = listaAlbumDD
        self._view.update_page()

    def handleCammino(self, e):
        NPartenza = self._view._ddAlbum1.value
        NArrivo = self._view._ddAlbum2.value
        cammino = self._model.getCammino(NPartenza, NArrivo)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Cammino creato correttamente!", color="green"))
        self._view.txt_result.controls.append(ft.Text(f"{cammino}", color="green"))
        self._view.update_page()