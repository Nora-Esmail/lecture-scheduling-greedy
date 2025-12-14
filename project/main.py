lectures = [
    {"name": "Lecture 1", "start": 1, "end": 3},
    {"name": "Lecture 2", "start": 2, "end": 5},
    {"name": "Lecture 3", "start": 4, "end": 6},
    {"name": "Lecture 4", "start": 6, "end": 7},
    {"name": "Lecture 5", "start": 5, "end": 9},
]
lectures_sorted = sorted(lectures, key=lambda x: x["end"])

selected = []
last_end = -1

for lec in lectures_sorted:
    if lec["start"] >= last_end:
        selected.append(lec)
        last_end = lec["end"]

print("Selected Lectures:")
for s in selected:
    print(s["name"], "from", s["start"], "to", s["end"])