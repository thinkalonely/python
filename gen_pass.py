import random
import string
#list1 = ['z', 'y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
#list2 = [i for i in range(1, 10)]

#st = [i for i in random.sample(list1, 2)]
#num = [i for i in random.sample(list2, 6)]
def gen_pass(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#print(st+num)
pass1 = gen_pass()
print(pass1)
