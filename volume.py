# Validate Inputs
def insert_val(st):
    val=input(st)
    try:
        val=float(val)
    except:
        print('Enter float value')
        val=insert_val(st)
    return val 
#calculate Volume
def cal_concrete():
    l=insert_val('Enter Length (m) :')
    w=insert_val('Enter Width (m)  :')
    h=insert_val('Enter Height (m) :')
    print('Concrete Volume',l*w*h,'m3')
    
 
#
print("Welcome")
while True:
    print('Select Option')
    print('Concrete Volume Calculation : 1')
    print('Exit                        : e')
    op=input("Enter Option :")
    if op == 'e':
        break
    elif op in ('1',):
        cal_concrete()
    else:
        print("Invalid Entry")
