
def test_bank_redist():

    assert redistribute([0, 2, 7, 0])[0]==5

def redistribute(banks):

    realloct = [banks]

    iterations=0

    
    while True:
        # need to copy it each time, cuz Python does references here
        banks = [x for x in banks]

        max_val = max(banks)

        bank_idx = banks.index(max(banks))

        banks[bank_idx]=0

        while max_val>0:

            bank_idx = (bank_idx+1)%len(banks)

            banks[bank_idx]+=1

            max_val-=1

        iterations+=1

        if (banks in realloct):
            break

        realloct.append(banks)
        

    return iterations,banks

            
if __name__=='__main__':

   banks = [int(x) for x in open("input.txt").read().strip().split("\t")]

   iterations,banks = redistribute(banks)

   print(iterations)
   print(redistribute(banks)[0])
