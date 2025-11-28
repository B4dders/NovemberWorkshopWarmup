import random
import json
from pathlib import Path

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

def book_in_elves(igloo_locations_list: Path, families_list: Path):
    with igloo_locations_list.open() as f:
        igloo_locations = json.load(f)
    with families_list.open() as f:
        families = json.load(f)

    sorted_igloos = sorted(igloo_locations, key=lambda x: x["capacity"], reverse=True)
    sorted_families = sorted(families, key=lambda x: x["count"], reverse=True)

    no_pet_igloos = [igloo for igloo in sorted_igloos if igloo["pet_friendly"] == False]
    no_pet_families = [family for family in sorted_families if family["pets"] == 0]
    pet_families = [family for family in sorted_families if family["pets"] != 0]
    pet_igloos =  [igloo for igloo in sorted_igloos if igloo["pet_friendly"] == True]

    pairings = {}

    def pair_families_with_igloos(families, igloos, pairings):
        for family in families:
            for igloo in igloos:
                if family["count"] <= igloo["capacity"]:
                    pairings[f"{igloo["site_name"]}.{igloo["igloo_number"]}"] = family["family_name"]
                    igloos.remove(igloo)
                    break
        return pairings, igloos

    pairings, leftover_igloos = pair_families_with_igloos(no_pet_families, no_pet_igloos, pairings)
    pairings, pet_leftover_igloos = pair_families_with_igloos(pet_families, pet_igloos, pairings)

    leftover_families = [family for family in sorted_families if family["family_name"] not in pairings.values()]
    pairings, leftover_igloos = pair_families_with_igloos(leftover_families, leftover_igloos + pet_leftover_igloos, pairings)
    families_housed = f"{len(pairings)} families housed"
    leftover_families = [family for family in sorted_families if family["family_name"] not in pairings.values()]
    unhoused_families = list([family["family_name"] for family in leftover_families])
    return print(families_housed, unhoused_families)

DATA_PATH = Path(__file__).parent.parent / "Data"
book_in_elves(DATA_PATH / "igloo_locations.json", DATA_PATH / "elf_families.json")