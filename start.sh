#/bin/bash

sudo docker build -t kamontia/autokenpos . --no-cache
sudo docker run -itd --name kenpos kamontia/autokenpos
