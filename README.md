ECE 422: Reliable and Secure Systems Design -- Winter 2018 
=============
Starter Kit for Reliability Project 
-----
First of all you need to create 3 VMs on Cybera cloud with the following specefications:
1. Use **Ubuntu 16.04** as the image for all VMs.

2. You need one of these VMs to run the client program for which you may use **m1.small** flavor. Let's call this VM as
the *clientVM*.

3. For the other two VMs, **m1.large** flavor would be a good choice. These two VMs will construct your Swarm cluster.

4. You need to open the following TCP ports in the default security group in Cybera:
   - 22 (ssh), 2376 and 2377 (for Swarm), 5000 (Visualization), 8000 (webapp), 6379 (for Redis)
   - You can do this on Cybera by going to *Network* menu and *Security Groups*.
   
5. For the VM that you want to be your Swarm Manger you need to run the following commands:
    ```bash
    $ sudo apt-get update 
    $ sudo apt-get -y install docker.io
    $ sudo docker swarm init
    ```
6. The above _init_ command will output something like following that you need to run on your another VM 
(ie the Swarm Worker):
    ```bash
    $ docker swarm join \
        --token SWMTKN-1-3pu6hszjas19xyp7ghgosyx9k8atbfcr8p2is99znpy26u2lkl-1awxwuwd3z9j1z3puu7rcgdbx \
        172.17.0.2:2377
    ```
    - Above command will join your worker to the Swarm cluster.
7. Login into your Swarm manager and download the docker-compose.yml file as follow:
    ```bash
    $ wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/docker-compose.yml
    ```
8. Run the following to deploy your application:
    ```bash
    $ sudo docker stack deploy --compose-file docker-compose.yml demo
    ```
9. Your application consists of three microservices:
    1. A visualization microservice that is used to show the Swarm cluster nodes and microservices that are running on
    the cluster. Open `http://swarm_manager_ip:5000` in your browser. Note that you should have the Cybera VPN client 
    running in order to see the page.
    2. The web application which is linked to a Redis datastore. This simple application shows the number that it has 
    been visited and the time that took it to solve a hard problem. 
        1. Open `http://swarm_manager_ip:8000` to see the web application. Try to refresh the app. You should see the 
        hitting number increase one by one.
    3. Redis microservice which in fact doesnt do anything special and just return the number of hitting.

10. Now, login into your **clientVM** and download the client program code:
    ```bash
    $ wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/ece422_client.py
    ```
    - Note this is a base implementation of the client and you need to modify this according to your needs.
    - This client program create a number of users that send requests to the server and after receiving the respose
     think for the amount of **think_time* and send another request.
    - It calculates the *response time* for each request as well.
    - If we increase the number of users, the response time is expected to increase.
    - **Important Note**: try not to run the client on your laptop as this may appears to a DoS attack to Cybera 
    firewall and brings about complicated situation for us. 