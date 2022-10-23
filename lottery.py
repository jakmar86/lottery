from random import randint

def picknumbers():
    numbers = []
    while len(numbers) < 6:
        pick = randint(1,59)
        if pick not in numbers:
            numbers.append(pick)
    return sorted(numbers)


def newdraw():
    result = []
    while len(result) < 6:
        ball = randint(1,59)
        if ball not in result:
            result.append(ball)
    return sorted(result)
        
def checknumbers():
    drawcount = 0
    while newdraw() != picknumbers():
        drawcount += 1
        print(drawcount)
        print("No Jakpot")
    print("Jackpot")
    
if __name__ == __main__:
    checknumbers()