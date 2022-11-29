import math
import copy

print("1. Зашифрувати текст")
print("2. Розшифрувати текст")




matrix_a=[[10, 7, 0],
          [17, 18, 21],
          [8, 19, 20]]








negative_a=[]



alphabet=[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', ';', '-', '\'']                                #Алфавіт




def anti_det(number):
    for i in range(0, 1000):
        if((number*i)%32==1):
            return(i)

def multiply(a, b):
    c=[]
    for i in range(0, 3):
        index = 0
        buffer = 0
        for k in range(0, 3):
            buffer+=a[i][index]*b[index]
            index+=1
        c.append(buffer)
    return(c)

def determinant3x3(martix):
    a=martix[0][0]*martix[1][1]*martix[2][2]+martix[1][0]*martix[2][1]*martix[0][2]+martix[0][1]*martix[1][2]*martix[2][0]
    b=martix[0][2]*martix[1][1]*martix[2][0]+martix[0][0]*martix[1][2]*martix[2][1]+martix[0][1]*martix[1][0]*martix[2][2]
    return(a-b)

def determinant2x2(matrix):
    det=matrix[0]*matrix[3]-matrix[1]*matrix[2]
    return(det)

def arr_to_matrix(massive):
    counter=0
    matrix=[]
    for i in range(0, 3):
        array=[]
        array.append(massive[counter])
        array.append(massive[counter+1])
        array.append(massive[counter+2])
        counter+=3
        matrix.append(array)
    return(matrix)

def ally(matrix):
    ally_matrix=[]
    buffer=[]
    array=[]
    for i in range(0, 3):
        for j in range(0, 3):
            minor = []
            for k in range(0, 3):
                for l in range(0, 3):
                    if(i!=k and j!=l):
                        minor.append(matrix[k][l])
            buffer.append(determinant2x2(minor)*math.pow(-1, i+j+2))
    counter=0
    for i in range(0, 3):
        array=[]
        array.append(buffer[counter])
        array.append(buffer[counter+1])
        array.append(buffer[counter+2])
        counter+=3
        ally_matrix.append(array)


    return(ally_matrix)

def transponed(matrix):
    matrix_shtrih=copy.deepcopy(matrix)
    for i in range(0, 3):
        for j in range(0, i):
            matrix_shtrih[i][j], matrix_shtrih[j][i]=matrix_shtrih[j][i], matrix_shtrih[i][j]
    return matrix_shtrih

def negative(matrix):
    trans_matrix=transponed(matrix)
    ally_matrix=ally(trans_matrix)
    det=anti_det(determinant3x3(matrix))
    if(det==None):
        print("Такий ключ не підходить")
        exit()
    for i in range(0, 3):
        for j in range(0, 3):
            ally_matrix[i][j]=ally_matrix[i][j]*det
    return(ally_matrix)

def find_NSD(a, b):
    if a % b == 0:
        return b
    else:
        return find_NSD(b, a % b)

def cipher(matrix, text):
    while(len(text)%3!=0):
        text.append(".")
    buffer_matrix=[[1], [1], [1]]
    ciphered_text=[]
    result=[]
    for i in range(0, len(text), 3):
        for k in range(0, 3):
            buffer_matrix[k]=alphabet.index(text[i+k])
        ciphered_text.append(multiply(matrix, buffer_matrix))
    for row in ciphered_text:
        for i in row:
            i=round(i)
            a=i%32
            result.append(alphabet[a])
    return(result)






file=""
while(True):
    choice=int(input())
    if(choice==1):
        file= "Sample.txt"
        matrix2=matrix_a
        break
    elif(choice==2):
        file = "Sample2.txt"
        matrix2=negative(matrix_a)
        break
    else:
        print("Такого варіанту немає")
        continue

f = open(file, 'r')
text=[]
for i in f.read():
    text.append(i)
f.close()

for i in range(0, len(text)):
    if(text[i]=="\n"):
        text[i]=" "

print("determinant", determinant3x3(matrix_a))
print("NSD", find_NSD(32, determinant3x3(matrix_a)))

if(determinant3x3(matrix_a)!=0):
    negative_matrix=negative(matrix_a)
    if(find_NSD(32, determinant3x3(matrix_a))!=1):
        print("Такий ключ не підходить")
        exit()
    else:
        new_text=(cipher(matrix2, text))
        for i in new_text:
            print(i, end="")

else:
    print("Такий ключ не підходить")
    exit()

