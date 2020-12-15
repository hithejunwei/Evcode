def read_tsp(path):
    data=[]
    for line in open(path,'r'):
        if not line:
            break
        tmp=line.split()
        data.append(tmp)
    data=data[6:-1]
    newdata=[]
    for tmp in data:
        triple=[]
        for i in range(len(tmp)):
            tmpdata=tmp[i]
            if i ==0:
                tmpdata=int(tmpdata)
            else:
                tmpdata=float(tmpdata)
            triple.append(tmpdata)
        newdata.append(triple)
    return newdata
if __name__=='__main__':
    data=read_tsp('pr2392.tsp')
    print(data)