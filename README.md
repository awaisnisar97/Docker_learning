Project overview: The purpose of this project was to create a multi container application consisting of a Python Flask web application and a Redis database. The Flask application uses Redis to store and retrieve data, demonstrating container communication using Docker Compose.

Requirements: 
            - The flask web application must have two routes
             
               1) /: displays a welcome message 
               2) :/count displays the number of times you visited the application and stores it in redis 

            - Redis database: use as a key value store to keep track of the visit count 
           
            - Dockerize both services 
               1)create dockerfiles for both applications (redis and flask)
               2)Use docker compose to manage the multi container application

            - Test the application using your browser and entering http://localhost:5002 to see the welcome message and http://localhost:5002/count to see the number of times you have visited 


Learning points = I learnt how to create a multi container application, use docker compose to manage multiple services and practiced using common docker commands such as docker compose up, docker ps, docker images, docker volume ls, 

Troubleshooting = One of the main challenges I encountered was YAML syntax and indentation errors within Docker Compose files. These issues highlighted the importance of correct spacing and formatting when working with configuration files.

Improvements made = In the current application setup, redis had no way of storing how many times you visited the application and instead each time the container was shut down and recreated the count started from 0. The redis-data volume is mounted to Redis’s /data directory, allowing Redis to persist its database files even when containers are removed or recreated. As a result, the visit counter is retained between deployments.
