data = ["AI", "ML", "AI", "Python", "ML", "AI"]
def count_occurrences(data, target):
     if not data:
        return 0
     return (1 if data[0] == target else 0) + count_occurrences(
          data[1:], target)

print(count_occurrences(data,"AI"))