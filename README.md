ECE 422: Reliable and Secure Systems Design 
=============
This repository provides the starter kit for the Reliability project. The `docker-images` folder
contains the Dockerfile, a simple application in `Python` and a requirement file including dependencies for
the application. This directory is for your information and reference as the image (simpleweb) has already been build 
and pushed to [Docker Hub](https://hub.docker.com/r/henaras/simpleweb) repository.

Following steps show how you can prepare the deployment environment on Cybera Cloud; briefly you need to a) provision 
Virtual Machines (VMs) on Cybera b) install Docker on VMs c) create a Swarm cluster of at least two of 
VMs and d) deploy a web application on the Swarm cluster as microservices.

Also this repository contains a base implementation of an HTTP client program that may be customized or extended 
according to your needs. 

Initial steps to accomplish your project:   

1. Create 3 VMs on Cybera cloud with the following specefications:

    1. Use `Ubuntu 16.04` as the image for all VMs.

    2. You need one of these VMs to run the client program for which you may use `m1.small` flavor. Let's call this VM as
the `Client_VM`.

    3. For the other two VMs, `m1.large` flavor would be a good choice. These two VMs will construct your Swarm cluster.

    4. You need to open the following TCP ports in the `default security group` in Cybera:
        - 22 (ssh), 2376 and 2377 (Swarm), 5000 (Visualization), 8000 (webapp), 6379 (Redis)
        - You can do this on Cybera by going to `Network` menu and `Security Groups`. ([See Here](./figures/sg.png))

2. On the `Client_VM` run
    ```bash
    $ sudo apt -y install python-pip
    $ pip install requests
    ```

2. Then, you need to install *Docker* on VMs that constitutes your Swarm Cluster. Run the followings on each node.
    ```bash
    $ sudo apt update
    $ sudo apt -y install docker.io
    ```
    
3. Now that Docker is installed on the two VMs, you will create the Swarm cluster.
    1. For the VM that you want to be your Swarm Manger run:
    ```bash
    $ sudo docker swarm init
    ```

    2. The above `init` command will produce something like bellow command that you need to run on all worker nodes.
    ```bash
    $ docker swarm join \
        --token xxxxxxxxxxxxxxxxxx \
        swarm_manager_ip:2377
    ```
    3. Above command will join your worker to the Swarm cluster.
5. On your Swarm manager, download the docker-compose.yml file:
    ```bash
    $ wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/docker-compose.yml
    ```
6. Run the following to deploy your application:
    ```bash
    $ sudo docker stack deploy --compose-file docker-compose.yml app_name
    ```
7. Your deployed application should includes three microservices:
    1. A visualization microservice that is used to visualize the Swarm cluster nodes and the running microservices. 
        - Open `http://swarm_manager_ip:5000` in your browser. Note that you should have the Cybera VPN client 
    running in order to see the page. ([Sample](./figures/vis.png))
    2. A web application which is linked to a Redis datastore. This simple application shows the number that it has 
    been visited and the period that took it to solve a hard problem. 
        - Open `http://swarm_manager_ip:8000` to see the web application. Try to refresh the page. You should see the 
        hitting number increases one by one and also the computation time to change each time. ([Sample](./figures/app.png))
    3. A Redis microservice which in fact doesnt do anything fancy but to return the number of hitting.

8. Now, login into your `Client_VM` and download the http client program:
    ```bash
    $ wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/http_client.py
    ```
9. Then run the `http_client.py` program with one user who sends a request, wait for response, when received the 
    response would think for one second, and then send another request. This cycle goes on as long as the client 
    program is running.
    ```bash
    $ python3.5 http_client.py swarm_manager_ip 1 1
    ```
    1. The program should print the response time for each request.
    2. Generally, this client program creates a number of users that send requests to the server and after receiving 
    the response thinks for the amount of `think_time` and then send a new request.
    3. If you increase the number of users or decrease the think time, ie increasing the workload, the response 
    time should increase.
    4. **Important Note**: for development and testing purposes you may want to run the client program on your laptop 
    which is a reasonable strategy. However, running the client program for a long time on your laptop might appear as 
    a DoS attack to Cybera firewall which may result in unexpected outcome for your VMs. Therefor, try to run the 
    http client program on the `Client_VM`.
    
    
 Good Luck!