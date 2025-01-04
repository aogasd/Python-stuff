def main():
     die = int(input("Size of dice? "))
     count = int(input("How many? "))
     # values:list= dice_generator(die,count)
     # dice_summer(values,count)
     # two_dice(die)
     how_many_of_each_result(die,count)

def dice_generator(die:int,count:int):
     output = []
     for d in range(die):
         output.append(d+1)
    #  for i in range(count):
    #       output.append([])
    #       for j in range(die):
    #         output[i].append(j+1)
    # print(output)
     return output
def dice_summer(dice_values:list,count):
    # was gonna try to just generate table of values that appear but this will be mega inefficient
    # it's nth dimensional matrix math but everything moves in increments of 1, I'm sure there's a math shortcut here
    # could probably find a guide online but that's not fun is it
    output = []
    for i in range(count):
        output.append([])
        for j in range(i+1):
            output[i].append([])
            for d in range(dice_values.__len__()):
                output[i][j].append(d+i+j+3)
            
        print(output[i])
    print(output)

def two_dice(die:int):
    # THE  only one that actually made sense
    output = []
    for i in range(die):  
        output.append([])
        for j in range(die):
            output[i].append(i+j+2)    
        print(output[i])

def how_many_of_each_result(die:int,count:int):
    # goal: calculate or tally how many instances of each result of the dice roll can happen
    # i.e. rolling 4d10 gives '20' in 633/10000 rolls
    # I dunno how to math this
    #staring at an excel doc for a couple hours for fun
    value_start = count
    value_end = die*count
    for i in range(value_end-value_start+1):
        print(f"{value_start+i}: {i+1}th value ")
        value_repeats:int = 1
        for j in range(i+1):
            value_repeats += j*count


if __name__ == "__main__":
     main()