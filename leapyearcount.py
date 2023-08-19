count=0
for year in range(2023,2051):

    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year=",year)
            count=count+1
        else:
            pass
    elif year % 4 == 0:
        print("Leap year=",year)
        count = count + 1
    else:
        pass

print(count)


def calleapdays(y1,y2):
    count = 0
    for year in range(2023, 2051):

        if year % 100 == 0:
            if year % 400 == 0:
                #print("leap year=", year)
                count = count + 1
            else:
                pass
        elif year % 4 == 0:
            #print("Leap year=", year)
            count = count + 1
        else:
            pass

    return count


print(calleapdays(2023,2050))