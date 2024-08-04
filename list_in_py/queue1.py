from collections import deque

#initializing an empty queue
queue = deque()

#adding to the end of the queue
queue.append("apple")
queue.append("banana")
queue.append("cherry")

print("Queue after enqueuing elements: ", queue)

#removing element from queue

first_ele = queue.popleft()
print("Dequeued element : ", first_ele)
print("Queue after dequeing an element:", queue)

first_ele = queue.popleft()
print("Dequeued element : ", first_ele)
print("Queue after dequeing an element:", queue)

first_ele = queue.popleft()
print("Dequeued element : ", first_ele)
print("Queue after dequeing an element:", queue)
#checking the first ele without removing it
if queue:
    first_ele=queue[0]
    print("first element: ", first_ele)
else:
    print("queue is empty")