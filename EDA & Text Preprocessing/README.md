
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

