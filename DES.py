def subkey(l1,r1):
    res=l1+r1
    sk1=""
    for j in PC2:
        sk1+=res[j-1]
    return sk1

def XR(a,b):
    if (a==b):
        return '0'
    else:
        return '1'
    
def Decimal(num):
    dec=0
    two=1
    for i in range(len(num)-1,-1,-1):
        if num[i]=='1':
            dec+=two
        two=two*2
    return dec

def binary(w):
    d={
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111',
        'O':'0000'}
    res=''
    for i in w:
        res+=d[i]
    return res
def HEX(m):
    result=""
    d={'0000':'0',
       '0001':'1',
       '0010':'2',
       '0011':'3',
       '0100':'4',
       '0101':'5',
       '0110':'6',
       '0111':'7',
       '1000':'8',
       '1001':'9',
       '1010':'A',
       '1011':'B',
       '1100':'C',
       '1101':'D',
       '1110':'E',
       '1111':'F'
        }
    for i in range(0,len(m),4):
        it=m[i:i+4]
        result+=d[it]
    return result

def dectobin(n):
    result=""
    while(n!=0):
        if(n%2==1):
            result='1'+result
        else:
            result='0'+result
        n=n//2
    if(len(result)%4!=0):
        result='0'*(4-len(result)%4)+result
    return result

PC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
IP=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
IP_1=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
EP=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
Permu=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
S1=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
S2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
S3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
S4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
S5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
S6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
S7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
S8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
Lad=['A','B','C','D','E','F']
LS=[S1,S2,S3,S4,S5,S6,S7,S8]



def Segre(nm):
    PT1=[]
    for i in range(0,len(nm),16):
        PT1.append(nm[i:i+16])
    return PT1


def Encrypt(nm,key):
    pt=nm
    res1= binary(key)
    pt1=Segre(nm)
    NE=[]
    for io in pt1:
        res2= binary(io)
        pres1=""
         
        for i in PC1:
            pres1+=res1[i-1]

        #Sub key generation
            
        l1=""
        r1=""
        n=16
        subk=[]

        for i in range(n):
            if(i==0):
                l1+=pres1[1:28]+pres1[0]
                r1+=pres1[29:]+pres1[28]
                subk.append(subkey(l1,r1))
            elif(i==1 or i==8 or i==15):
                l1=l1[1:]+l1[0]
                r1=r1[1:]+r1[0]
                subk.append(subkey(l1,r1))
            else:
                l1=l1[2:]+l1[:2]
                r1=r1[2:]+r1[:2]
                subk.append(subkey(l1,r1))
        '''
        for i in range(16):
            print("Sub key",i+1,":",subk[i])
        '''
        mip=""
        for i in IP:
            mip+=res2[i-1]

        Li=mip[:32]
        Ri=mip[32:]
        for k in range(16):
            ep=""
            for i in EP:
                ep+=Ri[i-1]
            epxsk1=""
            for i in range(len(ep)):
                epxsk1+=XR(ep[i],subk[k][i])

            count=0
            complete=""
            for i in range(0,len(epxsk1),6):
                row=epxsk1[i]+epxsk1[i+5]
                drow=Decimal(row)
                col=epxsk1[i+1:i+5]
                dcol=Decimal(col)
                num=LS[count][drow][dcol]
                result=""
                if num>9:
                    num-=10
                    result+=Lad[num]
                else:
                    result+=str(num)
                count+=1
                complete+=binary(result)

            func=""
            for i in Permu:
                func+=complete[i-1]

            modf=""
            for i in range(len(func)):
                modf+=XR(func[i],Li[i])
            Li=Ri
            Ri=modf

        RL=Ri+Li
        ctb=""
        for i in IP_1:
            ctb+=RL[i-1]

        CT=""
        for i in range(0,len(ctb),4):
            mid=ctb[i:i+4]
            z=Decimal(mid)
            if z>9:
                z=z-10
                CT+=Lad[z]
            else:
                CT+=str(z)
        NE.append(CT)
    tex=""
    for i in NE:
        tex+=i
    return tex

def Decrypt(ct,key):
    res1= binary(key)
    NE=[]
    pt1=Segre(ct)
    for io in pt1:
        res2= binary(io)
        pres1=""
        for i in PC1:
            pres1+=res1[i-1]
        l1=""
        r1=""
        n=16
        subk=[]

        for i in range(n):
            if(i==0):
                l1+=pres1[1:28]+pres1[0]
                r1+=pres1[29:]+pres1[28]
                subk.append(subkey(l1,r1))
            elif(i==1 or i==8 or i==15):
                l1=l1[1:]+l1[0]
                r1=r1[1:]+r1[0]
                subk.append(subkey(l1,r1))
            else:
                l1=l1[2:]+l1[:2]
                r1=r1[2:]+r1[:2]
                subk.append(subkey(l1,r1))
        '''
        for i in range(16):
            print("Sub key",i+1,":",subk[i])
        '''
        mip=""
        for i in IP:
            mip+=res2[i-1]
        Li=mip[:32]
        Ri=mip[32:]
        for k in range(16):
            ep=""
            for i in EP:
                ep+=Ri[i-1]
            epxsk1=""
            for i in range(len(ep)):
                epxsk1+=XR(ep[i],subk[15-k][i])

            count=0
            complete=""
            for i in range(0,len(epxsk1),6):
                row=epxsk1[i]+epxsk1[i+5]
                drow=Decimal(row)
                col=epxsk1[i+1:i+5]
                dcol=Decimal(col)
                num=LS[count][drow][dcol]
                result=""
                if num>9:
                    num-=10
                    result+=Lad[num]
                else:
                    result+=str(num)
                count+=1
                complete+=binary(result)

            func=""
            for i in Permu:
                func+=complete[i-1]

            modf=""
            for i in range(len(func)):
                modf+=XR(func[i],Li[i])
            Li=Ri
            Ri=modf

        RL=Ri+Li
        ptb=""
        for i in IP_1:
            ptb+=RL[i-1]

        PT=""
        for i in range(0,len(ptb),4):
            mid=ptb[i:i+4]
            z=Decimal(mid)
            if z>9:
                z=z-10
                PT+=Lad[z]
            else:
                PT+=str(z)
        NE.append(PT)
    tex=""
    for i in NE:
        tex+=i
    return tex
