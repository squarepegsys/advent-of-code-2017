
def test_passphrase():

    assert passphrase("abcde fghiaa bb cc dd ee")

    assert not passphrase("abcde xyz ecdab")

    assert passphrase("a ab abc abd abf abj")
    
def passphrase(phrase):

    words = ["".join(sorted(x)) for x in phrase.strip().split(" ")]

    return len(words)==len(set(words))
    
        
if __name__=="__main__":

    valid=0
    for line in open("input.txt").readlines():
        if not line:
            continue
        
        if passphrase(line):
            valid+=1

    print(valid)


