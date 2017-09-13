def pretty_print_record(**kwargs):   # във функцията kwargs ще бъде обикновен dict
    print(kwargs.pop('name', "Record"), ":")
    for k, v in kwargs.items():
        print("\t", k, "= ", v)

pretty_print_record(name="Venus", distance_au=0.723, diameter_km=12104)