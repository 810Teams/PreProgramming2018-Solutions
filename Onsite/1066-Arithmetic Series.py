"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    start, stop, step = int(input()), int(input()), int(input())
    counter = 0
    total = 0

    while counter < stop:
        total += start + step*counter
        counter += 1

    print(total)

main()
