def ones(number):
    ones=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
    return ones[number]


def eletohund(number):
    teens=['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens=['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety','One Hundred']
    if number<=19:
        return teens[number-11]
    

    a=list(str(number))
    
    if a[1]=='0':
        return tens[(number//10)-2]

    else:
        return tens[(number//10)-2]+ones(int(a[1]))

number=int(input())



if number<=10:
    print(ones(number))
elif number>10 and number<=100:
    print(eletohund(number))      

        
