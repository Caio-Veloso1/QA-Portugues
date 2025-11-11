FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
WORKDIR /qagnn
RUN apt-get update && apt-get install -y \
    wget \
    automake \
    build-essential \
    curl \
    vim \
    htop \
    nano \
	&& rm -rf /var/lib/apt/lists/*
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

COPY . .
 



