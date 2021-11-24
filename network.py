from node import Node


class Network:
    def __init__(self):
        self.nodes = {}  # 存 id 索引节点
        self.now_pt = None  # 当前节点指针

    def build_network(self):
        pass

    def remove_node(self, *args, ** kwargs):
        pass

    def initialize_failure(self, fail_rate, neighbour_fail_rate):
        from random import random

        network_size = len(self.nodes)
        for i in range(1, network_size):
            self.nodes[i].is_disabled = random() < fail_rate

        # self.print_network(print_disable=True)

        for i in range(1, network_size):
            if self.nodes[i-1].is_disabled and self.nodes[(i+1) % network_size]:
                self.nodes[i].is_disabled = self.nodes[i].is_disabled or random() < neighbour_fail_rate

        # 特殊处理首节点
        if not self.nodes[0].is_disabled and (self.nodes[-1].is_disabled or self.nodes[1].is_disabled):
            self.nodes[0].is_disabled = random() < neighbour_fail_rate

        # self.print_network(print_disable=True)

    def print_network(self, print_disable=False):
        if self.now_pt is None:
            print("select current pointer...")
            return

        tmp = self.now_pt
        while tmp.next_node != self.now_pt:
            if print_disable:
                print('X' if tmp.is_disabled else '', end= "")
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


