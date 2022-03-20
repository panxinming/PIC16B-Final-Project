
<p align="center">
      <font size=17> Final Project Proposal </font>
</p>

<p align="center">
    Xinming Pan, Xinyu Dong
</p>

## Questions
1. What do you think about the idea of our project. Do you think it's useful and meaningful?
2. If you are a potential breast cancer patient who want to use our WebAPP. Would you believe our test result? If not, can you give use some suggestions that we can win more trust from patients.
3. We want to build our WebApp as a medical platform. However, our App can just give us a prediction of breast cancer currenctly. If possible, do you have some sugggestoins that we can add to make our WebApp more attractive? 


## How to Use Our WebApp
Finally, we already construct our WebApp. It's developed by python. We used a lot of machine learning method and some very popular python packages. Now, I will introduce our App and how we use it.

1. First of all, this App is created for the patients who has potential breast cancer. So, if you are not the appropriate person, this App is only just for fun. Before you use it, you should understand the function of it. The App is created to predict one person has breast cancer or not.
2. Secondly, our App needs four detail information of the patient, so that our App can give them a prediction. If one of these information was lacked, it will return error.
3. Thirdly, the App will not go into medical field. Even though our prediction has very high accuracy, it still doesn't mean 100% correct. So, if one patient really want to test whether she got breast cancer or not. We highly recommend her to go to hospital instead of using our App. And we won't be responsible for the test result.
4. Last but not least, our App may has some bias. Because all the data is collected comes from United States. So, if you are the patients who come from Aisa, Africa, Europe etc. The prediction may be incorrect. 

If you fully understand the potential disadvantages of our App and accept the potential danger, I think you can use our WebApp right now. Good Luck and have fun.


## 1. Abstract
Breast cancer is the second leading cause of cancer death in women, with a death rate of 1 in 39 (about 2.6%). By using data containing some basic information about patients, we want to make predictions about whether they have breast cancer or not. Our team will divide a huge data set from the Internet into two parts—training and testing and use advanced machine learning methods to make predictions.

## 2. Planned Deliverables
We plan to make a webapp for our project. The ideal state is when a patient inputs basic information about herself, we will be able to make predictions about whether she will get breast cancer or not at 90% accuracy. Even if we failed to put the webapp together, we can create the code repository and show our machine learning methods.

## 3. Resources required
Data from UCI Machine Learning Repository
Link is here: [https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)

## 4. Tools and Skills Required
We will need machine learning and some knowledge about creating webapps. Some techniques we will use are: Python, Jupyter Notebook, Linux, SQL database, WebApp, Plotly. Because the original data has lots of missing values, so for our best predictions, we try to fill out these missing values by using Panda to do the data cleaning. Of course, We also plan to use the Tableau to create some wonderful figures, for example, we can create a histogram to show which people are more likely to get breast cancer. And recently, we learned how to use plotly to create awesome data visualization. So, we decide to use Plotly to create some nice figures. Because our data is large, so create a database and use SQL command is a good way to extract data.  
In the end, we plan to use a mathematical model to predict our result. Like linear regression, logistic regression, Random Forest etc. And we also want to use the most popular algorithm, which is called CNN, SVM. These works are all done in Jupyter Notebook, because Jupyter Notebook is a good platform to do machine learning and data analysis.

## 5. What You will learn
We will learn to create interactive webapps and complex machine learning models. For example, like we mentioned above, CNN and SVM algorithms are very popular mathematical models, but they are not covered in undergraduate school. So, we might learn how to use these complex methods to predict our data. What’s more, we can learn what this analysis can bring to us. For example, we may analyze if the radius, texture of the breast is associated with breast cancer. So, it will give us a medical acknowledgement of breast cancer. Finally, we plan to post our analysis, so it will also give us the ability to design a webapp.

## 6. Risks
### (a).
First risk we might encounter is there are some very complex mathematical models we have never learned. So, figuring out how these algorithms work is a risk for us.

### (b)
Second risk we might see is that our data is extremely huge, so we plan to create a database to save the data and use SQL commands to extract what we need. However, SQL commands are a little bit more complicated than Panda in Python. So, SQL commands may be our biggest risk.

## 7. Ethics

### (a). What groups of people have the potential to benefit from the existence of our product?
Those who may have a potential for breast cancer may benefit from the existence of our product.

### (b). What groups of people have the potential to be harmed from the existence of our product?
The health care workers may be harmed by the existence of our product.

### (c). Will the world become an overall better place because of the existence of our product?
Yes, the world will be a better place since we can predict those who may have a potential for breast cancer whether they have breast cancer or not quicker, more efficiently. It may save breast cancer patients time to recover from the cancer.
It will also save the patient money. Instead of going to the hospital to do some complex and expensive diagnosis. machine learning methods will be a better choice.

## 7. Algorithm Bias
### (a). Suppose that someone uses your app and it says that they have a low risk. Because of this, they don't go to the doctor for a checkup -- but later, they develop breast cancer. Is your app responsible for this outcome? Why or why not?
Actually, We think our APP won't be responsible for this outcome. However, we will warn the people who use our app that only if our app give a benign result, but it still can be malignant for some reasons. There are few predicting APPs that can give the people 100% prediction. Our APP only gives people a reference, if people want to get the accurate result, we still suggest they go to the hospital. What's more, we think if someone want to use our APP, we would ask them to sign the contract that they should understand that there is a risk even if the outcome is benign.

### (b). It is often found that medical recommender algorithms can work well on some groups of people and not others. For example, here is a summary of a recent journal article in which a recommender system included racial bias. Is there a risk of such bias in your algorithm? How do you know? Is there anything you might be able to do to check?
Yes, our algorithm exists bias. Like we mentioned above, ou data is from UCI Machine Learning Repository. And the data is collected during daily life. And the creators are all from university in United States. Therefore, the data we got might be limited. We all know that there is a huge difference in people's breast among different areas. So, our algorithm might not be suitable for Asia, Europe and Africa people. 
There is another bias in our algorithm. From the link above, we can see that the data is collected in 1995. Now is 2022, the time gap is extremely huge. With the time flowing, people's health and social environment both changed a lot. And these two factors may affect breast cancer, so I think our algorithm is not fair to those young people.
