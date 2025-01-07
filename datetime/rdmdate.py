import random
import time

def RandomDate(startDate, endDate):
    print("Creating a random date between", startDate, "and", endDate)
    rand = random.random()
    dateFmt = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFmt))
    endTime = time.mktime(time.strptime(endDate, dateFmt))

    randomTime = startTime + rand * (endTime - startTime)
    randomDate = time.strftime(dateFmt, time.localtime(randomTime))
    return randomDate

print("Some random date:", RandomDate("1/1/2000", "1/7/2025"))