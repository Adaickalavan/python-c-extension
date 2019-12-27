# Base image
FROM python:3.7.5 AS buildstage

LABEL Author Adaickalavan

# RUN apt-get update -y  
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get -y install \
    python-pip \
    cmake \
    pkg-config \
    libopenmpi-dev

# Change working directory
WORKDIR /src

COPY ./requirements.txt .

# Use pip to install requirements
RUN pip install -r /src/requirements.txt

# Copy the current folder which contains source code to the Docker image
COPY . .

# Build the C library
RUN cd /src/lib/cpp/ && \
    cmake -E make_directory build && \
    cmake -E chdir ./build cmake -DCMAKE_BUILD_TYPE=Release .. && \
    cmake --build ./build