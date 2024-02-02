#!/bin/bash
echo "Installing dependency packages"

#yum -y install python3-devel gdal gdal-devel numpy mpich mpich-devel mpich-autoload
yum -y install python3-devel gdal gdal-devel numpy

wget https://repo.continuum.io/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh
mkdir /opt/miniconda3
chmod +x Miniconda3-py37_4.10.3-Linux-x86_64.sh
./Miniconda3-py37_4.10.3-Linux-x86_64.sh -b -u -p /opt/miniconda3
rm -f Miniconda3-py37_4.10.3-Linux-x86_64.sh
echo 'export PATH=/opt/miniconda3/bin:$PATH:/home' >> /etc/profile
chmod -R +r /opt/miniconda3
chmod -R +x /opt/miniconda3

export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
export PATH=/opt/amazon/openmpi/bin/:$PATH

sudo -u ec2-user python3 -m pip install --upgrade pip setuptools wheel
sudo -u ec2-user python3 -m pip install numpy
sudo -u ec2-user python3 -m pip install "setuptools<58.0"
sudo -u ec2-user --preserve-env=CPLUS_INCLUDE_PATH,C_INCLUDE_PATH python3 -m pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')
sudo -u ec2-user python3 -m pip install tqdm
sudo -u ec2-user env PATH=$PATH python3 -m pip install mpi4py

