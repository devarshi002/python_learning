from collections import deque

queue = deque(["apple", "banana", "cherry"])
queue.append("date")
print(queue)

queue.popleft()
print(queue)