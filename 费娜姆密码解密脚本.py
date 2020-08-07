#--encoding:utf-8--
table = {'A':'1000001','N':'1001110',
         'B':'1000010','O':'1001111',
         'C':'1000011','P':'1010000',
         'D':'1000100','Q':'1010001',
         'E':'1000101','R':'1010010',
         'F':'1000110','S':'1010011',
         'G':'1000111','T':'1010100',
         'H':'1001000','U':'1010101',
         'I':'1001001','V':'1010110',
         'J':'1001010','W':'1010111',
         'K':'1001011','X':'1011000',
         'L':'1001100','Y':'1011001',
         'M':'1001101','Z':'1011010'}
key_list=[]  
value_list=[]  
for key,value in table.items():  
    key_list.append(key)  
    value_list.append(value)
#print key_list, value_list
def get_key_of_value(value):  
    if value in value_list:  
        get_value_index = value_list.index(value)
        #print type(key_list[get_value_index])
        return key_list[get_value_index]  
    else:  
        print ("你要查询的值%s不存在" %get_value)  
def how_to(a,b):
    if a in ['0','1'] and b in ['0','1']:
        if a == '1' and b == '1':
            return '0'
        elif a == '0' and b == '0':
            return '0'
        else:
            return '1'
    else:
        return 0
def bin_turn(arg):
    binstring = ''
    for i in arg:
        binstring += table[i]
    return binstring
def encrypt(plain,key):
    binkey = bin_turn(key)
    binplain = bin_turn(plain)
    chiper = ''
    if len(binplain)==len(binkey):
        for i in range(0,len(binplain)):
            chiper += how_to(binkey[i],binplain[i])
            #print
        return chiper
    else:
        return 0
def decrypt(chiper,key):
    binkey = bin_turn(key)
    plain = ''
    if len(chiper)==len(binkey):
        for i in range(0,len(chiper)):
            plain += how_to(binkey[i],chiper[i])
            #print binkey[i]
        #print plain
        return plain
    else:
        return 0  
key = 'WELCOMETOCFF'
chiper = '000000000000000000000000000000000000000000000000000101110000110001000000101000000001'
binplain = decrypt(chiper,key)
#print type(binplain)
plain = ''
for i in range(0,len(binplain),7):
    plain += str(get_key_of_value(binplain[i:i+7]))
print (plain)
