import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._migliorCammino = []

    def getPaese (self):
        return DAO.getPaese()

    def creaGrafo (self, paese):
        album = DAO.getAlbum(paese)
        self._grafo.add_nodes_from(album)
        album_clienti = {}
        for a in album:
            listaClienti = DAO.getClienti(a, paese)
            album_clienti[a] = listaClienti

        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                if u != v:
                    clientiU = album_clienti[u]
                    clientiV = album_clienti[v]
                    if set(clientiU) & set(clientiV):
                        numTracceU = DAO.getNumeroTracce(u)
                        numTracceV = DAO.getNumeroTracce(v)
                        self._grafo.add_edge(v, u, weight=numTracceU[0]+numTracceV[0])

    def getPrimi5(self):
        Primi5 = sorted(
            self._grafo.edges(data=True),
            key=lambda x: x[2].get("weight", 0),
            reverse=True
        )[:5]
        return Primi5

    def getListaAlbum(self, paese):
        return DAO.getAlbum(paese)

    def getCammino(self, NPartenza, NArrivo):
        cammino = nx.dijkstra_path(self._grafo, NPartenza, NArrivo, weight="weight")
        return cammino