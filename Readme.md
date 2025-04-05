# Dictionaries

## Learning Goals

- [ ] **Understand the basic operations with dictionaries in Python.**
- [ ] **Learn how to create, modify, and delete dictionary entries.**
- [ ] **Practice accessing dictionary values and iterating over key-value pairs.**
- [ ] **Explore dictionary methods for retrieving and updating data.**




## Resources
- [Dictionaries](https://www.w3schools.com/PYTHON/python_dictionaries.asp)


## Lab Deliverables

1. Creating Dictionary

- Create a dictionary for a workout named "Push-ups"
- With the keys exercise, sets, reps and notes 

<details>
  <summary>Click Here to view solution</summary>

```
push_ups = {
        "exercise":"Push-ups",
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    }

```

</details>

2. Accessing Dictionary keys

- Print out each key from the dictionary

<details>
  <summary>Click Here to view solution</summary>

```
print(push_ups["exercise"])
print(push_ups["sets"])
print(push_ups["reps"])
print(push_ups["notes"])

```

</details>

3. Accessing Dictionary keys

- Update the sets of the exercise
- Delete notes with del
- Add the key back aw workout_notes with the same value that notes had

<details>
  <summary>Click Here to view solution</summary>

```
# Update the sets of the exercise
push_ups["sets"] = 5

# Delete notes with del
del push_ups["notes"]

#Add the key back aw workout_notes with the same value that notes had
push_ups["workout_notes"] ="Keep your back straight, hands shoulder-width apart."

print(push_ups)

```

</details>

4. Accessing nested data

- Add the nested dictionary below
```
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

```
- Access Lunges notes

<details>
  <summary>Click Here to view solution</summary>

```
#Accessing nested data
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

#Access Lunges notes
print(workout_plan["Lunges"]["notes"])

```

</details>


5. Iterating over a dictionary

- Copy and observe the solution code
<details>
  <summary>Click Here to view solution</summary>

```
# Iterating over a dictionary
# The .items() method converts the dictionary into an iterable collection of key-value pairs (tuples).
# Each tuple contains the key as the first element and the value as the second.
# We can use a for loop to access both the key and value.

for key, value in push_ups.items():
    print(f"{key.upper()}: {value}")

```

</details>

## Submission Instructions

1. Push your code to GitHub.
2. Submit the link to your GitHub repository URL.
