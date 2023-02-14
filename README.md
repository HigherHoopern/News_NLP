# Global Geopolitical Risk Index Project

(`pip install news-nlp`)   https://pypi.org/project/news-nlp/

This project `(GPR)` aims to measure country-level Geopolitical Risk (GPR) based on news data. This risk index consists of seven predefined components, including Conflict, Terror Threat, Corruption, Environment, Social, Governance (ESG) and foreign policy. This project covers:

1. identifying search terms (key words and biagrams) using NLP TF-IDF method and word embedding model
2. an unsupervised clustering model (K-means) to categorise search terms into five groups
3. an NLP deep learning model to classify news articles into the predefined topics;
4. an hierarchy statistical model to infer news event location at country level and
5. an multiple geolocator in terms of longitude, latitude, and population
6. a supervised sentiment classifier to categorize GPR news articles into three classes.

- __News\_NLP__
  - [README.md](README.md)
  - __Utilities__

    - [ClassificationReport.py](Utilities/ClassificationReport.py)
    - [\_\_init\_\_.py](Utilities/__init__.py)
    - [binary\_roc\_curve.py](Utilities/binary_roc_curve.py)
    - [ff\_confusion\_matrix.py](Utilities/ff_confusion_matrix.py)
    - [multiclass\_roc.py](Utilities/multiclass_roc.py)
    - [num\_news\_source.py](Utilities/num_news_source.py)
    - [num\_of\_words.py](Utilities/num_of_words.py)
    - [similarity.py](Utilities/similarity.py)
  - __data__

    - [GPRI\_barchart.png](data/GPRI_barchart.png)
    - [GPR\_index.png](data/GPR_index.png)
    - [PolRisk\_data.csv](data/PolRisk_data.csv)
    - [SampleNews.csv](data/SampleNews.csv)
  - __notebooks__

    - [NewsAPP.ipynb](notebooks/NewsAPP.ipynb)
    - [News\_Analysis\_V5.ipynb](notebooks/News_Analysis_V5.ipynb)
    - [News\_Classification\_Implement\_model.ipynb](notebooks/News_Classification_Implement_model.ipynb)
    - [News\_Classification\_in\_DL.ipynb](notebooks/News_Classification_in_DL.ipynb)
    - [Terror\_KW\_Bigram\_Analysis.ipynb](notebooks/Terror_KW_Bigram_Analysis.ipynb)
    - [Unified\_News\_Classification\_V2.ipynb](notebooks/Unified_News_Classification_V2.ipynb)
    - [readme.txt](notebooks/readme.txt)


## Section 1:   Usage of `news-nlp` pacakge

The notebook `NewsApp.ipynb` is to demonstrate the usage of ` news-nlp` Python package.

1. download sample news dataset from ` data` folder
2. Suggect to run it in conda virtual environment named news_nlp

   `conda create -n news_nlp python=3.10 -y`

`conda activate news_nlp`

3. install dependcies

`python -m spacy download en_core_web_lg`

install cliff docker image to geoloate text data in terms of lan, lon, popualtion, location name, location type etc

   `docker pull rahulbot/cliff-clavin:2.6.1`

   `docker run -p 8080:8080 -m 8G -d  --name cliff rahulbot/cliff-clavin:2.6.1`

where `cliff` is the name of container

4. install News_NLP `pip install news-nlp`

## Section 2: Docker Image

(no need to config development environment)

1. `https://hub.docker.com/repository/docker/zhenxianlu/news-nlp-amd64/general`
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
9. Enter container `sudo docker container attach news-nlp`
10. Enter folder  `cd News_NLP/`
11. Open `geolocator.py` by `vim` and amend the line `my_cliff = Cliff('http://0.0.0.0:8080')` as `my_cliff = Cliff('http://172.**.*.*:8080')`
12. Back to parent folder `cd ..`
13. Excute `pyhton main.py`
14. Additonally, copy file from  container to host on the terminal of host
    `sudo docker cp nlp:/NewsApp/News_NLP/data/new_data.csv /host/path/target`
