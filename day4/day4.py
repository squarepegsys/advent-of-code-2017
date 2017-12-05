
def test_passphrase():

    assert passphrase("aa bb cc dd ee")
    assert not passphrase("aa bb cc dd aa")


    assert passphrase("aa bb cc dd aaa")

    assert passphrase("pphsv ojtou brvhsj cer ntfhlra udeh ccgtyzc zoyzmh jum lugbnk")
def passphrase(phrase):

    words = phrase.strip().split(" ")

    return len(words)==len(set(words))
    
        
if __name__=="__main__":

    valid=0
    for line in open("input.txt").readlines():
        if not line:
            continue
        
        if passphrase(line):
            valid+=1

    print(valid)


