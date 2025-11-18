ball = []
ball.append(5)
ball.append(4)
ball.append(3)
ball.append(5)
ball.append(2)
print("Текущие оценки:", ball)
first = ball.pop(0)
last = ball.pop()
sum = sum(ball)
schet = len(ball)
average = sum / schet
print("Средний балл:", average)
print("Итоговые оценки:", ball)
