from random import randint

def picknumbers():
   
    #Generates a list of 6 unique random numbers between 1 and 59.
    
    numbers = []
    while len(numbers) < 6:
        pick = randint(1, 59)
        if pick not in numbers:
            numbers.append(pick)
    return sorted(numbers)

def newdraw():
   
    #Simulates a new lottery draw by generating 6 random numbers.
   
    result = []
    while len(result) < 6:
        ball = randint(1, 59)
        if ball not in result:
            result.append(ball)
    return sorted(result)

def checknumbers():
   
    #Continuously generates new draws until a winning ticket is found.
 
    drawcount = 0
    while newdraw() != picknumbers():
        drawcount += 1
        print(f"Draw {drawcount}: No Jackpot")
    print("Jackpot!")

if __name__ == "__main__":
    checknumbers()
