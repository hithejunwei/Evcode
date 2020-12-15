def read_tsp(path):
    data=[]
    for line in open(path,'r'):
        line = line.strip('\n')
        tmp=line.split()
        data.append(tmp)
    data=data[6:]
    return data
if __name__=='__main__':
    data=read_tsp('eil51.tsp')
    print(data)