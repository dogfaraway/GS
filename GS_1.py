import numpy as np
import pandas as pd

man = np.array([['貂蝉', '大乔', '小乔', '阿丑', '尚香'],
                ['貂蝉', '小乔', '大乔', '尚香', '阿丑'],
                ['阿丑', '貂蝉', '小乔', '大乔', '尚香'],
              ])
a = ['吕布', '刘备', '孔明', '周瑜', '曹操']
pdman = pd.DataFrame(man, index=a)
print(pdman)

woman = np.array([['曹操', '吕布', '刘备', '周瑜', '孔明'],
                  ['周瑜', '刘备', '孔明', '吕布', '曹操'],
                  ['周瑜', '孔明', '刘备', '曹操', '吕布'],
                  ['吕布', '刘备', '周瑜', '孔明', '曹操'],
                  ['孔明', '周瑜', '曹操', '刘备', '吕布'],
                  ])
b = ['貂蝉', '大乔', '小乔', '尚香', '阿丑']
pdwoman = pd.DataFrame(woman, index=b)
print(pdwoman)

sd = pd.Series()

while len(a) > 0:
    sset = sd.index
    pp = pdman.loc[a[0]]
    for i in list(pp):
        if i in sset:
            mmm = sd[i]
            po = pdwoman.loc[i]
            kl = list(po)
            p = kl.index(mmm)
            q = kl.index(a[0])
            if p<q:
                continue
            else:
                sd[i] = a[0]
                #sd.drop(k)
                a.remove(a[0])
                a.append(mmm)
                break
        else:
            sd[i] = a[0]
            a.remove(a[0])
            break

print(sd)