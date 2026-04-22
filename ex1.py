from dice import RandomDice

def testroll(d:RandomDice, roll_times: int):
    print("*"*30)
    print("Roll times:",roll_times)
    rolls = dice.Roll(roll_times)  
    stats = {1:0,2:0,3:0,4:0,5:0,6:0}
    totalroll = 0
    for i in rolls:
        stats[i] += 1
        totalroll += 1
    print("-"*30)
    print("totalroll:",totalroll)
    print(stats)

    print("-"*30)

    for i in stats:
        print("probability:", i, stats[i]/roll_times)
    print("*"*30)

p = 1/6
# Example usage:
dice = RandomDice([p, p, p, p, p, p]) 

testroll(dice,1)

testroll(dice,10)

testroll(dice,10000000)