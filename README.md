# News_NLP

Suggect to run it in conda virtual environment named news_nlp
`conda create -n news_nlp python=3.10 -y`
`conda activate news_nlp`

`pip install scikit-learn`
`pip install mediacloud-cliff`
`pip install ipywidgets`

install scaCy en_core_web_lg
`python -m spacy download en_core_web_lg`

1. install cliff docker image to geoloate text data in terms of lan, lon, popualtion, location name, location type etc
   `docker pull rahulbot/cliff-clavin:2.6.1`
   `docker run -p 8080:8080 -m 8G -d rahulbot/cliff-clavin:2.6.1`
   
2. install News_NLP `pip install news-nlp`

3. `TestNoteBook.ipynb` demonstrates how to use News_NLP pacakge

