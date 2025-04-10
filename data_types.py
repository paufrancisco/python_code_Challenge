starting_location = input("Enter the starting location: ")
destination = input("Enter the destination: ")
mode_of_transport = input("Enter the mode of transport: ")

distance = float(input("Enter the distance in kilometers: "))
speed = float(input("Enter the speed in kilometers per hour: "))

estimated_travel_time = distance / speed

isMoreThan5hours = estimated_travel_time > 5


print(f"Trip Details:")
print(f"Starting Location: {starting_location}")
print(f"Destination: {destination}")
print(f"Mode of Transport: {mode_of_transport}")
print(f"Distance: {distance} km")
print(f"Speed: {speed} km/h")
print(f"Estimated Travel Time: {estimated_travel_time} hours")
if isMoreThan5hours:
    print("Travel exceeds 5 hours. You need a rest stop.")
    
else:
    print("Keep traveling.")