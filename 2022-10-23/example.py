def main():
    with open("example.py") as ex:
        for line in ex:
            print(line.rstrip())

main()