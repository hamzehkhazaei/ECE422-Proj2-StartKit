ECE 422 Instructions - Winter 2018
================
First of all you need to create 3 VMs on Cybera cloud with the following specefications:
1. Use **Ubuntu 16.04** as the image for VMs.
2. You need one of these VMs to run the client program for which you may use **m1.small** flavour.
    2. You will run the  `ece422_client.py`  on this VM. Note this is a base implementation of the client and you may
    modify this according to your needs.
3. For the other two VMs **m1.large** flavor would be a good choice. These two VMs will construct your Swarm cluster.
4. You need to open the following TCP ports in the default security group in Cybera:
    5. 22(ssh), 2376, 2377, 5000, 8000, 6379
    6. You can do this by going to your profile on Cybera then under *Network* look for *Security Groups*.
