# # import the python testing framework
# import unittest
# # our "unit"
# # this is what we are running our test on
# def isEven(n):
#     if n % 2 == 0:
#        return True
#     else:
#        return False
# # our "unit tests"
# # initialized by creating a class that inherits from unittest.TestCase
# class IsEvenTests(unittest.TestCase):
#     # each method in this class is a test to be run
#     def testTwo(self):
#         self.assertEqual(isEven(2), True)
#         # another way to write above is
#         self.assertTrue(isEven(2))
#     def testThree(self):
#         self.assertEqual(isEven(3), False)
#         # another way to write above is
#         self.assertFalse(isEven(3))
#     # any task you want run before any method above is executed, put them in the setUp method
#     def setUp(self):
#         # add the setUp tasks
#         print("running setUp")
#     # any task you want run after the tests are executed, put them in the tearDown method
#     def tearDown(self):
#         # add the tearDown tasks
#         print("running tearDown tasks")
# if __name__ == '__main__':
#     unittest.main() # this runs our tes < -v>


class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
        for i in nums:
            self.resutl = num + nums[i]
        return result
    def subtract(self, num, *nums):
    	for i in nums: 
            self.result = num - nums[i]
        return result
md = MathDojo()

x = md.add(2,5)
print(x)

# class Add:
#     def __init__(self):
#         self.result = 0
#     def simple_add(self,num, num1):
#         z = num + num1
#         return self

    # def simple_subtract(self,x, y):
    #     z = x - y
    #     return self

    # def print_result(self):
    #     print(f"This is my total:{self.result}")

# a = Add()

# w = a.simple_add(4,6).simple_add(7,3).print_result()


def total(a,b):
    sum = a+b
    return sum 




