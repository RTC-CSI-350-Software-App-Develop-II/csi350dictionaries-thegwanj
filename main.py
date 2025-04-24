push_ups = {
    "exercise": "Push-ups",
    "sets": 2,
    "reps": 20,
    "notes": "Inhale as you go down, exhale as you go back up"
}

# Print each key
print(push_ups["exercise"])
print(push_ups["sets"])
print(push_ups["reps"])
print(push_ups["notes"])

# Update sets
push_ups["sets"] = 3

# Delete notes
del push_ups["notes"]

# Add notes back as workout_notes using the same value
push_ups["workout_notes"] = "Inhale as you go down, exhale as you go back up"

# Adding nested dictionary
workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}

# Access Lunges notes
print(workout_plan["Lunges"]["notes"])

# Copy-Paste code from readme
# Iterating over a dictionary
# The .items() method converts the dictionary into an iterable collection of key-value pairs (tuples).
# Each tuple contains the key as the first element and the value as the second.
# We can use a for loop to access both the key and value.

for key, value in push_ups.items():
    print(f"{key.upper()}: {value}")