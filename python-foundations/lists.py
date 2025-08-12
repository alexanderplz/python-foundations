# I'm going to make a list containing my favorite things.
# Lists are a compound data type that can group values together.

favorite_things = ["Robotics", "Python", "Finance", "Reading", "Working Out"]
print("My favorite things are " , favorite_things)

my_favorite_number = ["My favorite number is", 7, True]
print(my_favorite_number)

# I want to add my weightlifting stats with a nested list.
weightlifting_stats = [["Bench Press", 225, "lbs"],
                       ["Squat", 375, "lbs"],
                       ["Deadlift", 425, "lbs"],
                       ["Overhead Press", 185, "lbs"]]

#Update new workout for new personal records.
weightlifting_stats = weightlifting_stats + [["Incline Bench Press", 205, "lbs"]]

# I want to create a list that contains only the weight values from my weightlifting stats.
# This will help me analyze my progress more easily.                       
weightlifting_numbers = [
    weightlifting_stats[0][1],  # Bench Press weight
    weightlifting_stats[1][1],  # Squat weight
    weightlifting_stats[2][1],  # Deadlift weight
    weightlifting_stats[3][1],  # Overhead Press weight
    weightlifting_stats[4][1]   # Incline Bench Press weight
]

print("My weightlifting stats are: ", weightlifting_stats)
print(weightlifting_numbers[:5])
print("The highest amount that I can lift is", (max(weightlifting_numbers)), "lbs!")  # This will return the maximum weight lifted.
