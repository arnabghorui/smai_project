# Statistical Methods in AI
Project for the course Statistical Methods in AI

- ## Task:
    Given two news articles, our task is to find out whether they are covering the same story or not, and to come up with a similarity score for the same. For our task we have taken the news article pairs of the same language i.e English. But in principle this can be done in cross language also. The rating scale for similarity is used as 4 for most similar and 1 for least similar articles. 



- ## Data:
    The data for this project was obtained from 

- ## Data Extraction:
First we accumulated all the data in a single json file, which is a list of dict. Each dict is a news article pair with a pair of text, score, etc. as given in dataPrepare.py

- ## Feature extraction:
We made feature vectors from the data.
We used tf-idf vectorization for this purpose as given in SMAI_Projrct.ipynb . 

- ## Model:
We implemented multi layer perceptron this task.
To be precise we used a siamese architecture with dence layers, as given in the model figure.

- ## Result:
We got a test result of 
