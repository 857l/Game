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


# def CreatingGame():


difficultyGame = GameDifficulty(4)
colorsGame = GameColors(5)

answer = SortGame(difficultyGame, colorsGame)

print(answer)

currentStep = GameDifficulty(4)


def GetStep(curStep):
    curStep[0], curStep[1], curStep[2], curStep[3] = map(int, input().split())
    return curStep


def EndGame():
    print("Yeah, you win!")


def ColorsHits(curStep, answer):
    countOfHits = 0
    for i in range(len(curStep)):
        for j in range(len(answer)):
            if curStep[i] == answer[j]:
                countOfHits += 1
    return countOfHits


def DoteHits(curStep, answer):
    countOfHits = 0
    for i in range(len(curStep)):
        if curStep[i] == answer[i]:
            countOfHits += 1
    return countOfHits


while currentStep != answer:
    currentStep = GetStep(currentStep)
    print(currentStep, ColorsHits(currentStep, answer), DoteHits(currentStep, answer))

EndGame()
