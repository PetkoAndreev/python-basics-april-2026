# Input declarations
length = int(input())
width = int(input())
height = int(input())
perc_full = float(input())

aquarium_volume = length * width * height
total_liters = aquarium_volume * 0.001
perc = perc_full * 0.01 # Sand, etc., air pump...
needed_liters = total_liters * (1-perc) # 100% we subtract air pump, sand, etc.

print(needed_liters)