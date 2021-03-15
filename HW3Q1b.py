import crypten
import torch

import crypten.mpc.primitives.binary as binary

crypten.init()

alice = torch.tensor(10)
bob = torch.tensor(5)

//encrypt the value of Alice and Bob
alice_enc = crypten.cryptensor(alice)
bob_enc = crypten.cryptensor(bob)


//convert the value to BinarySharedTensor
alice_enc_b = binary.BinarySharedTensor(alice_enc)
bob_enc_b = binary.BinarySharedTensor(bob_enc)

//compare a and b using gt function and print result of BinarySharedTensor object
compare_yao = binary.gt(alice_enc_b, bob_enc_b)
compare_yao



