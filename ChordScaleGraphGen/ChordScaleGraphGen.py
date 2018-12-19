######################################################################################################
# ChordScaleGraphGen.py
#
# Author:  Matt Crane
# Date:    19/12/2018
# Licence: GNU GPLv3.0
#
# Description:
#   Uses ChordScale to generate classes of chord scales
#   Graph/networks then defined
#   These graphs then used to generate random sequence of midi chords, bass note,
#   and melody with changing key
#   Graph dictionaries can be edited to shape sequence generation (the main point)
#
# NB: Many issues/to dos eg only plays at 60bpm(really 30bpm since unit is 1/8th note),
#     chd needs to be changed when melnote played in different key,
#     intkey to be included, noteoffs, proper pacakaging etc
#     An initial proof of concept and learning project
#     
########################################################################################################


class ChordScale:    

  def __init__(self, intkey, rt):
    self.intkey = intkey
    self.rt = rt
    self.mididiff = midi_diff(self.intkey)
    self.midinum =  list(map(lambda x: x+self.rt, self.mididiff))
    self.midinumdbl =  self.midinum + (list(map(lambda x: x+12, self.midinum)))
    self.chds = chd_gen(self.midinumdbl)
    self.oneoctscale = one_oct(self.midinum)

def midi_diff(intkey):
     
    mididiff = []
    for n in range(len(intkey)):
      if n == 0 :
        mididiff.append(intkey[0])
      else:
        mididiff.append(mididiff[n-1]+ intkey[n])
    mididiff.insert(0,0)

    return(mididiff)


def one_oct(scale):
  oneoct_scale = []
  for i in scale:
    oneoct_scale.append(60+(i%12))
  
  return(sorted(oneoct_scale))

def chd_gen(scale):
  chds = []
  for i in range(len(scale)-7):
    chds.append(one_oct(list(scale[i:i+5:2])))
  
  return(chds)




ChdGraph = { "1" : ["1", "3", "4"],
             "2" : ["2", "3", "5"],
             "3" : [ "1", "2", "4", "5"],
             "4" : ["3", "2", ],
             "5" : ["3", "2", "1", "6"],
             "6" : ["4", "5", "3", ]
#             "7" : ["1", "3", "5", "6"]
                                        }

MelGraph = { "1" : ["1", "3", "2" ],
             "2" : ["2", "3", "1" ],
             "3" : ["3", "1", "2" ],
             "4" : ["3", "2", "4" ],
             "5" : ["3", "2", "1", "6"],
             "6" : ["4", "5", "3", ]
#             "7" : ["1", "3", "5", "6"]
                                        }

MelTmeGph = { "1" : ["1", "3", "2" ],
              "2" : ["1", "2", "3" ],
              "3" : ["1", "3", "1", "2"]
#              "4" : ["1", "3", "2", "4"],
#              "5" : ["3", "2", "1", "6"],
#              "6" : ["4", "5", "3", "7"],
#              "7" : ["1", "3", "5", "6"]
                                        }

ChdTmeGph = { "2" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "3" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "4" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "5" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "6" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "7" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "8" : ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "14": ["2", "3", "4", "5", "6", "7", "8", "14", "16"],
              "16": ["2", "3", "4", "5", "6", "7", "8", "14", "16"]
                                                                    }

RtTmeGph = { "3" : ["3", "4", "5", "6", "7", "8", "14", "16"],
             "4" : ["3", "4", "5", "6", "7", "8", "14", "16"],
             "5" : ["3", "4", "5", "6", "7", "8", "14", "16"],
             "6" : ["3", "4", "5", "6", "7", "8", "14", "16"],
             "7" : ["3", "4", "5", "6", "7", "8", "14", "16"],
             "8" : ["3", "4", "5", "6", "7", "8", "14", "16"],
             "14": ["3", "4", "5", "6", "7", "8", "14", "16"],
             "16": ["3", "4", "5", "6", "7", "8", "14", "16"]
                                                              }

RtGph = {    "1" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "2" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "3" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "4" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "5" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "6" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "7" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "8" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "9" : ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "10": ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "11": ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"],
             "12": ["1", "2", "3", "4", "5", "6", "7", "8", "9",  "10", "11", "12"]
                                                                                    }

import random

def walkstep(graph, currentnode):
  currentnode = (random.choice(graph[currentnode]))

  return(currentnode)

gphrt = "3"
rt = (59 + (int(gphrt)))
meldeg = "4"
chddeg = "6"
chdtimestep = "2"
intkey = [2,2,1,2,2,2]
meltimestep = "1"
rtimestep = "4"
CTsum = 0
MTsum = 0
RtTsum = 0

from tkinter import *
import pygame.midi

root = Tk()

pygame.midi.init()

print (pygame.midi.get_device_info(1))
player = pygame.midi.Output(1)
player.set_instrument(4)

T = ((pygame.midi.time())//1000)
#MT = ((pygame.midi.time())//1000)
#RtT = ((pygame.midi.time())//1000)


while pygame.midi.time() < 1024000:
    
  Scale = ChordScale(intkey, rt)
  T = ((pygame.midi.time())//1000)

  if T == (CTsum):
      
    chdtimestep =(walkstep(ChdTmeGph, chdtimestep))
    print("chdtimestep: " + (chdtimestep))
    print("ChdTmeGph: " + (str((ChdTmeGph[chdtimestep]))))

    
    print("chddeg: " + chddeg)
    print("ChdGraph: " + (str(ChdGraph[chddeg])))
    chddeg = (walkstep(ChdGraph, chddeg))

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

    meltimestep = (walkstep(MelTmeGph, meltimestep))
    meldeg = (walkstep(MelGraph, meldeg))
    melnote = ()
    melnote = (Scale.oneoctscale[int(meldeg)])
    player.note_on(melnote, velocity=127, channel=0)
    print(melnote)
    
    print("MTsum: " + (str(MTsum)))
    print("melnote: " + (str(melnote)))
    MTsum = (MTsum +(int(meltimestep)))

  elif T == (RtTsum):
    
    rtimestep = (walkstep(RtTmeGph, rtimestep))
    gphrt = (walkstep(RtGph, gphrt))
    rt = (int(gphrt))
   
    RtTsum = (RtTsum + (int(rtimestep)))

    print("scale: " + (str(Scale.oneoctscale)))
    print("RtTsum: " + (str(RtTsum)))
    
  
root.mainloop()

      
    
