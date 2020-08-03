x_cache = {

}

y_cache = {

}

z_cache = {

}

xyz_cache = {

}


def expensive_seq(x, y, z):
    if f"{x},{y},{z}" in xyz_cache:
        return xyz_cache[f"{x},{y},{z}"]
    else:
        return_value = 0
        if x <= 0:
            return_value = y+z
            xyz_cache[f"{x},{y},{z}"] = return_value
            return return_value
        else:
            x_return = []
            y_return = []
            z_return = []

            if x in x_cache:
                x_return = x_cache[x]
            else:
                x_return = [x-1, x-2, x-3]
                x_cache[x] = x_return

            if y in y_cache:
                y_return = y_cache[y]
            else:
                y_return = [y+1, y+2, y+3]
                y_cache[y] = y_return

            if z in z_cache:
                z_return = z_cache[z]
            else:
                z_return = [z, z*2, z*3]
                z_cache[z] = z_return

            return_value = expensive_seq(x_return[0], y_return[0], z_return[0]) + expensive_seq(
                x_return[1], y_return[1], z_return[1]) + expensive_seq(x_return[2], y_return[2], z_return[2])

            xyz_cache[f"{x},{y},{z}"] = return_value

            return return_value


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        if x is None:
            print("ehm..")
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
