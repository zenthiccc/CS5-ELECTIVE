from tree import Vertex, Tree
import inspect, os, sys

def test1():
    v10 = Vertex(10)
    # level 1
    t = Tree(v10)
    print("Expected output:\n0")
    print("Actual output: ")
    print(t.compute_m())

def test2():
    v10 = Vertex(10)
    v15 = Vertex(15)
    v20 = Vertex(20)
    v25 = Vertex(25)
    # level 1
    v10.add_child(v15)
    # level 2
    v15.add_child(v20)
    # level 3
    v20.add_child(v25)
    t = Tree(v10)
    print("Expected output:\n1")
    print("Actual output: ")
    print(t.compute_m())

def test3():
    v10 = Vertex(10)
    v15 = Vertex(15)
    v20 = Vertex(20)
    v25 = Vertex(25)
    # level 1
    v10.add_child(v15)
    v10.add_child(v20)
    # level 2
    v20.add_child(v25)
    
    t = Tree(v10)
    print("Expected output:\n2")
    print("Actual output: ")
    print(t.compute_m())

def test4():
    v10 = Vertex(10)
    v15 = Vertex(15)
    v20 = Vertex(20)
    v25 = Vertex(25)
    v30 = Vertex(30)
    v35 = Vertex(35)
    v40 = Vertex(40)
    v45 = Vertex(45)
    # level 1
    v10.add_child(v15)
    v10.add_child(v20)
    # level 2
    v15.add_child(v25)
    v15.add_child(v30)
    v15.add_child(v35)
    v20.add_child(v40)
    v20.add_child(v45)

    t = Tree(v10)
    print("Expected output:\n3")
    print("Actual output: ")
    print(t.compute_m())

def test5():
    v10 = Vertex(10)
    v15 = Vertex(15)
    v20 = Vertex(20)
    v25 = Vertex(25)
    v30 = Vertex(30)
    v35 = Vertex(35)
    v40 = Vertex(40)
    v45 = Vertex(45)
    v50 = Vertex(50)
    v55 = Vertex(55)
    v60 = Vertex(60)
    v65 = Vertex(65)
    v70 = Vertex(70)
    # level 1
    v10.add_child(v15)
    v10.add_child(v20)
    # level 2
    v15.add_child(v25)
    v20.add_child(v30)
    # level 3
    v25.add_child(v35)
    v25.add_child(v40)
    v25.add_child(v45)
    v25.add_child(v50)
    v30.add_child(v55)
    v30.add_child(v60)
    v30.add_child(v65)
    v30.add_child(v70)

    t = Tree(v10)
    print("Expected output:\n4")
    print("Actual output: ")
    print(t.compute_m())


def run():
    tests = [obj for name,obj in inspect.getmembers(sys.modules[__name__]) 
                if (inspect.isfunction(obj) and name.startswith('test'))]
    
    test_ctr = 1
    for test in tests:
        print('\nRunning Test #' + test_ctr.__str__())
        try:
            test()
        except Exception as e:
            print('ERROR: Program crashed/raised an error! See error message below: ')
            print(e)
        test_ctr += 1

    print()

run()