import math


def add_binary_nums(x, y):
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    # initialize the result
    result = ''

    # initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1  # Compute the carry.

    if carry != 0: result = '1' + result

    return result.zfill(max_len)

def checkSumClientSideImplementation(string):
    sixteenBitArr = []
    binString = ''.join(format(ord(x),'b') for x in string)
    adtZero = math.ceil(len(binString)/16)* 16 - len(binString)
    appZero = '0'*adtZero
    binString = appZero + binString
    print(binString,len(binString))
    for i in range(0,len(binString),16):
        sixteenBitArr.append(binString[i:i+16])
    sixteenBitArr = map(lambda string:'0b'+string ,sixteenBitArr)
       
    sumOfBnos = '0b0'
    for i in sixteenBitArr:
         sumOfBnos = bin(int(sumOfBnos[2:], 2) + int(i[2:], 2))

    if(len(sumOfBnos[2:])<16):
        sumOfBnos = '0b' + str(0*(16 - len(sumOfBnos[2:]))) + sumOfBnos[2:]

    print(sumOfBnos,2)

    temp = sumOfBnos[2:]
    if(len(sumOfBnos[2:])>=17):
        while(len(temp)!= 16):
            temp = add_binary_nums(temp[1:],'0000000000000001')
            #print(sumOfBnos,type(sumOfBnos))
        #sumOfBnos = sumOfBnos[3:]

    comp = ""
    for i in temp:
        if(i=='1'):
            comp = comp+'0'
        else:
            comp+='1'
    print(comp)

    return comp


def checkSumServerSideImplementation(checksum,string):
    sixteenBitArr = []
    binString = ''.join(format(ord(x),'b') for x in string)
    adtZero = math.ceil(len(binString)/16)* 16 - len(binString)
    appZero = '0'*adtZero
    binString = appZero + binString
    print(binString,len(binString))
    for i in range(0,len(binString),16):
        sixteenBitArr.append(binString[i:i+16])
    sixteenBitArr = map(lambda string:'0b'+string ,sixteenBitArr)
       
    sumOfBnos = ""
    for i in sixteenBitArr:
        print(i)
        sumOfBnos = add_binary_nums(sumOfBnos,i[2:])
        print(sumOfBnos,len(sumOfBnos))


    if (len(sumOfBnos) >= 17):
        while (len(sumOfBnos)!=16):
            sumOfBnos = add_binary_nums(sumOfBnos[1:], '0000000000000001')

    print(checksum,sumOfBnos,len(sumOfBnos))
    sumOfBnos = add_binary_nums(sumOfBnos,checksum)
    print(checksum, sumOfBnos)

    for i in sumOfBnos:
        if i=='0':
            print("error")
            return
    print("no error")
    return
    

    
# def checkSumMD5():
#     # File to check
#     file_name = 'filename.exe'

#     # Correct original md5 goes hereṇ
#     original_md5 = '5d41402abc4b2a76b9719d911017c592'  

#     # Open,close, read file and calculate MD5 on its contents 
#     with open(file_name) as file_to_check:
#         # read contents of the file
#         data = file_to_check.read()    
#         # pipe contents of the file through
#         md5_returned = hashlib.md5(data).hexdigest()
#     # Finally compare original MD5 with freshly calculated
#     if original_md5 == md5_returned:
#         print "MD5 verified."
#     else:
#         print "MD5 verification failed!."

    
# def checkSumMD5():
#     # File to check
#     file_name = 'filename.exe'

#     # Correct original md5 goes hereṇ
#     original_md5 = '5d41402abc4b2a76b9719d911017c592'  

#     # Open,close, read file and calculate MD5 on its contents 
#     with open(file_name) as file_to_check:
#         # read contents of the file
#         data = file_to_check.read()    
#         # pipe contents of the file through
#         md5_returned = hashlib.md5(data).hexdigest()
#     # Finally compare original MD5 with freshly calculated
#     if original_md5 == md5_returned:
#         print "MD5 verified."
#     else:
#         print "MD5 verification failed!."


