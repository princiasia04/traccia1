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

    def handlePaeseSelection(self, e):
        ##self.fillDDArtist() #questo dal paese dovra trovare gli album per ddalbum1 e 2
        pass

    def handleCammino(self, e):
        pass