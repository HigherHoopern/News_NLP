# News_NLP

## Section 1:   NewsApp.ipynb demonstrates how to use `news-nlp` pacakge

1. download this dataset and save it under`./News_NLP/data`

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
   
   `docker run -p 8080:8080 -m 8G -d rahulbot/cliff-clavin:2.6.1`
   
4. install News_NLP `pip install news-nlp`


