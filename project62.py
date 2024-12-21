def cubic_permutations(nb_perm):
    i = 1
    cube_perm_dict = dict()
    while True:
        cube_str = str(i ** 3)
        cube_str_sorted_digit = ''.join(sorted(cube_str))
        if cube_perm_dict.get(cube_str_sorted_digit):
            cube_perm_dict[cube_str_sorted_digit].append(i)
            if len(cube_perm_dict[cube_str_sorted_digit]) >= nb_perm:
                return min(cube_perm_dict[cube_str_sorted_digit]) ** 3
        else:
            cube_perm_dict[cube_str_sorted_digit] = [ i ]
        i += 1

print(cubic_permutations(5))
