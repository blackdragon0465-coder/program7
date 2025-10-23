# attendance_tracker.py

# Ask user for total classes held and attended
classes_held = int(input("Enter total number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

# Calculate attendance percentage
attendance = (classes_attended / classes_held) * 100

# Determine eligibility
if attendance >= 75:
    status = "Eligible for exams"
else:
    status = "Not eligible for exams"

# Display results
print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance:", round(attendance, 2), "%")
print("Status:", status)
