ECE 422: Reliable and Secure Systems Design 
=============
This repository provides the starter kit of reliability project. The *docker-images* folder
contains the Dockerfile, a simple application in `Python` and a requirement file including dependencies for
the application. This directory is for students reference as the image (simpleweb) has already been build 
and pushed to [Docker Hub](https://hub.docker.com/r/henaras/simpleweb) repository.

Following steps show how students can prepare the deployment environment on Cybera Cloud; briefly, 1) a number
of Virtual Machines (VMs) will be provisioned 2) Docker will be installed; 3) a Swarm cluster is created of 
at least two of VMs and 4) a simple web application will be deployed on the Swarm cluster as microservices.

Also this repository contains a base HTTP client program that may be customized or extended as one of the 
final project deliveries. Following are the initial steps to accomplish your project:   


1. Create 3 VMs on Cybera cloud with the following specefications:

    1. Use **Ubuntu 16.04** as the image for all VMs.

    2. You need one of these VMs to run the client program for which you may use **m1.small** flavor. Let's call this VM as
the *clientVM*.

    3. For the other two VMs, **m1.large** flavor would be a good choice. These two VMs will construct your Swarm cluster.

    4. You need to open the following TCP ports in the default security group in Cybera:
        - 22 (ssh), 2376 and 2377 (Swarm), 5000 (Visualization), 8000 (webapp), 6379 (Redis)
        - You can do this on Cybera by going to *Network* menu and *Security Groups*. ([See Here](./figures/sg.png))

2. Then, you need to install *Docker* on VMs that are part of your Swarm Cluster. Run the followings on each node.
    ```bash
    $ sudo apt-get update
    $ sudo apt-get -y install docker.io
    ```
    
3. Now that Docker is installed on the two VMs, you will create the Swarm cluster. 
    6. For the VM that you want to be your Swarm Manger you need to run:
   ```bash
   $ sudo docker swarm init
   ```

4. The above _init_ command will produce something like following command that you need to run on all worker nodes.
    ```bash
    $ docker swarm join \
        --token xxxxxxxxxxxxxxxxxx \
        swarm_manager_ip:2377
    ```
    - Above command will join your worker to the Swarm cluster.
5. SSH to your Swarm manager and download the docker-compose.yml file:
    ```bash
    $ wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/docker-compose.yml
    ```
6. Run the following to deploy your application:
    ```bash
    $ sudo docker stack deploy --compose-file docker-compose.yml demo
    ```
7. Your application consists of three microservices:
    1. A visualization microservice that is used to show the Swarm cluster nodes and running microservices. 
        - Open `http://swarm_manager_ip:5000` in your browser. Note that you should have the Cybera VPN client 
    running in order to see the page. ([Sample](./figures/vis.png))
    2. The web application which is linked to a Redis datastore. This simple application shows the number that it has 
    been visited and the time that took it to solve a hard problem. 
        - Open `http://swarm_manager_ip:8000` to see the web application. Try to refresh the app. You should see the 
        hitting number increase one by one and also the computation time to change accordingly. ([Sample](./figures/app.png))
    3. Redis microservice which in fact doesnt do anything special and just return the number of hitting.

8. Now, login into your **clientVM** and download the http client program:
    ```bash
    $ wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/http_client.py
    ```
    - Note this is a base implementation of an HTTP client and you need to modify this according to your needs.
    - This client program creates a number of users that send requests to the server and after receiving the response
     thinks for the amount of *think_time* and then send another request.
    - It calculates the *response time* for each request as well.
    - If you increase the number of users or decrease the think time, the response time should increase.
    - **Important Note**: try not to run the client on your laptop as this may appear as a DoS attack to Cybera 
    firewall which may result in unexpected outcome for your VMs. 
    
 Good Luck!