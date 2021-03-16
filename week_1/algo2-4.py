alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']      #
string = input()                                        #
count = 0                                               #
for i in alpha:                                         #
   if i in string:                                      #
       string = string.replace(i," ")                   #
print(len(string))                                      # replace : 크로아티아 문자가 2~3개로 인식되므로 하나로 인식되도로고 공백이나 다른 한문자로 대체 해준다.