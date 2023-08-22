from pprint import pprint

paths = [
    {
        "carId": 'car1',
        "selected": 'first',
        "i": 0,
        "first": [
            [8, 17],
            [8, 16],
            [8, 15],
            [8, 14],
            [7, 14],
            [6, 14],
            [6, 13],
            [6, 12],
            [6, 11],
            [6, 10],
            [6, 9],
            [6, 8],
            [6, 7],
            [6, 6],
            [7, 6],
            [8, 6],
            [9, 6],
            [10, 6],
            [11, 6],
            [12, 6],
            [12, 7],
            [12, 8],
            [12, 9],
            [12, 10],
            [12, 11],
            [12, 12],
            [12, 13],
            [12, 14],
            [13, 14],
            [14, 14],
            [15, 14],
            [16, 14],
            [16, 13],
            [16, 12],
        ],
        "second": [
            [16, 12],
            [16, 11],
            [17, 11],
            [18, 11],
            [19, 11],
            [20, 11],
            [21, 11],
            [22, 11],
            [23, 11],
            [24, 11],
            [25, 11],
            [26, 11],
            [26, 12],
            [26, 13],
            [26, 14],
            [26, 15],
            [26, 16],
            [26, 17],
            [26, 18],
            [26, 19],
            [26, 20],
            [26, 21],
            [26, 22],
            [25, 22],
            [24, 22],
            [23, 22],
            [22, 22],
            [21, 22],
            [20, 22],
            [20, 23],
            [20, 24],
            [19, 24],
            [18, 24],
            [17, 24],
            [16, 24],
            [15, 24],
            [14, 24],
            [13, 24],
            [12, 24],
            [11, 24],
            [10, 24],
            [9, 24],
            [8, 24],
            [8, 23],
            [8, 22],
            [8, 21],
            [8, 20],
            [8, 19],
            [8, 18],
            [8, 17],
        ]
    },
    {
        "carId": 'car2',
        "selected": 'first',
        "i": 0,
        "first": [[32, 31], [33, 31], [34, 31], [35, 31], [36, 31], [37, 31], [38, 31], [39, 31], [39, 32], [39, 33],
                  [39, 34], [39, 35], [40, 35], [41, 35], [42, 35], [43, 35], [44, 35], [44, 36], [44, 37], [44, 38],
                  [44, 39], [44, 40], [44, 41], [44, 42], [43, 42], [42, 42], [41, 42], [40, 42], [39, 42], [38, 42],
                  [37, 42], [36, 42], [35, 42], [34, 42], [33, 42], [33, 41], [33, 40], [33, 39], [32, 39], [31, 39],
                  [31, 38], [30, 38], [29, 38], [28, 38]],
        "second": [[28, 38], [27, 38], [26, 38], [25, 38], [25, 39], [24, 39], [23, 39], [22, 39], [21, 39], [20, 39],
                   [20, 38], [20, 37], [20, 36], [20, 35], [20, 34], [20, 33], [20, 32], [20, 31], [21, 31], [22, 31],
                   [23, 31], [24, 31], [25, 31], [26, 31], [27, 31], [28, 31], [29, 31], [30, 31], [31, 31], [32, 31]],
    },
    {
        "carId": 'car3',
        "i": 0,
        "selected": 'first',
        "first": [[9, 38], [8, 38], [8, 37], [8, 36], [8, 35], [8, 34], [8, 33], [8, 32], [8, 31], [8, 30], [8, 29],
                  [8, 28], [8, 27], [8, 26], [9, 26], [10, 26], [11, 26], [12, 26], [13, 26], [14, 26], [15, 26],
                  [16, 26], [16, 27], [16, 28], [16, 29], [16, 30], [16, 31]],
        "second": [[16, 31], [16, 32], [16, 33], [16, 34], [16, 35], [16, 36], [16, 37], [16, 38], [16, 39], [16, 40],
                   [15, 40], [14, 40], [13, 40], [12, 40], [11, 40], [10, 40], [9, 40], [9, 39], [9, 38]],
    },
]

driver = [
    {'driverId': 'd0c600a2-298c-44dc-b9d7-85f790703959', 'name': 'Steven'},
    {'driverId': '1cfa84fc-1991-4a5d-8e66-ff067876ca57', 'name': 'Frank'},
    {'driverId': '768e9685-01f6-4a64-a718-68373ca2f9d0', 'name': 'William'},
]

customers = [
    {'customerId': 'a033590f-daf2-408c-a07f-fdd37a8a6a13', 'name': 'Alice'},
    {'customerId': '454652dc-e13a-480e-a505-ebe8758b5c86', 'name': 'Michael'},
    {'customerId': 'd90ebf24-70ad-47c9-a80d-9075c14c765a', 'name': 'Kate'},
    {'customerId': 'e98a4069-41fd-4961-86ac-bffb9eea08c4', 'name': 'Paul'},
    {'customerId': '1c67131b-aa8d-42cc-87b9-5ed7cc88fa18', 'name': 'Susan'},
    {'customerId': 'cce3fd42-e97c-4164-8e88-f3b3d0108763', 'name': 'Andrew'},
]

if __name__ == "__main__":
    path = paths[2]
    select = "second"
    for i, val in enumerate(path[select]):
        before = path[select][i - 1]
        if i > 0:
            if abs(val[0] - before[0]) > 1 and abs(val[1] - before[1]) > 1:
                print("gap at: ", i)
