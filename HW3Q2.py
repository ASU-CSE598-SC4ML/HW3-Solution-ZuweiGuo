import crypten
import torch
import numpy as np

import crypten.mpc.primitives.binary as binary

crypten.init()

//random code m0, m1

m0 = np.rand.randint(2,size=10)
m0 = m0.join("")
m1 = np.rand.randint(2,size=10)
m1 = m1.join("")

//let alice has score 10 and bob has threshold 20 

alice = torch.tensor(10)
bob = torch.tensor(20)

//encrypt the value of Alice and Bob
alice_enc = crypten.cryptensor(alice)
bob_enc = crypten.cryptensor(bob)


//convert the value to BinarySharedTensor
alice_enc_b = binary.BinarySharedTensor(alice_enc)
bob_enc_b = binary.BinarySharedTensor(bob_enc)

//compare a and b using gt function and store value to u, compute v = 1 - u
u = binary.gt(alice_enc_b, bob_enc_b)
v = crypten.cryptensor(torch.tensor(1)) - u

c = u*crypten.cryptensor(m0) + v*crypten.cryptensor(m1)
//alice get the code
alice_c = c.get_plain_text()



