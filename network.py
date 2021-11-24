from node import Node


class Network:
    def __init__(self):
        self.nodes = {}  # 存 id 索引节点
        self.now_pt = None  # 当前节点指针

    def build_network(self):
        pass

    def remove_node(self, *args, ** kwargs):
        pass

    def print_network(self):
        if self.now_pt is None:
            print("select current pointer...")
            return

        tmp = self.now_pt
        while tmp.next_node != self.now_pt:
            print(tmp.id, end=" -> ")
            tmp = tmp.next_node
        print(tmp.id, end=" -> ")
        print(self.now_pt.id)


class SimplexNetwork(Network):

    def build_network(self):
        for i in range(1, len(self.nodes)):
            self.nodes[i - 1].next_node = self.nodes[i]
        self.nodes[-1].next_node = self.nodes[0]

    def remove_node(self, father_node):
        node_to_remove = father_node.next_node
        father_node.next_node = node_to_remove.next_node
        self.nodes.pop(node_to_remove.id)


class DuplexNetwork(Network):

    def remove_node(self,):
        pass

