############################################################################
##
##      name:           weighted_graph_walk.py
##      date:           june 2019
##      license:        GNU GPLv3.0
##      author:         matt crane
##      description:    weighted walk fns converted to class and methods
##                      for random weighted walks though graphs
##                      to be incorporated into music generation program
##                      (ChordScaleGraphGen)
##
############################################################################

from random import randrange

MelGraph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }
#             "7" : ["1", "3", "5", "6"]
                                        }
class Weighted_Walk(object):
        def __init__(self, Graph,node='1'):
                self.graph = Graph
                self.node = node
##                self.node = self.get_next_node(self.graph, self.node)
                self.weight_range = self.total_weights(self.graph, self.node)
                self.dice_roll = self.edge_weight_rand(self.graph, self.node)
                self.node = self.get_next_node(self.graph, self.node)
                
        def total_weights(self,graph, node):
            
                weight_total = 0
                for edge in graph[node]:
                      weight_total += graph[node][edge]  
                return weight_total

        def edge_weight_rand(self,graph, node):
            
                dice_roll = randrange(self.weight_range)
                return dice_roll

        def get_next_node(self,graph, node):

                run_total = 0
                dice_roll = 0
                dice_roll = self.edge_weight_rand(graph, node)
                print("diceroll = ",dice_roll, ", node is ", node, graph[node])
                while run_total < dice_roll:
                        for edge in graph[node]:
                                if run_total < dice_roll:
                                        run_total += graph[node][edge]
                                        print("runtotal is ", run_total)
                                        node = str(edge)
                print("returned node is ", node, ", edges ", graph[node])
                return node

                   
for i in range(7):
        testwalk = Weighted_Walk(MelGraph) 
        print(testwalk.node)
##        print(testwalk.__dict__)

