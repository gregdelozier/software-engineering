from calc import add
from random import randint
from random import uniform

def test_add():
    assert add(2,2) == 4
    assert add(1,3) == 4
    assert add(2,4) == 6
    assert add(-1,5) == 4
    assert add(6,7) == 13
    assert add(6.5, 7.5) == 14
    assert add(-6.5, -7.5) == -14
    assert add(-6.521, -7.521) == -14.042
    assert add(521, 321) == 842
    assert add(0,12) == 12
    assert add(0,-3) == -3
    assert add(-3,-3) == -6 
    assert add(-4,-4) == -8 
    assert add(-5,-5) == -10 
    assert add(0,0) == 0
    string_legal = False
    try: 
        assert add("cat","dog") == "catdog"
        string_legal = True
    except:
        pass        
    assert not string_legal, "Strings should not be accepted"
    string_legal = False
    try: 
        assert add("foo","taz") == "footaz"
        string_legal = True
    except:
        pass        
    assert not string_legal, "Strings should not be accepted"
    string_legal = False
    try: 
        assert add("+","-") == "+-"
        string_legal = True
    except:
        pass        
    assert not string_legal, "Strings should not be accepted"
    assert add(1000, 12) == 1012
    for i in range(0, 1000000):
        k = randint(-100000000,1000000)
        j = randint(-1000000,100000000)
        assert add(k,j) == k + j
    for i in range(0, 1000000):
        k = uniform(-100000000.0, 1000000.0)
        j = uniform(-1000000.0, 100000000.0)
        assert add(k,j) == k + j
    assert add(add(2,3),4) == 9

if __name__ == "__main__":
    test_add()
    # print(add(1.2345, 4.567))
    print("done.")
