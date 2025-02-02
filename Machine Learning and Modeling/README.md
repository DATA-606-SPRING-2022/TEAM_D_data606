Following, Text Pre-processing in the previous phase which contained steps like: 

Tokenization: It is the process of dividing a text into smaller units (each word will be an index in an array)

Lemmatization: It removes the endings of the word to the root word. It reduces the word children to a child.

Stop words Removal: Words like the and for will be eliminated from our dataset because they take too much room.In this phase, after text pre-processing, we have vectorized the data and applied TF-IDF. 

we vectorized and applied TF-IDF. We performed this step, to get predictions based on the text from our model, we need to encode it in vector format then it is processed by the machine. For our project, We used TfIdf Vectorizer to convert our text strings (text, title and subject columns) to numerical representations and initialize a PassiveAgressive Classifier to fit the model. In the end, the accuracy score and confusion matrix tell us how well our model works.

![image](https://user-images.githubusercontent.com/98927072/169704574-125aedeb-e29c-4249-acf3-1d45da106bed.png)
 
The passive-aggressive algorithms are a family of algorithms for large-scale learning. Intuitively, passive signifies that if the classification is correct, we should keep the model, and, aggressive signifies that if the classification is incorrect, update the model to adjust to more misclassified examples. Unlike most others, it does not converge, rather it makes updates to correct the loss.

Post which, since this is a classification problem , meaning , the task is the classify fake news from real news, we have implemented a set of Classification Machine Learning Algorithms after dividing the training and testing data into 80 : 20 ratio. For this project, we built a pipeline as well. 

The algorithms we have implemented for our projec are as follows : 

1. Logistic regression.
2. Decision Tree Classifier.
3. Randomn Forest Classifier and 
4. Gradient Boost Algorithm. 

After training the models with Train data, we tried to quantify the quality of our model’s predictions by analyzing the Accuracy, Precision, Recall, F-1 Score, AUC etc. By looking at there metrics, we would be able to answer questions like:

1. Is our model accurate enough to put into production
2. Will a larger training set improve my model’s performance?
3. Is my model under-fitting or over-fitting?
4. Will a larger training set improve my model’s performance?
5. Is my model under-fitting or over-fitting?

From our analysis, we found that Gradient Boost is out performing all the other algorithms and this makes sense as Gradient boosting trees can be more accurate because we train them to correct each other's errors, they're capable of capturing complex patterns in the data. However, if the data are noisy, the boosted trees may overfit and start modeling the noise.
 
For future scope, To improve the model performance, we plan to : 

1. Train the models on a large dataset.
2. Tweak hyperparameters of the model.
