import speed_calculator_1ex

running_distance = float(input("What distance you run? : "))
running_time = float(input("What time run? : "))

speed = speed_calculator_1ex.speed(running_distance, running_time)
print(f"Twoja średnia prędkość biegu jest równa {speed} km/h. ")