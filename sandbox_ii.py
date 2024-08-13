#print("Starting to feel a bit more like me again which is nice")

arr_highlow = [1, 9, 3, 4, -5, 100]

for x in arr_highlow:
    for y in arr_highlow:
        print("Is {} bigger than {}".format(x, y))

        if x > y:
            print("Yes! {} is bigger than {}".format(x, y))
        else:
            print("Clearly not!")






