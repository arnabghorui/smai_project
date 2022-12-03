# Multilingual News Article Similarity
### Team No. 54
### Project for the course Statistical Methods in AI

- ## Task and Data:
    Here we have Attempted SemEval 2022 Task 8: Multilingual News Article Similarity. Given two news articles, our task is to find out whether they are covering the same story or not, and to come up with a similarity score for the same. The rating scale for similarity is used as 4 for most similar and 1 for least similar articles. 

    The data is provided in a csv file. News articles are given pairwise, with there original links and internet archive links. Here for each pair of news articles similarity scores of coutry, entity, time etc  are provided. [Source](https://competitions.codalab.org/my/datasets/download/8379dc75-c824-4ea7-bf00-9d29cb644af5).

    -### Data Extraction:
        First we crawled the data using a bot suggested by the paper. We accumulated all the data in a single json file, which is a list of dict.
        Each dict is a news article pair with a pair of text, score, etc. as given in dataPrepare.py

- ## System Description
    ![flowchart diagram drawio](https://user-images.githubusercontent.com/61308067/201865396-e5cfcd4f-07fa-47dd-9233-5e40674f6317.svg)
    We used a Siamese based architecture to detect the similarity between two news articles as given in the image.
    We implemented 3 major models on this architecture:
    - Multilayer Perceptron using tf-idf
    - LSTM using glove encodings
    - Transformer - DistilBERT
    The details can be found in the report 
    
- ## Experiments
    We did 10 experiments as following:
    - MLP with Tf-Idf (MLP_English_Overall.ipynb)
    - MLP with Tf-Idf concatenated as [X1+X2, X1-X2] (MLP_English_Overall.ipynb)
    - MLP with Tf-Idf and MultiLable learning (MLP_Multilabel.ipynb)
    - MLP with Tf-Idf MultiLingual (MLP_Multilingual.ipynb)
    - LSTM with Glove Embedding (LSTM_English_Overall .ipynb)
    - LSTM with Glove Embedding concatenated as [X1+X2, X1-X2] (LSTM_English_Overall .ipynb)
    - LSTM with Glove Embedding and MultiLable learning (LSTM_multilable.ipynb .ipynb)
    - DistilBERT-base--cased as encoder (DistilBERT_English_Overall.ipynb)
    - DistilBERT-base-multilingual-cased as encoder (DislitBERT_Multilingual.ipynb)
    - DistilBERT-base-multilingual-cased as encoder  and MultiLable learning (DislitBERT_Multilabel.ipynb)
    
    Details of Experiments and results are in the Report

- ## Result:
    We got the best result on unilingual setting with MLP using Multilable training where
the test MSE was 1.31 , and PCC was 0.2817. We got the best result on multilingual setting with DistilBERT
where the test MSE was 0.5113 , and PCC was 0.5683.
