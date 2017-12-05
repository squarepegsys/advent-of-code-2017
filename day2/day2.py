def test_checksum():

    sheet = """5\t1\t9\t5
7\t5\t3
2\t4\t6\t8"""

    assert checksum(sheet)==18


def checksum(sheet):

    per_row = []

    for row in sheet.split("\n"):
        num_row = [int(x) for x in row.split("\t")]

        difference = max(num_row)-min(num_row)
        per_row.append(difference)

    return sum(per_row)


if __name__=='__main__':

    print(checksum(open("input.txt").read().strip()))
