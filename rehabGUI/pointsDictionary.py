def points_dictionary(keypoint):
    switcher = {
        0: "Szyja",
        2: "Prawy bark",
        3: "Prawy lokiec",
        4: "Prawa dlon",
        5: "Lewy bark",
        6: "Lewy lokiec",
        7: "Lewa dlon",
        8: "Biodra",
        9: "Prawe kolano",
        10: "Prawa stopa",
        11: "Biodra",
        12: "Lewe kolano",
        13: "Lewa stopa",
        14: "Glowa"
    }
    return switcher.get(keypoint)

