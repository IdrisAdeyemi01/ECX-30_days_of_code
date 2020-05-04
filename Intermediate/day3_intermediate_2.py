def itos(numb):
    '''
    This function takes in an integer and returns the string form of that integer.
    '''
    if type(numb) != int:
        raise ValueError('Only integer input are allowed')
    diction1= {1:'1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0'}
    num_list = []
	
    num1,num2= numb, numb

    count=0
    while (num1> 0):
        num1= num1//10
        count = count + 1
  
    
    while (count>0):
        num_list.append(num2//10**(count-1))
        num2 = num2%10**(count-1)
        count-= 1
	
    str_list=[]	
    for i in num_list:
        str_list.append(diction1[i])
        string= ''.join(str_list)
    return string

def stoi(string):
    '''
	This function takes in a string as its parameter and converts the string to its integer equivalent.
    '''
    if type(string) != str:
        raise ValueError('Only strings values are allowed')
 
    diction2= {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    string = string[::-1]
    number=0
    for i in range(len(string)):
    	con= diction2[string[i]] * 10**i
    	number += con
    return number


def ftos(float_value):
    '''

    '''
    if not type(float_value) is float:
        raise ValueError('You can only input float values')
    real = float_value//1
    deci_part= float_value%1
    diction3= {1:'1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0'}
    #For the real part
    real_list = []	
    num1,num2= real, real
    count=0
    while (num1> 0):
        num1= num1//10
        count = count + 1
    while (count>0):
        real_list.append(num2//10**(count-1))
        num2 = num2%10**(count-1)
        count-= 1
    realstr_list=[]	
    for i in real_list:
        realstr_list.append(diction3[i])
        string1= ''.join(realstr_list)
    #For the decimal part
    deci_list = []
    counting= 0
    while deci_part%1 != 0:
        deci_part = deci_part*10
        counting +=1
    while (counting>0):
        deci_list.append(deci_part//10**(counting-1))
        deci_part= deci_part% 10**(counting-1)
        counting -= 1
    decistr_list =[]
    for i in deci_list:
        decistr_list.append(diction3[i])
        string2= ''.join(decistr_list)
    float_string = '.'.join([string1,string2])
    return float_string

def stof(string_value):
    '''

    '''
    if not type(string_value) is str:
        raise ValueError('You are only allowed to use  strings')
    diction4= {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    splitter=string_value.split('.')
    whole= splitter[0]
    deci= splitter[1]

    whole = whole[::-1]
    whole_num = 0
    for i in range(len(whole)):
    	con = diction4[whole[i]] * 10**i
    	whole_num += con
    	
    deci = deci[::-1]
    deci_num = 0
    for i in range(len(deci)):
    	con = diction4[deci[i]] * 10**i
    	deci_num += con
    deci_num = deci_num/(10**len(deci))
    final= whole_num + deci_num
    return final
    

    

print(type(itos(345)))
print(type(stoi('4000')))
print(type(ftos(1234.5678)))
print(type(stof('1234.5678')))
