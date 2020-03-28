from Statistics.ZScore import ZScore


def correlation(data, data1):
    try:
        z1 = ZScore(data)
        z2 = ZScore(data1)
        z1_and_z2 = list(map(lambda x, y: x * y, z1, z2))
        correlate = sum(z1_and_z2) / len(z1_and_z2)
        return round(correlate, 2)
    except ZeroDivisionError:
        print("Watch out: You are dividing by Zero!")
