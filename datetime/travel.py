def hotelCost(nights):
    return nights * 140

def planeRideCost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    else:
        return 500
    
def CarRentalCost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40*days

def tripCost(city, days, spendingMoney):
    return planeRideCost(city) + CarRentalCost(days) + hotelCost(days) + spendingMoney

print("Our trip costed:",tripCost("Los Angeles", 6, 150))