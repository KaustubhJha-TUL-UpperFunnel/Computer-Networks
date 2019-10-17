import math
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
        sumOfBnos = bin(int(sumOfBnos[2:],2) + int(i[2:],2)) 
    
    while(len(sumOfBnos)!=18):
        sumOfBnos = bin(int(sumOfBnos[3:],2) + int(1,2))
        
    print(sumOfBnos)
    
    return ~sumOfBnos

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
       
    sumOfBnos = '0b0'
    for i in sixteenBitArr:
        sumOfBnos = bin(int(sumOfBnos[2:],2) + int(i[2:],2))
        
    while(len(sumOfBnos)!=18):
        sumOfBnos = bin(int(sumOfBnos[3:],2) + int(1,2))
    
    
    sumOfBnos += checksum
    
    for i in sumOfBnos[2:]:
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


