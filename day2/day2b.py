def test_checksum():


    sheet="""5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5"""

    assert find_row_val([5,9,2,8])==4

    assert checksum(sheet)==9



def find_row_val(numbers):

    idx=0
    for x in numbers:
        for y in numbers[idx+1:]:
            top=max(x,y)
            bottom=min(x,y)

            if (top/bottom==int(top/bottom)):
                return int(top/bottom)
        idx+=1
        
def checksum(sheet):

    per_row = []

    for row in sheet.split("\n"):
        num_row = [int(x) for x in row.split("\t")]

        per_row.append(find_row_val(num_row))


    return sum(per_row)


if __name__=='__main__':

    print(checksum(open("input.txt").read().strip()))
