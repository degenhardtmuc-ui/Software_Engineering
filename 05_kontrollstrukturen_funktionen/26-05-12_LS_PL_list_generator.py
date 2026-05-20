def main(winning_numebers=[]):

    if not winning_numbers: 

            winning_numbers = generate_random_numbers()

# Und hier noch einen List generator, da ich ihn schon 1-2 Mal sah:

list1 = [1, 2, 3, 4]

list2 = [3, 4, 5]

result = [x for x in list1 if x not in list2]