print("Welcome to NIM memoized\n")

selection = int(input("Enter 1 to run algorithm against n stones. Enter 2 to run algorithm over (0, n) stones\n"))

done = []
w = []


def play():
    num_stones = input("Please enter the number of stones: ")

    for i in range(int(num_stones) + 1):
        done.append(False)
        w.append(False)

    nim(int(num_stones))
    return


def nim(n):

    if not (win(n-1)):
        print("Take 1 stone")
        return 1
    print("Take 2 stones")
    return 2


def win(n):

    if n == 0:
        return True
    if n == 1:
        return False
    if done[n]:
        return w[n]

    w[n] = not (win(n - 1) and win(n - 2))
    done[n] = True

    return w[n]


def showOutput():
    num_stones = int(input("Please enter the number of stones to calculate up to: \n"))

    for i in range(int(num_stones) + 1):
        done.append(False)
        w.append(False)

    for i in range(1, num_stones + 1):
        nim(i)

    return


if selection == 1:
    play()
if selection == 2:
    showOutput()

