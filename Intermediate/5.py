road_trip = ["go", "go", "turn left", "go", "fuel", "go", "finish", "fuel"]

for item in road_trip:
    print(item)
    if item == "fuel":
        print("waiting")
        for i in range(10):
            print(f'processing fuel - {i+1}')
        continue
    elif item == "finish":
        break