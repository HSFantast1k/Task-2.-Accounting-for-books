def received_operations(oper):
    X, Y = oper
    boxes_coutn[X - 1] += Y
    received_and_sold[0] += Y

def sold_operations(oper):
    X, Y = oper
    if Y >= boxes_coutn[X - 1]:
        received_and_sold[1] += boxes_coutn[X - 1]
        boxes_coutn[X - 1] = 0
    else:
        boxes_coutn[X - 1] -= Y
        received_and_sold[1] += Y


def controler(all_operations_list):
    for operations_list in all_operations_list:
        if int(operations_list[-1]):
            sold_operations(operations_list[:-1])
        else:
            received_operations(operations_list[:-1])


N, M = map(int, input().split())
all_operations = [[x for x in map(int, input().split())] for j in range(M)]
boxes_coutn = [0] * N
received_and_sold = [0, 0]
all_operations.sort(key=lambda x: x[-1])
controler(all_operations)
print(*received_and_sold)
print(*boxes_coutn)


