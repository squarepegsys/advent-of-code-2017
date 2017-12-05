def test_decoder():

    assert decode("1122")==3
    assert decode("1111")==4

    assert decode("1234")==0

    assert decode("91212129")==9

def decode(numbers):

    numberList = [int(x) for x in numbers]

    last_idx = len(numberList)-1

    vals = []
    idx=0

    print(numbers)
    print("### %s" %(last_idx))
    for val in numberList:
        
        right_idx = idx+1

        if (idx==last_idx):
            right_idx=0

        right_val = numberList[right_idx]

        if (val==right_val):
            vals.append(val)

        idx+=1


    value = sum(vals)

    return value
    
if __name__=='__main__':

    fp = open("input.txt")

    print(decode(fp.read().strip()))
