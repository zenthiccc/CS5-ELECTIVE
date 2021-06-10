from social_network import SocialNetwork
import inspect, os, sys

def test1():
    sn = SocialNetwork()
    user1 = sn.create_user('dark_knight')
    user2 = sn.create_user('choox')
    user3 = sn.create_user('aaroooon')
    sn.create_friendship(user1, user2)
    sn.create_friendship(user2, user3)
    sn.create_friendship(user3, user1)
    print('Expected Result: \n1')
    print('Actual Result: ')
    print(sn.count_circles())

def test2():
    sn = SocialNetwork()
    user1 = sn.create_user('dark_knight')
    user2 = sn.create_user('choox')
    user3 = sn.create_user('aaroooon')
    user4 = sn.create_user('aldog')
    user5 = sn.create_user('Calinou')
    sn.create_friendship(user1, user2)
    sn.create_friendship(user1, user3)
    sn.create_friendship(user4, user5)
    print('Expected Result: \n2')
    print('Actual Result: ')
    print(sn.count_circles())

def test3():
    sn = SocialNetwork()
    user1 = sn.create_user('dark_knight')
    user2 = sn.create_user('choox')
    user3 = sn.create_user('aaroooon')
    user4 = sn.create_user('aldog')
    user5 = sn.create_user('Calinou')
    user6 = sn.create_user('r4ngo')
    user7 = sn.create_user('thelegend27')
    user8 = sn.create_user('captain_hook')
    user9 = sn.create_user('v3ngeful_spirit')
    sn.create_friendship(user1, user2)
    sn.create_friendship(user1, user3)
    sn.create_friendship(user4, user5)
    sn.create_friendship(user6, user7)
    sn.create_friendship(user6, user8)
    sn.create_friendship(user8, user9)
    sn.create_friendship(user9, user6)
    print('Expected Result: \n3')
    print('Actual Result: ')
    print(sn.count_circles())

def test4():
    sn = SocialNetwork()
    user1 = sn.create_user('dark_knight')
    user2 = sn.create_user('choox')
    user3 = sn.create_user('aaroooon')
    user4 = sn.create_user('aldog')
    user5 = sn.create_user('Calinou')
    user6 = sn.create_user('r4ngo')
    user7 = sn.create_user('thelegend27')
    user8 = sn.create_user('captain_hook')
    user9 = sn.create_user('v3ngeful_spirit')
    user10 = sn.create_user('AM')
    user11 = sn.create_user('CM')
    sn.create_friendship(user1, user2)
    sn.create_friendship(user2, user3)
    sn.create_friendship(user3, user4)
    sn.create_friendship(user1, user6)
    sn.create_friendship(user2, user7)
    sn.create_friendship(user7, user8)
    sn.create_friendship(user1, user9)
    sn.create_friendship(user4, user10)
    sn.create_friendship(user10, user11)
    print('Expected Result: \n2')
    print('Actual Result: ')
    print(sn.count_circles())

def test5():
    sn = SocialNetwork()
    print('Expected Result: \n0')
    print('Actual Result: ')
    print(sn.count_circles())
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