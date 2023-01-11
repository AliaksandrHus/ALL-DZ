
# Решение 1
text = '1 2 3 1'
print(sorted(list(set([x for x in text.lower().split() if text.lower().split().count(x) == max(map(text.lower().split().count, text.lower().split()))])))[0])

# Решение 2
text = '1 2 3 1'
text = text.lower().split()
max_count = max([text.count(x) for x in text])
print(sorted([x for x in text if text.count(x) == max_count])[0])

# Решение 3
text = '1 2 3 1'
t = text.lower().split()
m = [t.count(x) for x in t]
print(sorted([x for x, y in zip(t, m) if y == max(m)])[0])

