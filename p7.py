# attendance_tracker.py

# Ask user for total classes held and attended
classes_held = int(input("Enter total number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

# Calculate attendance percentage
attendance = (classes_attended / classes_held) * 100

# Display result
print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance:", attendance, "%")
