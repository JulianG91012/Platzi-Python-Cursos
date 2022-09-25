def contador_floats():
    x = 0.0
    for i in range(10):
        x += 0.1

    if x == 1.0:
        print(f'x = {x}')
    else:
        print(f'x != {x}')

def run():
    contador_floats()


if __name__ == "__main__":
    run()
