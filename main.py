import random

def GameDifficulty(difficulty):
    arr = [0] * difficulty
    return arr

def GameColors(colors):
    arr = [0] * colors
    return arr

def SortGame(difficulty, colors):
    difficulty[0] = random.randint(0, len(colors) - 1)
    colors[difficulty[0]] = 1

    for i in range(1, len(difficulty)):
        newColor = CreateNewColor(colors)
        while colors[newColor] == 1:
            newColor = CreateNewColor(colors)
        colors[newColor] = 1
        difficulty[i] = newColor
    return difficulty

def CreateNewColor(colors):
    newColor = random.randint(0, len(colors) - 1)
    return newColor

#def CreatingGame():


difficultyGame = GameDifficulty(4)
colorsGame = GameColors(5)

print(SortGame(difficultyGame, colorsGame))
