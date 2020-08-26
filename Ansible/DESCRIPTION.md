## install_ansible.sh
- Used to install the following:
    - ` aptitude ` : Ansible prefers to use this over apt or apt-get (though it can use apt as well).
    - ` dialog ` : A simple utility for creating interactive dialogues in the command line.
    - ` ansible ` : The real deal.

## Define the hosts

Ansible uses a hosts file that contains a list of all the hosts you might want to connect with and manage. If you were just using Ansible to manage your own machine, then you would just need one `local` entry, but if you want to manage remote machines, you can add their SSH connection details in this file `hosts.yml` file.
```
all:
  hosts:
    local:
      ansible_host: 127.0.0.1
      ansible_connection: local
    wintel0:
      ansible_host: 192.168.1.121
    wintel1:
      ansible_host: 192.168.1.142
    ybox-vm:
      ansible_host: 192.168.1.128
```

## Playbooks and Roles
Ansible's main "unit of work" is the playbook. This is a single YAML file (keep at least one playbook per physical machine that I want to keep set up or up to date). <br>
Sometimes when there's a cluster of machines that all need the same setup, a host group can be added to the hosts.yml and a single playbook used that target all of them. <br>
Ansible has another level of hierarchy called Roles. Use Roles for the individual things that a particular playbook needs to do, for example set up a single software package.

## Run Output example
```
$ ansible-playbook playbooks/machine-wintel0.yml -i hosts.yml -K --ask-pass
SSH password:
BECOME password[defaults to SSH password]:

PLAY [wintel0] ****************************************************

TASK [Gathering Facts] ****************************************************
ok: [wintel0]

TASK [include_role : software-common-apt] *********************************

TASK [software-common-apt : Installing Common Apt packages] ***************
ok: [wintel0]

TASK [include_role : software-python] *************************************

TASK [software-python : Installing Python 3.8] ****************************
ok: [wintel0]

TASK [software-python : Install stuff that ansible needs] *****************
ok: [wintel0]

TASK [include_role : software-docker] *************************************

TASK [software-docker : Ensure built-in docker is removed] ****************
ok: [wintel0]

TASK [software-docker : Install docker GPG] *******************************
ok: [wintel0]

TASK [software-docker : Install docker apt repository] ********************
ok: [wintel0]

TASK [software-docker : Install docker-ce] ********************************
ok: [wintel0]

TASK [software-docker : Install dependencies] *****************************
ok: [wintel0]

TASK [software-docker : Install Python docker package] ********************
ok: [wintel0]

TASK [software-docker : Check if docker-compose is installed] *************
ok: [wintel0]

TASK [software-docker : Check docker-compose version] *********************
ok: [wintel0]

TASK [software-docker : Install docker-compose] ***************************
skipping: [wintel0]

TASK [software-docker : Check if docker-credential-helper is installed] ***
ok: [wintel0]

TASK [software-docker : Check docker-credential-helper version] ***********
ok: [wintel0]

TASK [software-docker : Install docker-credential-helpers] ****************
ok: [wintel0]

TASK [software-docker : Remember to add docker group to users!] ***********
ok: [wintel0] => {
    "msg": "Remember to add docker groups to users with \"usermod -aG docker <username>\". Use \"newgrp docker\" to use the group immediately"
}

PLAY RECAP ****************************************************************
wintel0: ok=16   changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```