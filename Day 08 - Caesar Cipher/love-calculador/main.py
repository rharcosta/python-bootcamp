def calculate_love_score(name1, name2):
    name_combination = (name1 + name2).upper()
    true = "TRUE"
    love = "LOVE"
    count_true = count_love = 0

    for each_letter in true:
        for name_letter in name_combination:
            if each_letter == name_letter:
                count_true += 1

    for each_letter in love:
        for name_letter in name_combination:
            if each_letter == name_letter:
                count_love += 1

    print(f"{count_true}{count_love}")


calculate_love_score("Rubia", "Marijn")
