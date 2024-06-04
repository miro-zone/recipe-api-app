# Carry defined outside loop with initial value 0.
# 532189 => [9,8,1,2,3,5,0,0,0,0,..]
# 123    => [3,2,1,0,0,0,0,...]  12 % 10 => 2
#           [2,1,3,2,3,5,0] 
# First step => Sum 2 elements + Carry.
# Second step => Save (result%10) to new array. 
# Third step => Update the carry (carry = sum/10)
# Fourth step => repeat


# const char* str ="18373280" => [8,2,3,7,3,8,1]

class HugeInt:
    # expect size 30
    num = []
    def __init__(self):
         self.num = [0 for x in range(30)]
