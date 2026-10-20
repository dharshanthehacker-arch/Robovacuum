from robovacuum.room import Room

room = Room(seed=42)
print(room)
print("Dirt tiles:", room.dirt_remaining())
