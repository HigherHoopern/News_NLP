# News_NLP

## Section 1:   NewsApp.ipynb demonstrates how to use `news-nlp` pacakge

1. download this dataset and save it under `./News_NLP/data`

`https://drive.google.com/file/d/1oAxSyq1T9ZEpaoeBzzfzsXelYph-7IX6/view?usp=share_link`

2. Suggect to run it in conda virtual environment named news_nlp

   `conda create -n news_nlp python=3.10 -y`

`conda activate news_nlp`

3. install dependcies

`pip install scikit-learn`

`pip install mediacloud-cliff`

`pip install ipywidgets`

install scaCy en_core_web_lg
`python -m spacy download en_core_web_lg`

install cliff docker image to geoloate text data in terms of lan, lon, popualtion, location name, location type etc

   `docker pull rahulbot/cliff-clavin:2.6.1`

   `docker run -p 8080:8080 -m 8G -d  --name cliff rahulbot/cliff-clavin:2.6.1`

where `cliff` is the name of container

4. install News_NLP `pip install news-nlp`

# Section 2: Docker Image

(no need to config development environment)

1. https://hub.docker.com/repository/docker/zhenxianlu/news-nlp-amd64/general
2. download docker image `docker pull zhenxianlu/news-nlp-amd64:latest`
3. check local images `docker images`
4. start this image `sudo docker run -itd --name news-nlp zhenxianlu/news-nlp-amd64:latest  /bin/bash` where `news-nlp` is to name the contianer
5. check running containers `sudo docker ps`
6. keep container running `sudo docker attach news-nlp`
7. create bridge network to connect `news-nlp` container with `cliff` container
   `sudo docker network create -n my-net`  create a bridge named my-net
   `sudo docker network connect my-net news-nlp`
   `sudo docker network connect my-net cliff`
8. check the IPs of the contianers connected to `my-net`
   `sudo docker network inspect my-net`
   copy the IP of container `cliff` for future use, it should something like that `172.**.*.*`
9. Enter container `sudo docker container attach new-nlp`
10. Enter foler  `cd News_NLP/`
11. Open `geolocator.py` by `vim` and amend the line `my_cliff = Cliff('http://0.0.0.0:8080')` as `my_cliff = Cliff('http://172.**.*.*:8080')`
12. Back to parent folder `cd ..`
13. Excute `pyhton main.py`
14. Additonally, copy file from  container to host on the terminal of host
    `sudo docker cp nlp:/NewsApp/News_NLP/data/new_data.csv /host/path/target`
