Following, Text Pre-processing in the previous phase which contained steps like: 

Tokenization: It is the process of dividing a text into smaller units (each word will be an index in an array)

Lemmatization: It removes the endings of the word to the root word. It reduces the word children to a child.

Stop words Removal: Words like the and for will be eliminated from our dataset because they take too much room.In this phase, after text pre-processing, we have vectorized the data and applied TF-IDF. 

we vectorized and applied TF-IDF. We performed this step, to get predictions based on the text from our model, we need to encode it in vector format then it is processed by the machine. For our project, We used TfIdf Vectorizer to convert our text strings (text, title and subject columns) to numerical representations and initialize a PassiveAgressive Classifier to fit the model. In the end, the accuracy score and confusion matrix tell us how well our model works.

![image](https://user-images.githubusercontent.com/98927072/169704574-125aedeb-e29c-4249-acf3-1d45da106bed.png)
 
The passive-aggressive algorithms are a family of algorithms for large-scale learning. Intuitively, passive signifies that if the classification is correct, we should keep the model, and, aggressive signifies that if the classification is incorrect, update the model to adjust to more misclassified examples. Unlike most others, it does not converge, rather it makes updates to correct the loss.

Post which, since this is a classification problem =, meaning , the task is the classify fake news from real news, we have implemented a set of Classification Machine Learning Algorithms after dividing the training and testing data into 80 : 20 ratio. 

The algorithms we have implemented for our projec are as follows : 

1. Logistic regression.
2. Decision Tree Classifier.
3. Randomn Forest Classifier and 
4. Gradient Boost Algorithm. 
 
 
 
 
 
To improve the model performance, we plan to : 

Train the models on a large dataset.
Tweak hyperparameters of the model.
