import random

def plant_tree(bauble_count: int, height: int) -> None:
    stalk = "[_]"
    bottom = "" if height <= 2 else "^" * int((height - 1)/2)
    bauble_running_count = 0
    for i in range(height):
        if i == 0 :
            space_created = int((height + 1)/2)
        else:
            space_created = int((height - i)/2)
        if i == 0:
            print(" " * space_created + "*")
        else:
            tree_width = i + 1 if int(i/2) == i/2 else i
            if bauble_running_count < bauble_count:
                fern_and_bauble = "".join(random.choices([".","o"], weights=[(height^2)/bauble_count,1], k=tree_width))
            else:
                fern_and_bauble = tree_width * "."
            bauble_running_count += (len(fern_and_bauble) - len(fern_and_bauble.strip("o")))
            print(" " * space_created + "/" + fern_and_bauble + "\\")
    print(bottom + stalk + bottom)

plant_tree(14, 7)
plant_tree(1, 3)
plant_tree(6, 5)
plant_tree(24, 10)
plant_tree(11, 6)
plant_tree(38, 15)
plant_tree(2, 4)
plant_tree(28, 9)