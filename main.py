import numpy as np
import torch

x = torch.tensor([1, 2, 3])
print(int(torch.argmax(x).data.numpy()))