import torch
import  torch.nn.functional as F
a = torch.tensor([1,2,3,4,5]).reshape(1,5)
n = 8
b = F.one_hot(a,n)
print(a.T)