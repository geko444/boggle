import string
import collections
import random

def makeDictionary():
    word_dict = collections.defaultdict(list)
    with open('words.txt') as f:
        for w in f.readlines():
            if len(w) > 3:
                word_dict[w[0]].append(w.strip())
    return word_dict

def makeGrid(size):
    letters = list(string.ascii_lowercase)
    return [[random.choice(letters) for i in range(size)] for j in range(size)]

def gridPrint(grid):
    grid_string = '\n'.join([''.join(row) for row in grid])
    print grid_string

def getLetter(grid, coordinate):
    return grid[coordinate[1]][coordinate[0]]

def getLetters(grid, coordinates):
    return [getLetter(grid, coordinate) for coordinate in coordinates]

def getWordFromPath(grid, coordinates):
    return ''.join(getLetters(grid, coordinates))

def getNeighbours(grid, coordinate, path=[]):
    size = len(grid)
    neighbours = []
    if coordinate not in path:
        path.append(coordinate)
    c, r = coordinate
    for j in range(r-1, r+2):
        if j in range(size):
            for i in range(c-1, c+2):
                if i in range(size):
                    if (i, j) not in path:
                        neighbours.append((i, j))
    return neighbours

def getWordsStartingWith(letters, dictionary):
    return [word for word in dictionary[letters[0]] if word.startswith(letters)]

def isWord(letters, dictionary):
    return letters in dictionary[letters[0]]

def isWordStart(letters, dictionary):
    if len(getWordsStartingWith(letters, dictionary)) == 0:
        return False
    else:
        return True

def findWords(grid, dictionary, start):
    path = [start]
    words = []
    max_length = len(grid) ** 2
    def takeStep(position):
        letters = getWordFromPath(grid, path)
        if isWord(letters, dictionary):
            words.append(letters)
            print letters
        if len(letters) < max_length and isWordStart(letters, dictionary) is True:
            neighbours = getNeighbours(grid, position, path)
            if len(neighbours) > 0:
                for n in neighbours:
                    path.append(n)
                    takeStep(n)
                    path.pop()

    takeStep(start)
    return words

def solveBoggle(grid, dictionary):
    words = []
    size = len(grid)
    for r in range(size):
        for c in range(size):
            words.extend(findWords(grid, dictionary, (c, r)))
    return words

test_grid = [['s', 't', 'n', 'g'], ['e', 'i', 'a', 'e'], ['d', 'r', 'l', 's'], ['s', 'e', 'p', 'o']]
grid2 = makeGrid(4)
gridPrint(grid2)
print '\n'
dictionary = makeDictionary()

print len(solveBoggle(grid2, dictionary))