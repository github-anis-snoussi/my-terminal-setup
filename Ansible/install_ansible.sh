#!/bin/bash

# install ansible ppa
apt-add-repository ppa:ansible/ansible -y

# install stuff
apt update
apt install -y aptitude ansible dialog