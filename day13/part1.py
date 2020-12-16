with open("day13/input.txt", "r") as f:
    arrival_time = int(f.readline().rstrip("/n"))
    busses = [int(bus) for bus in f.readline().rstrip("/n").replace("x", "").split(",") if bus]

minutes_until_departure = [round(abs((arrival_time % bus) - bus)) for bus in busses]
min_wait = min(minutes_until_departure)
bus = busses[minutes_until_departure.index(min_wait)]
print(bus * min_wait)