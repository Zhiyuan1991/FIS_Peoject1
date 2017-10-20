# FIS_Peoject1
how to run the code:
python main.py [mazefile]
e.g. python main.py puzzle/puzzle1.txt

# puzzle 1
maze: 
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']

------- method 1: euclidean -------
solution found!
initial maze:
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']

step: 0
['1', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']
dice state:  { 1 2 3 0 0 }

step: 1
['S', '.', '.', '.', 'G']
['2', '.', '.', '.', '.']
dice state:  { 2 6 3 1 0 }

step: 2
['S', '.', '.', '.', 'G']
['.', '4', '.', '.', '.']
dice state:  { 4 6 2 1 1 }

step: 3
['S', '.', '.', '.', 'G']
['.', '.', '5', '.', '.']
dice state:  { 5 6 4 1 2 }

step: 4
['S', '.', '.', '.', 'G']
['.', '.', '.', '3', '.']
dice state:  { 3 6 5 1 3 }

step: 5
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '2']
dice state:  { 2 6 3 1 4 }

step: 6
['S', '.', '.', '.', '1']
['.', '.', '.', '.', '.']
dice state:  { 1 2 3 0 4 }

dice state description: {top,north,east,row,col}

nodes generated:  13
nodes visited:  9
steps:  6
------- method 1: ends -------

------- method 2: manhattan -------
solution found!
initial maze:
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']

step: 0
['1', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']
dice state:  { 1 2 3 0 0 }

step: 1
['S', '.', '.', '.', 'G']
['2', '.', '.', '.', '.']
dice state:  { 2 6 3 1 0 }

step: 2
['S', '.', '.', '.', 'G']
['.', '4', '.', '.', '.']
dice state:  { 4 6 2 1 1 }

step: 3
['S', '.', '.', '.', 'G']
['.', '.', '5', '.', '.']
dice state:  { 5 6 4 1 2 }

step: 4
['S', '.', '.', '.', 'G']
['.', '.', '.', '3', '.']
dice state:  { 3 6 5 1 3 }

step: 5
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '2']
dice state:  { 2 6 3 1 4 }

step: 6
['S', '.', '.', '.', '1']
['.', '.', '.', '.', '.']
dice state:  { 1 2 3 0 4 }

dice state description: {top,north,east,row,col}

nodes generated:  13
nodes visited:  9
steps:  6
------- method 2: ends -------

------- method 3: orientation_manhattan -------
solution found!
initial maze:
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']

step: 0
['1', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']
dice state:  { 1 2 3 0 0 }

step: 1
['S', '.', '.', '.', 'G']
['2', '.', '.', '.', '.']
dice state:  { 2 6 3 1 0 }

step: 2
['S', '.', '.', '.', 'G']
['.', '4', '.', '.', '.']
dice state:  { 4 6 2 1 1 }

step: 3
['S', '.', '.', '.', 'G']
['.', '.', '5', '.', '.']
dice state:  { 5 6 4 1 2 }

step: 4
['S', '.', '.', '.', 'G']
['.', '.', '.', '3', '.']
dice state:  { 3 6 5 1 3 }

step: 5
['S', '.', '.', '.', 'G']
['.', '.', '.', '.', '2']
dice state:  { 2 6 3 1 4 }

step: 6
['S', '.', '.', '.', '1']
['.', '.', '.', '.', '.']
dice state:  { 1 2 3 0 4 }

dice state description: {top,north,east,row,col}

nodes generated:  24
nodes visited:  17
steps:  6
------- method 3: ends -------