def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"Firstname":"Facundo", "Lastname": "García"}

    super_list = [
        {"Firstname":"Facundo","Lastname":"García"},
        {"Firstname":"Julian", "Lastname": "Gómez"},
        {"Firstname":"Johana","Lastname":"Patricia"},
        {"Firstname":"Sofia","Lastname":"Gómez"},
    ]

    super_dict = {
        "Natural nums": [1,2,3,4,5],
        "Integer nums": [-1,-2,0,1,2],
        "Floating nums": [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == "__main__":
    run()
