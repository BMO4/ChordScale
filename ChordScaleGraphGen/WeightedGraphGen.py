################################################################################################################################
##
##  name:           WeightedGraphGen.py
##  author:         Matt Crane
##  date:           june 2019
##  description:    Weighted Walk class added to ChordScaleGraphGen
##                  for testing pre converting sections to individual modules
##                  and other features developed
##  license:        GNU GPLv3
##  
##
##
##############################################################################################

class ChordScale:    

    def __init__(self, intkey, rt):
        self.intkey = intkey
        self.rt = (rt)
        self.mididiff = self.midi_diff(self.intkey)
        self.midinum =  list(map(lambda x: x+int(self.rt), self.mididiff))
        self.midinumdbl =  self.midinum + (list(map(lambda x: x+12, self.midinum)))
        self.chds = (self.chd_gen(self.midinumdbl))
        self.oneoctscale = one_oct(self.midinum)

    def midi_diff(self,intkey):
       
        mididiff = []
        for n in range(len(intkey)):
            if n == 0 :
                mididiff.append(intkey[0])
            else:
                mididiff.append(mididiff[n-1]+ intkey[n])
        mididiff.insert(0,0)

        return(mididiff)

    def chd_gen(self,scale):
        chds = []
        for i in range(len(scale)-7):
            chds.append(one_oct(list(scale[i:i+5:2])))
              
        return(chds)
      
def one_oct(scale):
      oneoct_scale = []
      for i in scale:
          oneoct_scale.append(60+(i%12))
      
      return(sorted(oneoct_scale))
      
testCS = ChordScale([2,2,1,2,2,2,1],60)
print(testCS.__dict__)
for i in testCS.mididiff:
    print(testCS.rt + i)


ChdGraph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }
#             "7" : ["1", "3", "5", "6"]
                                        }

MelGraph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }
#             "7" : ["1", "3", "5", "6"]
                                        }

MelTmeGph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }
                                        }

ChdTmeGph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }

                                        }

RtTmeGph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }

                                        }

RtGph = { "1" : {"1": 2, "3" : 3, "2":5, "5":4, "6":3 },
             "2" : {"2": 1, "3":  2, "1":3, "5": 4 },
             "3" : {"3":1, "1":2, "2":3 },
             "4" : {"3": 2, "2": 3, "4": 4, "5": 5, "6": 6},
             "5" : {"3": 1, "2":2, "1":3, "6":4, "5":5},
             "6" : {"4":1, "5":2, "3":3, "6":4 }
#             "7" : ["1", "3", "5", "6"]
                                        }

import random

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
        self.weight_range = int(self.total_weights(self.graph, self.node))
        self.dice_roll = int(self.edge_weight_rand(self.graph, self.node))
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
                    run_total += int(graph[node][edge])
                    print("runtotal is ", run_total)
                    node = str(edge)
        print("returned node is ", node, ", edges ", graph[node])
        return node

from tkinter import *
import pygame.midi
from random import *

root = Tk()

gphrt = "1"
rt = 59 + int(gphrt)
meldeg = "1"
chddeg = "1"
chdtimestep = "2"
intkey = [2,2,1,2,2,2]
meltimestep = "1"
rtimestep = "1"
CTsum = 0
MTsum = 0
RtTsum = 0

pygame.midi.init()

print (pygame.midi.get_device_info(1))
player = pygame.midi.Output(3)
player.set_instrument(4)

while pygame.midi.time() < 1024000:
    
    Scale = ChordScale(intkey, gphrt)
    T = ((pygame.midi.time())//1000)

    if T == (CTsum):
      
        chdtimeobj =(Weighted_Walk(ChdTmeGph, chdtimestep))
        chdtimestep = chdtimeobj.node

        chddegobj = (Weighted_Walk(ChdGraph, chddeg))
        chdeg = chddegobj.node
        
        print("chdtimestep: " + str(chdtimestep))
        print("ChdTmeGph: " + (str((ChdTmeGph[chdtimestep]))))
        print("chddeg: " + str(chddeg))
        print("ChdGraph: " + (str(ChdGraph[chddeg])))

        chd = []
        chd = (Scale.chds[int(chddeg)])
        print("chd: " + (str(chd)))
    
        for i in chd:
            player.note_on(i, velocity=95, channel=0)
        player.note_on(((chd[0])-24), velocity=80, channel=0)
        print("bs note: " + (str((chd[0])-24)))

        CTsum = (CTsum + (int(chdtimestep)))
        
        print("CTsum: " + (str(CTsum)))

    elif T == (MTsum):

        meltimeobj = (Weighted_Walk(MelTmeGph, meltimestep))
        meltimestep = meltimeobj.node
        meldegobj = (Weighted_Walk(MelGraph, meldeg))
        meldeg = (meltimeobj.node)
        melnote = int(Scale.oneoctscale[int(meldeg)])
        player.note_on(melnote, velocity=127, channel=0)
        print(melnote)
        
        print("MTsum: " + (str(MTsum)))
        print("melnote: " + (str(melnote)))
        MTsum = (MTsum +(int(meltimestep)))

    elif T == (RtTsum):
    
        rtimeobj = (Weighted_Walk(RtTmeGph, rtimestep))
        rtimestep = rtimeobj.node
        rtobj = (Weighted_Walk(RtGph, gphrt))
        gphrt = rtobj.node
        Scale.rt = 59 + int(gphrt)

        RtTsum = (RtTsum + (int(rtimestep)))

        print("scale: " + (str(Scale.oneoctscale)))
        print("RtTsum: " + (str(RtTsum)))
        
root.mainloop()
