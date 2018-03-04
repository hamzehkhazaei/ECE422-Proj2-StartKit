ECE 422 Instructions - Winter 2018
================
First of all you need to create 3 VMs on Cybera cloud with the following specefications:
1. Use **Ubuntu 16.04** as the image for all VMs.
2. You need one of these VMs to run the client program for which you may use **m1.small** flavour.
   - You will run the  `ece422_client.py`  on this VM. 
   - Note this is a base implementation of the client and you may modify this according to your needs.
3. For the other two VMs **m1.large** flavor would be a good choice. These two VMs will construct your Swarm cluster.
4. You need to open the following TCP ports in the default security group in Cybera:
   - 22 (ssh), 2376 and 2377 (for Swarm), 5000 (Visualization), 8000 (webapp), 6379 (for Redis)
   - You can do this on Cybera by going to *Network* menu and *Security Groups*.
5. For the VM that you want to make it your Swarm Manger you need to run the following commands:
```bash
sudo apt-get update 
sudo apt-get -y install docker.io
sudo docker swarm init
```

