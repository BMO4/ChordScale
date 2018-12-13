**ChordScalePlay.py**
* python program for music creation 
* facillitate a user unaware of music theory to make music of coherent harmonic complexity
* generates ChordScales as class ojects (families of scales and chords) 
* chords and scales (attributes) confined to one octave to facillitate voice leading, minimal large intervallic leaps
* maps these dynamically to qwerty keyboard
* [a-g,z-n] select key/root note (ie c,c#,d,d# -> b)
* [1-7] play chords of that key from degree 1-7 (one octave, various inversions, plus bass note)
* [r-p] play melodic scale note (one octave)
* Intkey defines intervallic structure of scale (eg T=2 semitones, S=1 semitone, major scale=[T,T,S,T,T,T]=[2,2,1,2,2,2])
* proof of concept in python, limitation of latency won't be overcome until implemented in compiled language eg C
* required packages/modules pygame, pygame.midi, [t|T]kinter
* NB: click in widget to focus/get started!
