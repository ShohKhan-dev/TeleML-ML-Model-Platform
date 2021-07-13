def get_score(gender, age, distance):

    if age > 12:
        if gender == 'F':
            distance_levels = [
                [1500, 1600, 1900, 2000],
                [1600, 1700, 2000, 2100],
                [1700, 1800, 2100, 2300],
                [1500, 1800, 2200, 2700],
                [1400, 1700, 2000, 2500],
                [1200, 1500, 1900, 2300],
                [1100, 1400, 1700, 2200]
            ]
        else:
            distance_levels = [
                [2100, 2200, 2400, 2700],
                [2200, 2300, 2500, 2800],
                [2300, 2500, 2700, 3000],
                [1600, 2200, 2400, 2800],
                [1500, 1900, 2300, 2700],
                [1400, 1700, 2100, 2500],
                [1300, 1600, 2000, 2400]
            ]

        age_levels = [15, 17, 20, 30, 40, 50]
        scores = ['Very bad', 'Bad', 'Average', 'Good', 'Excellent']
        age_index = len([x for x in age_levels if x <= age])
        distance_index = len([x for x in distance_levels[age_index] if x <= distance])
        return scores[distance_index]
    else:
        return "Age should be greater than 12"

print(get_score('F', 38, 2099))