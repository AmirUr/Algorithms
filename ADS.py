krestiki = [["X", "", "X"],
            ["X", "O", "X"],
            ["X", " ", "O"]]
for row in krestiki:
    if row[0] == row[1] == row[2] and row[0] != " ":
        print(f"Победитель: {row[0]}")


if krestiki[0][0] == krestiki[1][1] == krestiki[2][2] and krestiki[0][0] != " ":
    print(f"Победитель {krestiki[0][0]}")
if krestiki[0][2] == krestiki[1][1] == krestiki[2][0] and krestiki[0][2] != " ":
    print(f"Победитель {krestiki[0][2]}")

for col in range(3):
    if krestiki[0][col] == krestiki[1][col] == krestiki[2][col] and krestiki[0][col] != " ":
        print(f"Победитель: {krestiki[0][col]}")



def search_in_matrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False

matrix1 = [["X", "", "X"],
            ["X", "O", "X"],
            ["X", " ", "O"]]

print(search_in_matrix(matrix1, "O"))



def Ferz(n):
    def print_board(board, n):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()

    def add_sol(board, ans, n):
        temp = []
        for i in range(n):
            string = ""
            for j in range(n):
                string += board[i][j]
            temp.append(string)
        ans.append(temp)

    def is_safe(row, col, board, n):
        x = row
        y = col

        while (x >= 0):
            if board[x][y] == "Q":
                return False
            else:
                x -= 1

        x = row
        y = col
        while (y < n and x >= 0):
            if board[x][y] == "Q":
                return False
            else:
                y += 1
                x -= 1

        x = row
        y = col
        while (y >= 0 and x >= 0):
            if board[x][y] == "Q":
                return False
            else:
                x -= 1
                y -= 1
        return True

    def solveNQueens(row, ans, board, n):
        if row == n:
            add_sol(board, ans, n)
            return

        for col in range(n):
            if is_safe(row, col, board, n):
                board[row][col] = "Q"
                solveNQueens(row + 1, ans, board, n)
                board[row][col] = "."

    if __name__ == "__main__":
        board = [["." for i in range(n)] for j in range(n)]
        ans = []
        solveNQueens(0, ans, board, n)

        if ans == []:
            print("Solution does not exist")
        else:
            print(len(ans))
            print(f"Out Of {len(ans)} solutions one is following")
            for i in range(len(ans)):
                print_board(ans[i], n)
                print("---------------")
print(Ferz(8))


def count_ways(n):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]
print(count_ways(15))


def create_three_stacks(stack_size):
    stack_array = [None] * (stack_size * 3)
    stack_pointers = [0, stack_size, stack_size * 2]
    return stack_array, stack_pointers

def push(stack_array, stack_pointers, stack_num, data):
    stack_size = len(stack_array) // 3
    if stack_pointers[stack_num] >= (stack_num + 1) * stack_size:
        print("Стек переполнен")
        return
    stack_array[stack_pointers[stack_num]] = data
    stack_pointers[stack_num] += 1

def pop(stack_array, stack_pointers, stack_num):
    stack_size = len(stack_array) // 3
    if stack_pointers[stack_num] == stack_num * stack_size:
        print("Стек пуст")
        return None
    data = stack_array[stack_pointers[stack_num] - 1]
    stack_array[stack_pointers[stack_num] - 1] = None
    stack_pointers[stack_num] -= 1
    return data

def peek(stack_array, stack_pointers, stack_num):
    stack_size = len(stack_array) // 3
    if stack_pointers[stack_num] == stack_num * stack_size:
        print("Стек пуст")
        return None
    return stack_array[stack_pointers[stack_num] - 1]

stack_array, stack_pointers = create_three_stacks(5)  # создаем массив и указатели для трех стеков
push(stack_array, stack_pointers, 0, 1)  # добавляем элемент 1 в первый стек
push(stack_array, stack_pointers, 1, 2)  # добавляем элемент 2 во второй стек
push(stack_array, stack_pointers, 2, 3)  # добавляем элемент 3 в третий стек

print(pop(stack_array, stack_pointers, 0))  # выводим и удаляем элемент из первого стека
print(peek(stack_array, stack_pointers, 1))  # просматриваем верхний элемент второго стека

push(stack_array, stack_pointers, 0, 4)  # добавляем элемент 4 в первый стек
print(pop(stack_array, stack_pointers, 2))  # выводим и удаляем элемент из третьего стека


def exponential_filter(input_value, prev_output, alpha):
    return alpha * input_value + (1 - alpha) * prev_output

# Вводные данные
input_value = 10.0  # Входное значение
prev_output = 5.0  # Предыдущее значение выхода
alpha = 0.2  # Коэффициент сглаживания

print(exponential_filter(input_value, prev_output, alpha))


def find_missing_number(arr):
    n = len(arr)
    num_set = set(arr)

    # Проверяем каждое целое число, начиная с 1
    for i in range(1, n + 2):
        if i not in num_set:
            return i

    # Если все числа с 1 до n+1 присутствуют, возвращаем n+2
    return n + 2

# Пример использования
arr = [3, 1, 4, 6, 2]
missing_number = find_missing_number(arr)
print("Наименьшее пропущенное число:", missing_number)





