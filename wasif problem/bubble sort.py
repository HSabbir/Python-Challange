#"wasif:wasif@gmail.com"

array = ["wasif4:wasif@gmail.com","wasif3:wasif@gmail.com","wasif1:wasif@gmail.com","wasif2:wasif@gmail.com"]
for i in range(len(array)-1):
    for j in range(len(array)-1):
        name1,email1 = array[j].split(':')
        name2,email2 = array[j+1].split(':')

        if name1 > name2 :
            array[j],array[j+1] = array[j+1],array[j]

print(array)