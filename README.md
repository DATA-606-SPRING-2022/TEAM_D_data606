# UMBC DATA606 Data Science Capstone Project

## Capstone Project Proposal

##Proposed Team Name - TEAM_D_Data606

Author : Sushrutha DT and Srikeerthi Upperla 

# FAKE NEWS CLASSIFICATION AND PREDICTION

![image](https://user-images.githubusercontent.com/98927072/153283455-74b6119b-51b2-4c09-a95c-f961c636b736.png)


-------------------------------------------------------------------------------------------------------------------------------------------------------------

_**1.	What is your issue of interest (provide sufficient background information)?**_

Fake news on social media and other forms of media is widespread, and it is a source of serious concern because it has the potential to cause significant social and national harm, as well as have debilitating effects on individuals and communities. It has long been recognized that the authenticity of information is a problem that affects businesses and society in general, and that this is true for both printed and digital media. Fake news entails deliberate disinformation where false and misleading information is sowed to mislead, manipulate or harm for which there is invariably a large economic price tag attached. The year 2021 proved to be up to the task, beginning with the Capitol insurrection and continuing with a deluge of falsehoods and distortions about COVID-19 vaccines. 2021 proved to be up to be advent of new era as new social media apps like Tik-tok and other platforms came to rise. It is reasonable to assume that the global economy bears a cost of at least $78 billion per year from a growing number of small costs associated with fake news and larger incidents. Fake news' dangers and costs will only increase as technology improves, despite the best efforts of law enforcement.


_**2.	Why is this issue important to you and/or to others?**_

Personally, I've been a victim of fake news, particularly in the area of job rackets, where I received fake interview letters from recruiters claiming that if I paid up front, they would get me through the next rounds quickly, and the covid vaccination fiasco, where I was told that they were administering covid vaccine in a nearby government hospital, only to find out it was fake news and contract covid. Exam postponement is another example, as is fake news about the death of one of my favorite celebs.



**3.	Why is this important?**_

![image](https://user-images.githubusercontent.com/98927072/153283392-e9994172-1419-4541-9dc6-e5da6ef6f510.png)

The World Economic Forum ranks the spread of misinformation and fake news, as among the world’s top global risks. 
 
   o	**You deserve the truth** and are educated enough to make your own decisions based on the facts. 

   o	**False news erodes credibility** People will be less inclined to accept you if you base your arguments on incorrect data.

   o	**Fake news can harm you and others** Mercola.com and NaturalNews.com, for example, help promote misconceptions that HIV and AIDS are unrelated, or vaccines cause autism. These sites are dangerous and heavily trafficked.

   o	**Real news can help** If you wish to invest in a company, you should study factual articles about it. A voter should research a candidate thoroughly before casting a ballot to ensure that the candidate best represents his or her views. Real news may help you generate money and make the world a better place.


_**4.	What questions do you have in mind and would like to answer?**_

It is an important skill to be able to distinguish between accurate news and fake news, and one that you will use for the rest of your life. Our research investigates various textual properties that can be used to distinguish between fabricated and authentic content. In order to take advantage of these characteristics, we train a combination of different machine learning algorithms using various ensemble methods, and then evaluate their performance on real-world datasets. It is our goal to distinguish between fake and true news by developing powerful classification models for the news data we have gathered so far. 

•	**Spot if next submission of author is fake or**

•	**Extensive EDA of news**

•	**Suspicious titles that can be tagged to fake** 

_**Size of the dataset** :_ 123.81 MB

_**Shape of the dataset** :_ (20800, 5)

**train.csv**: A full training dataset with the following attributes:

**id** : unique id for a news article


**title**: the title of a news article


**author**: author of the news article


**text**: the text of the article; could be incomplete


**label**: a label that marks the article as potentially unreliable


   1: unreliable


   0: reliable


**test.csv**: A testing training dataset with all the same attributes at train.csv without the label.

**submit.csv**: A sample submission 


_**5.	What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units (observations) do you expect to analyze?**_

Here the unit of analysis is : Author / News organizations. 


_**6.	What variables/measures do you plan to use in your analysis (variables should be tied to the questions in #3)?**_

![image](https://user-images.githubusercontent.com/98927072/153284147-31b435f7-b2a2-4b44-8505-f91a156f7967.png)

I would mostly like to concentrate on – title, author and text from the dataset. 

_Title and Text:_ 

Does all the fraudulent news have repetitive jargon? Is there a pattern? 
What keywords are highly used in fake news?

_Author:_  

Are most of the fake news generated by the same author? Is there a pattern?
Predict if the following edition of the author would be fake.

_**7.	What kinds of techniques/models do you plan to use (for example, clustering, NLP, ARIMA, etc.)?**__

The sensationalism of not-so-accurate but eye-catching and intriguing headlines to retain audiences' attention to sell news has persisted throughout all sorts of information broadcast history, which, as conferred above, has many muted issues; thus, we would like to classify and predict fake news for which I plan to use the following models:

•	Logistic Regression


•	Multinomial Naïve Bayes


•	Passive aggressive classifier 


•	Support Vector Machine


•	Decision Trees


•	KNN

_**8.	How do you plan to develop/apply ML and how you evaluate/compare the performance of the models?**_

As the project aims to classify and predict Fake news, I would be considering this as more as a classification problem and thus would work on generating the Classification report that is used to measure the quality of predictions from a classification algorithm—the precision, AU- ROC, recall, F1 Score, and our trained classification model support. We plan to use visualization techniques to compare the performance and better understand each model's metrics.

_**9.	What outcomes do you intend to achieve (better understanding of problems, tools to help solve problems, predictive analytics with practical applications, etc)?**__

This project aims to develop a solution that users can utilize to detect and filter out news containing false and misleading information. The plan is to carefully select features to identify fake posts/news.

_**10.	Team Responsibility**_


Sri Keerthi - Team Captain

•	 Documentation

•	 Data EDA

•	 Data Cleanup

•	 Implementing NLP algorithms


Sushruth - Team Member

•	 Documentation

•	 Data EDA

•	 Data Cleanup

•	 Implementing Supervised classification algorithms and tuning 


**Reason for Pairing** : 
We became acquainted as mutual friends while assisting one of our mutual friends with her thesis psychology project on misinformation, which brought us together. And we were talking about how much it has immensely affected our personal lives as a result of this. We later discovered that we were enrolled in your Data 606 capstone course. Later, we came to the conclusion that we should collaborate and work on fake news detection.

_**EXPLORATORY DATA ANALYSIS:**_


Sushruth and I believe that Exploratory Data Analysis (EDA) is an essential process of using statistics and visual representations to perform initial analyses on data to uncover patterns, detect anomalies and verify assumptions about our datasets on Fake News. Thus, in our initial examination, we have 

- Checked for datatypes
- Check for missing values and their imputation
- Find the distribution of data.
- Closer look for outliers
- Check for correlation
- Descriptive Analysis and 
- Text Preprocessing

Initially, we have imported the necessary libraries like pandas, matplotlib, and seaborn 

Subsequently, we have loaded our datasets - submit.csv, test.csv, and train.csv from our Github repository using pandas. 

## Some interesting findings are listed down below: 

![image](https://user-images.githubusercontent.com/98927072/154867559-341c7502-0d90-4700-af58-276a74de90f5.png)

![image](https://user-images.githubusercontent.com/98927072/154867576-0f376a4c-972d-4537-aeb8-3ef2d79c5ca1.png)
  
 ![image](https://user-images.githubusercontent.com/98927072/154867585-41ca19ff-f0ab-4334-ad54-2d62fbe5d188.png)
 
- Here, we observed that Datatypes of columns are as expected. Therefore, there is no need to change data type

![image](https://user-images.githubusercontent.com/98927072/154867679-4f3d4d06-9c4f-4acd-9da6-5bb74c90b218.png)

- As there are missing values, we filled them with an empty string. 

![image](https://user-images.githubusercontent.com/98927072/154868210-dde18b80-4093-4a34-85e6-184e21438a5a.png)

- As, our dataset mostly contains text data, we got inquisitive to find the most frequent words and plotted a worldcloud 

![image](https://user-images.githubusercontent.com/98927072/154868268-8a4d0dd2-98fa-4a34-8089-1988c28e68fb.png)

- We found out that the words - Woman, Clinton,Hillary Civilians and Campus are few words that are more frequent in Titles of Articles.

 
![image](https://user-images.githubusercontent.com/98927072/154869313-c5ab5435-9dcd-4a94-8706-fdfdc0b9f5b4.png)
 
- Above are the few common words that were frequently used in dataset.

![image](https://user-images.githubusercontent.com/98927072/154869011-59548138-cc57-41c3-8757-807a7662194e.png)


![image](https://user-images.githubusercontent.com/98927072/154869186-59cdba66-ff42-49b5-ba18-02ae7cb8e1c7.png)

- Pam key, Admin, Jerome Hudson are few of the authors that has published most articles as per to Test and Train Data.




