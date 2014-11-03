class DirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self.nodes:
            self.nodes[node_a] = [node_b]
        else:
            self.nodes[node_a].append(node_b)

        if node_b not in self.nodes:
            self.nodes[node_b] = []

    def get_neighbours(self, node):
        return self.nodes[node]

    def path_between(self, node_a, node_b):
        if node_a not in self.nodes or node_b not in self.nodes:
            return False
        elif node_b in self.get_neighbours(node_a):
            return True

        else:
            for node in self.nodes[node_a]:
                if node_b in self.get_neighbours(node):
                    return True
                else:
                    return self.path_between(node, node_b)
        return False

    def __str__(self):
        result = ''
        for node in self.nodes:
            res = node + "--->"
            for a in self.nodes[node]:
                res += "{} ".format(a)
            result += "{}\n".format(res)

        return result
