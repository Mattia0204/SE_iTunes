import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._nodes = []
        self._edges = []

    def build_graph(self, durata_min):
        self.G.clear()
        self._nodes = []
        self._edges = []

        dict_album = DAO.get_all_album()
        dict_connessioni = DAO.get_connessioni()

        for codice, durata in dict_album.items():
            if durata >durata_min:
                self._nodes.append(codice)
                self.G.add_node(codice)

        for (a1, a2), c in dict_connessioni.items():
            if a1 in self._nodes and a2 in self._nodes:
                self.G.add_edge(a1, a2)


    def get_num_of_nodes(self):
        return self.G.number_of_nodes()

    def get_num_of_edges(self):
        return self.G.number_of_edges()

    def get_album(self):
        lista_album = []
        diz_album = DAO.get_album_attributes()
        for k, v in diz_album.items():
            if k in self._nodes:
                lista_album.append(v)

        return lista_album

    def get_component(self, album):
        """Restituisce la componente connessa di un album"""
        if album not in self.G:
            return []
        return list(nx.node_connected_component(self.G, album))
