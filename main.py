"""
    一个环形结构内有1000个工作节点，头尾相连形成一个单向的环形监控结构，正常工作的节点只能监控与它相连的下一个节点的宕机情况，宕机节点无法监控与它
相连的下一个节点的宕机情况。当宕机节点被发现时，会被移出环形结构，剩下的节点会重新组成新的环形监控网络。假设环形结构内的宕机事件为同时发生，汇报事件
也是同时发生，环形结构每重组一次记为一个时间周期（每次重组能移除多个宕机节点），环形结构内的节点宕机率为百分之8。节点间连续宕机的概率为百分之20。
1.求平均每个时间周期内宕机状况的汇报次数。
2.当每个节点之间为双向监督时，平均每个时间周期内宕机状况的汇报次数。
"""
from network import *
from node import *

SINGLE_FAIL_RATE = 0.08
NEIGHBOUR_FAIL_RATE = 0.08 * 0.2

if __name__ == '__main__':
    Node0 = Node(0)
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    network = SimplexNetwork()
    network.nodes = [Node0, Node1, Node2, Node3]
    network.build_network()

    network.now_pt = Node1
    network.print_network()
    network.remove_node(Node1)  # 1 上报 2 错误； 移除 2。
    network.print_network()
