#!/bin/bash

my_app=flask_mio
sudo docker build -t ${my_app} .
sudo docker run -d -p 5000:5000 --name=${myapp} --link redis:redis -v $PWD:/pers ${my_app}
