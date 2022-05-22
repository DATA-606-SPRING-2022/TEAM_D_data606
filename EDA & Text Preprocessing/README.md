<h1> Fake News Classification and Prediction - Team D <h1>
  
  <h3> By Srikeerthi Upperla and Sushruth DT </h3>


_**PROJECT IDEA:**_

Fake news on social media and other forms of media is widespread, and it is a source of serious concern because it has the potential to cause significant social and national harm, as well as have debilitating effects on individuals and communities. It has long been recognized that the authenticity of information is a problem that affects businesses and society in general, and that this is true for both printed and digital media. It is reasonable to assume that the global economy bears a cost of at least $78 billion per year from a growing number of small costs associated with fake news and larger incidents. Fake news' dangers and costs will only increase as technology improves, despite the best efforts of law enforcement.
  
 Therefore, we want to build models using Machine Learning that classifies and Predicts Fabricated News. 


_**WE HAVE BEEN A VICTIM OF FAKE NEWS:**_

Personally, We've been a victim of fake news, particularly in the area of job rackets, where we received fake interview letters from recruiters claiming that if we paid up front, they would get me through the next rounds quickly, and the covid vaccination fiasco, where we were told that they were administering covid vaccine in a nearby government hospital, only to find out it was fake news and contract covid. Exam postponement is another example, as is fake news about the death of one of my favorite celebs.



_**THIS IS IMPORTANT TO US BECAUSE:**_

![image](https://user-images.githubusercontent.com/98927072/153283392-e9994172-1419-4541-9dc6-e5da6ef6f510.png)

The World Economic Forum ranks the spread of misinformation and fake news, as among the world’s top global risks. 
 
   o	**You deserve the truth : ** You are educated enough to make your own decisions based on the facts. 

   o	**False news erodes credibility : ** People will be less inclined to accept you if you base your arguments on incorrect data.

   o	**Fake news can harm you and others : ** Mercola.com and NaturalNews.com, for example, help promote misconceptions that HIV and AIDS are unrelated, or vaccines cause autism. These sites are dangerous and heavily trafficked.

   o	**Real news can help : ** If you wish to invest in a company, you should study factual articles about it. A voter should research a candidate thoroughly before casting a ballot to ensure that the candidate best represents his or her views. Real news may help you generate money and make the world a better place.




_**WE BELIEVE THAT:**_

It is an important skill to be able to distinguish between accurate news and fake news, and one that you will use for the rest of your life. Our research investigates various textual properties that can be used to distinguish between fabricated and authentic content. In order to take advantage of these characteristics, we train a combination of different machine learning algorithms using various ensemble methods, and then evaluate their performance on real-world datasets. It is our goal to distinguish between fake and true news by developing powerful classification models for the news data we have gathered so far. 

•	**Spot if next submission of author is fake or**

•	**Plan of Action : Extensive EDA of news**

•	**Suspicious titles that can be tagged to fake** 




_**UNIT OF ANALYSIS:**_

Here the unit of analysis is : Author / News organizations.


The sensationalism of not-so-accurate but eye-catching and intriguing headlines to retain audiences' attention to sell news has persisted throughout all sorts of information broadcast history, which, as conferred above, has many muted issues; thus, we would like to classify and predict fake news for which I plan to use the following models:

•	Logistic Regression


•	Multinomial Naïve Bayes


•	Passive aggressive classifier 


•	Support Vector Machine


•	Decision Trees


•	KNN

As the project aims to classify and predict Fake news, I would be considering this as more as a classification problem and thus would work on generating the Classification report that is used to measure the quality of predictions from a classification algorithm—the precision, AU- ROC, recall, F1 Score, and our trained classification model support. We plan to use visualization techniques to compare the performance and better understand each model's metrics.


_**TEAM RESPONSIBILITY:**_


Sri Keerthi - Team Captain

•	 Documentation

•	 Data EDA

•	 Data Cleanup

•	 Implementing Machine Learning Algorithms


Sushruth - Team Member

•	 Documentation

•	 Data EDA

•	 Data Cleanup

•	 Implementing Supervised classification algorithms and tuning 

  
_**REASON FOR PAIRING: **_
We became acquainted as mutual friends while assisting one of our mutual friends with her thesis psychology project on misinformation, which brought us together. And we were talking about how much it has immensely affected our personal lives as a result of this. We later discovered that we were enrolled in your Data 606 capstone course. Later, we came to the conclusion that we should collaborate and work on fake news detection.
  
<h1> EXPLORATORY DATA ANALYSIS </h1>
   
 In the exploratory Data Analysis phase, we have performed some initial investigations on the dataset to discover patterns and uncover hidden insights. Our aim was to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations. CHeck our our plots below. 
   

<h3> Insights from Data </h3>
   
 Checking distribution of Data: 
   
 ![image](https://user-images.githubusercontent.com/98927072/169607093-c6dbfafb-6fdf-4bad-a605-28d5b22a4740.png)
   
 
 ![image](https://user-images.githubusercontent.com/98927072/169607366-bd6e1281-c219-447f-9483-6e116978cf84.png)
   
 By looking at the above plot, we can say that the data is clean, having No Null values. The data is Normally Distributed, having no outliers
   
  ![image](https://user-images.githubusercontent.com/98927072/169608291-0dac673d-f01d-4309-955b-f72958c1db78.png)
   
 By looking at the above countplot, we can say that the data us clearly balanced. 
   
   ![image](https://user-images.githubusercontent.com/98927072/169608434-40eff314-2f6e-4552-b6a8-2fddb14340a6.png)

By looking at the plot above, we conclude that there are topics in the subject column that are different from both the categories. 
   
 <h3> Text Preprocessing </h3>
      
Aside from numerical data, text data is widely available and is utilized to assess and solve business problems. However, before using the data for analysis and prediction, it must be processed. Text preprocessing is used to prepare text data for model creation. SIince our dataset is mostly textual data containing columns like "Text" ,  "Title" and "Subject", the preprocessing steaps we have implemented are as follows: 
      
 Some of the preprocessing steps are:

1. Removing punctuations like . , ! $( ) * % @
2. Removing URLs
3. Removing Stop words
4. Lower casing
5. Tokenization
6. Stemming
7. Lemmatization

<h3> Insights after Preprocessing the Text <h3>
  
  ![image](https://user-images.githubusercontent.com/98927072/169616183-dff6d256-74a1-4efd-ac39-92afe4109081.png)
  
The above word cloud is plotted for the column "Title" from the dataset and it can be seen that words like Donald, Trump, Embarrassing, Internet, Pope, Francis etc are highly repeated. 
  
  ![image](https://user-images.githubusercontent.com/98927072/169616432-5872c08a-7710-4b16-91c9-ee5935e79750.png)
  
The above word cloud is plotted for the column "Text" from the dataset and it can be seen that words like Reuters, Christmas, Trump, Devin, Annual etc are highly repeated.
  
![image](https://user-images.githubusercontent.com/98927072/169616980-e50bfa5c-3d00-473c-9245-eafaadff470b.png)

The above plot states the average word length in each text. 
   
 ![image](https://user-images.githubusercontent.com/98927072/169617900-967b095e-d3e7-4621-b6c7-46c0dc9b73ba.png)

The distribution of both seems to be a bit different. 2500 characters in text is the most common in original text category while around 5000 characters in text are most common in fake text category.
   
Furthermore, We have also plotted some n-grams, take a peek at them. 
   
![image](https://user-images.githubusercontent.com/98927072/169618009-f6ab4bae-3a42-40a3-a7d8-b0aba29de1d5.png)

   
![image](https://user-images.githubusercontent.com/98927072/169618536-6671df16-be7c-4a43-bb1a-f74f0276299a.png)
   
![image](https://user-images.githubusercontent.com/98927072/169618558-2e0a23ea-5e3f-42fb-8673-aec74c217bf7.png)
   
   
*Link to the Initial Video Presentation:*  https://youtu.be/7wq8NAB0-cI 

*Steamlit Web App:*  https://youtu.be/tIAiCyhWOWc
   
Thank you!



      

