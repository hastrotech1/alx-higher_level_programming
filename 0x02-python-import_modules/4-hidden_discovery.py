#!/usr/bin/python3


if __name__ == "__main__":

    import hidden_4

    file = dir(hidden_4)

    for q in file:
        if not q.startswith("__"):
            print("{:s}".format(q))
