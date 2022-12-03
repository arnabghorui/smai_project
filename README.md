# Multilingual News Article Similarity
### Team No. 54
### Project for the course Statistical Methods in AI

## Task and Data:
    Here we have Attempted SemEval 2022 Task 8: Multilingual News Article Similarity. Given two news articles, our task is to find out whether they are covering the same story or not, and to come up with a similarity score for the same. The rating scale for similarity is used as 4 for most similar and 1 for least similar articles. 

    The data is provided in a csv file. News articles are given pairwise, with there original links and internet archive links. Here for each pair of news articles similarity scores of coutry, entity, time etc  are provided. [Source](https://competitions.codalab.org/my/datasets/download/8379dc75-c824-4ea7-bf00-9d29cb644af5).

### Data Extraction:
    First we crawled the data using a bot suggested by the paper. We accumulated all the data in a single json file, which is a list of dict.
    Each dict is a news article pair with a pair of text, score, etc. as given in dataPrepare.py

## System Description
    ![flowchart diagram drawio](https://user-images.githubusercontent.com/61308067/201865396-e5cfcd4f-07fa-47dd-9233-5e40674f6317.svg)
    We used a Siamese based architecture to detect the similarity between two news articles as given in the image.
    We implemented 3 major models on this architecture:
    - Multilayer Perceptron using tf-idf
    - LSTM using glove encodings
    - Transformer - DistilBERT

- ## Model:
    We implemented multi layer perceptron this task.
    To be precise we used a siamese architecture with dence layers, as given in the model figure.
    

- ## Result:
    We got a test result of 
    mean_squared_error =
    mean_absolute_error =
    r2_score =
