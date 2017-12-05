def test_decoder():

    assert decode("1212")==6

    assert decode("1221")==0

    assert decode("123425")==4

    assert decode("123123")==12

    assert decode("12131415")==4
    

def decode(numbers):

    numberList = [int(x) for x in numbers]

    last_idx = len(numberList)-1

    vals = []
    idx=0

    step_val=int(len(numberList)/2)

    for val in numberList:
        
        right_idx = (idx+step_val)%len(numberList)

        right_val = numberList[right_idx]

        if (val==right_val):
            vals.append(val)

        idx+=1


    value = sum(vals)

    print(value)

    return value
    
if __name__=='__main__':

    fp = open("input.txt")

    print(decode(fp.read().strip()))
