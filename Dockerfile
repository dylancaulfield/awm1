##
##
# Start from an existing image with Python 3.8
FROM python:3.8

SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
      apt-get -y install sudo

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
RUN chmod +x Miniconda3-py39_4.12.0-Linux-x86_64.sh && ./Miniconda3-py39_4.12.0-Linux-x86_64.sh -b -p ~/miniconda
COPY env.yml /usr/src/app



RUN echo ". ~/miniconda/etc/profile.d/conda.sh" >> ~/.bashrc
RUN source ~/.bashrc
RUN conda.sh init

RUN conda.sh config --add channels conda-forge
RUN conda.sh config --set channel_priority strict
RUN conda.sh config --set channel_priority strict
RUN conda.sh create --name env gdal=3.4.3 pyproj requests psycopg2 requests django django-cors-headers djangorestframework-gis djangorestframework

RUN conda.sh activate env

COPY . /usr/src/app
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "8001"]
