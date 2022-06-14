import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt
import csv
import streamlit as st
import PIL
from PIL import Image as image

#%matplotlib inline  

def draw_daily_tweets():
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[0])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[0])
            
    
    #code to get the daily increase       
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)

    
    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)
    
    
    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[1,2,3,4,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[1,2,3,4,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y
    

     #plotting the graph  
    figure = plt.figure(figsize=(20,10))   
      
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = 'dashed',
             marker = 'o',label = "Samsung Daily Tweets Counts")
    
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = 'dashed',
             marker = 'o',label = "Huawei Daily Tweets Counts")
    
      
    
    plt.ylim([0,30])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Tweets', fontsize = 40)
    plt.title('Daily Tweets Posted ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()
    
    return figure,Samsung_df,Huawei_df

def draw_daily_followers():
    
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[1])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[1])
    
          
    #code to get the daily increase 
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)
    
    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)
    
    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[0,2,3,4,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[0,2,3,4,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y
       
    
    #plotting the graph
    figure = plt.figure(figsize=(20,10))     
        
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = 'dashdot',
             marker = 'o',label = "Samsung Daily New Followers")
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = 'dashdot',
             marker = 'o',label = "Huawei Daily New Followers")
    
    
    plt.ylim([-200,1000])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Followers', fontsize = 40)
    plt.title('Daily Increased Followers Count ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()
    
    return figure, Samsung_df, Huawei_df

def draw_daily_retweets():
    
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[3])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[3])
    
        
    #code to get the daily increase     
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)

    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)

    
    #replace the outliers with mean 
    # Samsung_Y_mean = Samsung_Y.copy()
    # Samsung_Y_mean.pop(0)
    # Samsung_Y_mean.pop(0)
    
    # mean = np.mean(Samsung_Y_mean)
    
    # Samsung_Y_mean = Samsung_Y.copy()
    # Samsung_Y_mean[1] = mean
    
    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[1,2,0,4,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[1,2,0,4,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y

     
    #plotting the figure  
    figure = plt.figure(figsize=(20,10))     
         
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = '-',
             marker = 'o',label = "Samsung Daily New Retweets")
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = '-',
             marker = 'o',label = "Huawei Daily New Retweets")
    
    
    
    plt.ylim([-2000,6000])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Retweets', fontsize = 40)
    plt.title('Daily Increased Retweets Count ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()
    
    
    
    return figure, Samsung_df, Huawei_df

def draw_daily_favorites():
    
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[4])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[4])
    
         
    #code to get the daily increase 
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)

    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)


    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[1,2,3,0,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[1,2,3,0,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y

       
    #plotting the figure
    figure = plt.figure(figsize=(20,10))     
        
      
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = '-',
             marker = 'o',label = "Samsung Daily New Favorites")
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = '-',
             marker = 'o',label = "Huawei Daily New Favorites")
    
    
    plt.ylim([-3000,30000])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Favorites', fontsize = 40)
    plt.title('Daily Increased Favorites Count ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()

    
    return figure, Samsung_df, Huawei_df



#### paste the story here into the respective story string
followers_story_str = "Even thought Samsung has a lot more followers than Huawei, Huawei has more daily follower increase compare to Samsung. This is because Samsung might already have reach all their pontential consumers while Huawei still starting to approach more variety consumer."
tweets_story_str ="Huawei tweet more than Samsung as most Huawei tweet are more related to their product usecase which need more than 1 tweets to showcase the product usecase on different scenario while Samsung tweets are more focus on the product features which different from what Huawei does. Another interesting fact is that both pages doesnt tweet at Saturday."
retweets_story_str = "The cause of sudden spike of Samsung daily retweet counts on 22/September is because on 21/September samsung retweets about BTS stuff and get alot of retweets while the sudden drop is because Samsung might have use bot to boost their retweet of certain post and caught by twitter anti-bot algorithm and had their retweet count to be remove. Another cause of droping that the new post doesnt generate enough retweet to cover back the bot detection algorithm. From here we at least can conclude that, Huawei doesnt use bot to help them boot their own tweets because their decline tweets might due to dissatisfied from consumer"
favorites_story_str = "The cause of sudden spike of Samsung daily favourite counts is the same reason as retweets which Samsung retweets about BTS stuff. As for the declide also the same as retweets reason which samsung use bot to boost their tweets."




#config on basic settings of stramlit
st.set_page_config(layout="wide")


page = st.sidebar.selectbox("Page to show", ("Assignment 1","Assignment 2","Assignment 3"))

### using columns to make the visualization looks better
col = st.columns(2)

if(page == 'Assignment 1'):
    st.title("Social media analysis for Samsung and Huawei on Twitter")
    st.markdown("***")
    option = st.sidebar.selectbox('Which visualization to show?', ('Daily increase of followers', 'Daily increase of tweets','Daily increase of retweets','Daily increase of favorites'))

    #using if else to show the choice of user on the dashboard
    if(option == 'Daily increase of followers'):
        figure,Samsung_df, Huawei_df  = draw_daily_followers()
        with col[0]:
            st.write(figure)
            st.write(followers_story_str)
        with col[1]:
            st.write("Samsung data")
            st.write(Samsung_df)
            st.write("Huawei data")
            st.write(Huawei_df)
        
    elif(option == 'Daily increase of tweets'):
        figure,Samsung_df, Huawei_df = draw_daily_tweets()
        with col[0]:
            st.write(figure)
            st.write(tweets_story_str)
        with col[1]:
            st.write("Samsung data")
            st.write(Samsung_df)
            st.write("Huawei data")
            st.write(Huawei_df)
        
        
    elif(option == 'Daily increase of retweets'):
        figure ,Samsung_df, Huawei_df = draw_daily_retweets()
        with col[0]:
            st.write(figure)
            st.write(retweets_story_str)
        with col[1]:
            st.write("Samsung data")
            st.write(Samsung_df)
            st.write("Huawei data")
            st.write(Huawei_df)

    elif(option == 'Daily increase of favorites'):
        figure,Samsung_df, Huawei_df  = draw_daily_favorites()
        with col[0]:
            st.write(figure)
            st.write(favorites_story_str)
        with col[1]:
            st.write("Samsung data")
            st.write(Samsung_df)
            st.write("Huawei data")
            st.write(Huawei_df)

elif(page == "Assignment 2"):
    
    option = st.sidebar.selectbox('Which question to show?', (1,2,3,4,5,6))
    if(option == 1):
        bigram_frequency = image.open("question1.png")
        
        st.title("What is the opinion of users towards the industry? ")
        st.markdown("***")
        
        col = st.columns(2)
        
        with col[0]:
            st.write("We want to look at the word frequency to see which words are repeated most often in the  comments. Word frequency helps in the sense of giving a quick sight of data such as how  people feel or their opinions within the context. We visualize the word frequency by bigram words as bigram helps to show the relation between words and get better insight. After  plotting the graph on the first ten word frequency “phone” was most repeated which is also  obvious since most of the extracted data contain this word. This is why we did not consider the  first ten words frequency and plot second ‘top thirty’ words frequency.  ")
            st.image(bigram_frequency)
            st.write("We can see the most repeated words are phone, camera, and case which are  basically properties of a phone. Beside that we can also know the existence of words user,  upload, social, work, dm (direct message) which possibly mean the usage of phone in daily life  and sharing the life activities. Another interesting matter is that we found the only brand name  ‘IPhone’ which also possibly depicts the most popular topic or expressed opinions towards  iPhone. Finally we can conclude that the most opinions towards the mobile industry are mostly  related to the properties of phones and sharing the usage of phone activities within the range of  data we collected.")
        
    
    elif(option == 2):
        brand_popularity = image.open("question2.png")
        
        st.title("Which are the brands that are popular among users  within the industry? ")
        st.markdown("***")
        
        col = st.columns(2)
        
        with col[0]:
            st.write("We will be analyzing the repeating count of each brand name over the collected data. We  believe that the most popular brand will be in topic for most of the time, in other words they  will appear in the topic for most count .Hence, the count of brand name appearance will help  to reach the conclusion towards the popularity. The count of appearance for each brand name  is shown in figure")
            st.image(brand_popularity)
            st.write("From the figure we can see that the apple was counted for the most of the time. After Apple  Samsung can be considered their next competitor and followed by Oppo, Huawei. From this  point of view it can be said that Apple, Samsung, Oppo, and Huawei are leading in the market  or industry. On the other hand , Nokia, Asus , Vivo , Sony , Motorola have very less count and  therefore less appearance in the data compared to other existing brands. Overall it can be  concluded that Apple, Samsung, Huawei, Oppo are the most popular brands among the users  within the industry.")

    elif(option == 3):
        samsung_pie = image.open("samsung_pie.png")
        apple_pie = image.open("apple_pie.png")
        oppo_pie = image.open("oppo_pie.png")
        xiaomi_pie = image.open("xiaomi_pie.png")
        huawei_pie = image.open("huawei_pie.png")
        
        st.title("What are the brands that are viewed negatively or  positively? ")
        st.markdown("***")
        st.write("To figure which brand is viewed positively or negatively, we perform sentiment analysis on  each brand. We have chosen Vader sentiment analysis to statistically label the sentiment of  each data. Vader is optimized and can yield good results when especially the data from Twitter,  Facebook etc. Vader sentiment produces the polarity of the word and their probabilities of  positive, negative, neutral and compound. Compound is the average value of probabilities of  positive and negative scores. In our analysis we designed the sentiments in a way where  polarity > 1, polarity == 1, and polarity < 1 are considered as Positive, Neutral and Negative.  Once we have the sentiments for each brand, we plot a pie chart by showing the percentage of  each sentiment of each brand. Here, we analyse the sentiments for each brand individually. ")
        st.markdown("***")
        
        col = st.columns(2)
        
        with col[0]:
            samsung_expander = st.expander(label='Samsung')
            apple_expander = st.expander(label='Apple')
            oppo_expander = st.expander(label='Oppo')
            
            with samsung_expander:
                st.header("Samsung")
                st.markdown("***")
                st.image(samsung_pie)
                st.write("From figure we can see the positive sentiments of Samsung is 50.5% of total sentiments and  less negative sentiments with 19.4% which illustrate the sentiments with positivity towards  Samsung. ")
            
            with apple_expander:
                st.header("Apple")
                st.markdown("***")
                st.image(apple_pie)
                st.write("Figure shows the high percentage of positive sentiments with 51.3% and 23.4% negative  sentiments. From here, we can conclude that Apple is evaluated more positively among the  users. ")
                
            with oppo_expander:
                st.header("oppo")
                st.markdown("***")
                st.image(oppo_pie)
                st.write("Figure shows the percentage of positive sentiments 50.6%, neutral sentiments 34.0% and  15.5 % negative sentiments. The result is quite similar to Huawei. So it can be concluded that  like Huawei, Oppo is also a favourite of its users. ")
        
        with col[1]:   
            xiaomi_expander = st.expander(label='Xiaomi')
            huawei_expander = st.expander(label='Huawei')
            
            with xiaomi_expander:
                    st.header("Xiaomi")
                    st.markdown("***")
                    st.image(xiaomi_pie)
                    st.write("Figure illustrates the sentiments of Xiaomi, here it shows the positive sentiments is 50.3%,  30.7% negative assignments and 19.0% negative assignments. Like other brands Xiaomi also  shows more positive acceptance by their users. ")
                    
            with huawei_expander:
                    st.header("Huawei")
                    st.markdown("***")
                    st.image(huawei_pie)
                    st.write("We can see in the figure that Huawei has more than half of the total sentiments positive and  also very less negative sentiments which is 15.1%. This can possibly tell us that Huawei is  the favourite of its users. ")
        
    elif(option == 4):
        st.title("Within the industry, what is the users’ sentiment towards the different brands?")
        st.markdown("************")
        col = st.columns(3)
        samsung_sentiment = image.open("samsung_sentiment.png")
        apple_sentiment = image.open("apple_sentiment.png")
        xiaomi_sentiment = image.open("xiaomi_sentiment.png")
        huawei_sentiment = image.open("huawei_sentiment.png")
        oppo_sentiment = image.open("oppo_sentiment.png")
        
        samsung_str = "Samsung with a count of 1746, 1015 of them having neutral sentiment and the count of negative sentiment towards Samsung is 559. Overall the sentiment of the user in the tweets that we collected are positive towards Samsung."
        apple_str = "We can observe that in the figure above the overall sentiments of users towards Apple are positive. Based on the output of TextBlob, Apple acquired 6841 positive sentiment, 3409 neutral sentiment and 2369 negative sentiment. Most of the users are having positive sentiments with the most discussed brands of the data collected."
        huawei_str = "Same as the previous brand, the sentiment of users towards Huawei is also positive most of the time by having 497 positive sentiment tweets from users. 340 of them are neutral sentiment tweets and only 141 are negative."
        xiaomi_str = "The figure shows the sentiment analysis of Xiaomi on tweets collected and it is positive overall. Xiaomi is getting 818 positive sentiment tweets from users, 492 neutral tweets and 265 negative sentiment tweets from the users."
        oppo_str = "With the 700 cleaned data of Oppo dataset, we can conclude that the overall sentiment of users towards the brand Oppo is also positive. Oppo has 378 positive sentiment tweets, 220 neutral sentiment tweets and 100 negative tweets from the user of the cleaned dataset."
        conclusion_str = "In conclusion, all the brands that we collected are getting mostly positive sentiment from the users of twitter. This means that most of the users are having positive thoughts about these brands in the industry within the range of data we collected."
        
        with col[0]:
            st.header("Samsung")
            st.image(samsung_sentiment)
            st.write(samsung_str)
            
            st.markdown("********")
            
            st.header("Apple")
            st.image(apple_sentiment)
            st.write(apple_str)
        with col[1]:
            st.header("Huawei")
            st.image(huawei_sentiment)
            st.write(huawei_str)
            
            st.markdown("********")
            
            st.header("Xiaomi")
            st.image(xiaomi_sentiment)
            st.write(xiaomi_str)
        with col[2]:
            st.header("Oppo")    
            st.image(oppo_sentiment)
            st.write(oppo_str)   
            
            st.markdown("********")
        
        st.markdown("********") 
        st.write(conclusion_str)
            
    elif(option == 5):
        st.title("What are the frequent topics that users mention when they interact with the different brands over social media? What is their sentiment towards those topics?")
        st.markdown("************")
        
        coherence = image.open("coherence_industry.png")
        topic = image.open("industry_lda_topic.png")
        
        topic_0 = image.open("industry_topic_0.png")
        topic_1 = image.open("industry_topic_1.png")
        topic_2 = image.open("industry_topic_2.png")
        topic_3 = image.open("industry_topic_3.png")
        topic_4 = image.open("industry_topic_4.png")
        
        topic_0_infer = "With the keyword of topic 0, we can infer that topic 0 could be related to the mobile product after service and warranty issues."
        topic_1_infer = "From the frequent words of topic 1, we can observe that there are words like get, new and buy. We can infer that this topic is where the user discusses getting a new phone of one of the brands we analyse on."
        topic_2_infer = "From the keyword of topic 2, we can infer that the topic might be talking about how the specification of a mobile phone affects the price because of the words like: camera, gb and series appear. "
        topic_3_infer = "As the figure above shows, the keyword from topic 3 is kinda hard for us to infer what is the main focus of the topic. The only idea we can infer is maybe users are talking about mobile phone applications that need to have support for new features or something."
        topic_4_infer = "Based on the keyword in topic 4, we can conclude that there are two topics that are discussed and they might be related. First, the user might be discussing the series and the model of mobile phones of different brands because terms like: x, lite, note and pro appear. Next the users are discussing the charging and the power of the battery. This two topic should be related to each other as the charging ability of different phone modal can be different."
        
        
        sentiment_topic_0 = image.open("industry_sentiment_topic_0.png")
        sentiment_topic_1 = image.open("industry_sentiment_topic_1.png")
        sentiment_topic_2 = image.open("industry_sentiment_topic_2.png")
        sentiment_topic_3 = image.open("industry_sentiment_topic_3.png")
        sentiment_topic_4 = image.open("industry_sentiment_topic_4.png")
        
        sentiment_analyze_topic_0 = "Looking at the sentiment analysis of topic 0, most of the users have positive sentiment when they are discussing topic 0. Positive sentiments are the majority but the number of negative and neutral sentiments is more than the positive sentiment. This can mean most of the users are happy with the topic discussed in topic 0 but some of them are having unpleasant experiences and issues when dealing with the thing discussed in topic 0."
        sentiment_analyze_topic_1 = "As the figure shows most of the user sentiments towards topic 1 are in a positive way. Neutral and negative sentiments are less than half of the positive sentiments."
        sentiment_analyze_topic_2 = "When talking about the specification and price of the mobile phone, most of the users are having positive and neutral sentiments towards the topic. Only a minority of the users are having negative sentiments towards it."
        sentiment_analyze_topic_3 = "When it comes to topic 3, most of the user sentiment towards it are positive and some of them are neutral. Only a minority is negative sentiments."
        sentiment_analyze_topic_4 = "As the figure shows, just like previous topics the topic 4 also getting positive sentiments overall. Few of them are having neutral sentiments and a small group of users are having negative sentiments towards topic 4."
        
        
        st.write("To answer this question, we concat all the cleaned data of the collected brands into the same set of data and perform topic modelling. Next is to perform some other pre-process such as lemmatization and turn the dataset into numerical representations using a bag of words. After all this we can use the coherence score to find out what is the best number of topics for our dataset.")
        st.image(coherence)
        st.write("After calculating the coherence score of different numbers of topics, we decided to use 5 as the k for the LDA model to perform topic modelling. The frequent word of each topic are shown in the word cloud.")
        
        col = st.columns(2)
        with col[0]:
            st.image(topic)
            st.markdown("***")
        
            
        with col[1]:
            topic_0_expander = st.expander(label='Topic 0')
            topic_1_expander = st.expander(label='Topic 1')
            topic_2_expander = st.expander(label='Topic 2')
            topic_3_expander = st.expander(label='Topic 3')
            topic_4_expander = st.expander(label='Topic 4')
            
            with topic_0_expander:
                st.header("Topic 0")
                st.image(topic_0)
                st.write(topic_0_infer)
                st.image(sentiment_topic_0)
                st.write(sentiment_analyze_topic_0)
                st.markdown("***")
                
            with topic_1_expander:
                st.header("Topic 1")
                st.image(topic_1)
                st.write(topic_1_infer)
                st.image(sentiment_topic_1)
                st.write(sentiment_analyze_topic_1)
                st.markdown("***")
            
            with topic_2_expander:
                st.header("Topic 2")
                st.image(topic_2)
                st.write(topic_2_infer)
                st.image(sentiment_topic_2)
                st.write(sentiment_analyze_topic_2)
                st.markdown("***")
            
            with topic_3_expander:
                st.header("Topic 3")
                st.image(topic_3)
                st.write(topic_3_infer)
                st.image(sentiment_topic_3)
                st.write(sentiment_analyze_topic_3)
                st.markdown("***")
            
            with topic_4_expander:
                st.header("Topic 4")
                st.image(topic_4)
                st.write(topic_4_infer)
                st.image(sentiment_topic_4)
                st.write(sentiment_analyze_topic_4)
                st.markdown("***")
        
    elif(option == 6):
        st.title("What are the important aspects (and its sentiment) that are discussed by the users specifically on the target company.")        
        st.markdown("************")
        
        coherence = image.open("samsung_coherence.png")
        topic = image.open("samsung_lda_topic.png")
        
        topic_0 = image.open("samsung_topic_0.png")
        topic_1 = image.open("samsung_topic_1.png")
        topic_2 = image.open("samsung_topic_2.png")
        topic_3 = image.open("samsung_topic_3.png")
        topic_4 = image.open("samsung_topic_4.png")
        topic_5 = image.open("samsung_topic_5.png")
        topic_6 = image.open("samsung_topic_6.png")
        topic_7 = image.open("samsung_topic_7.png")
        
        topic_0_infer = "Based on the keyword above, topic 0 might be related to customer service and product after service on the Samsung mobile phone."
        topic_1_infer = "From the frequent words of topic 1, we can observe that there are words like get, new and need. We can infer that this topic is where the user discusses getting a new Samsung phone."
        topic_2_infer = "From what we can observe, users might be discussing the specifications of different Samsung phone models. Words like note, galaxy and ultra are the words that Samsung uses to name their phone model series. Users might me discuss these phone models about their specifications such as color and features."
        topic_3_infer = "Based on the keyword above, the user might be discussing Samsung products other than mobile phones. The user might be discussing how Samsung is doing with the product other than mobile phones."
        topic_4_infer = "From what the keyword shows, we can infer that topic 4 might be talking about the other products of Samsung like tv and tablet and how they work with the Samsung mobile phones."
        topic_5_infer = "The keywords of topic 5 barely make any sense. The only idea that can be inferred from is the charging issues of Samsung and charger. This topic might be discussing something related with the technology of phone charging of Samsung."
        topic_6_infer = "From the keyword we can infer that Samsung and Google are choosing V to represent their brands. V is a member from the korean group BTS. So the text that belongs to this topic is mostly talking about V promoting their products."
        topic_7_infer = "Last topic is the users talking about the latest flippable phone by Samsung that is going to launch. The model name is Samsung Galaxy S21 FE so the keyword fe and galaxy keep appearing."
        
        sentiment_topic_0 = image.open("samsung_sentiment_topic_0.png")
        sentiment_topic_1 = image.open("samsung_sentiment_topic_1.png")
        sentiment_topic_2 = image.open("samsung_sentiment_topic_2.png")
        sentiment_topic_3 = image.open("samsung_sentiment_topic_3.png")
        sentiment_topic_4 = image.open("samsung_sentiment_topic_4.png")
        sentiment_topic_5 = image.open("samsung_sentiment_topic_5.png")
        sentiment_topic_6 = image.open("samsung_sentiment_topic_6.png")
        sentiment_topic_7 = image.open("samsung_sentiment_topic_7.png")
        
        sentiment_analyze_topic_0 = "Unlike most of the sentiment analysis results we get along this assignment, sentiment of users towards topic 0 are more neutral instead of positive and negative. With that said, the number of positive sentiments still overpower the negative sentiment in this topic."
        sentiment_analyze_topic_1 = "From the figure of sentiment analysis above, we can see that the majority of the tweets get positive sentiment from the users. Only a minority have negative sentiment and neutral sentiment."
        sentiment_analyze_topic_2 = "The positive sentiments and neutral sentiments are almost even based on the figure of sentiment analysis of topic 2 shown above. Only a minority of users give negative sentiments towards topic 2."
        sentiment_analyze_topic_3 = "The sentiment analysis of topic 3 only has a minority in negative sentiments and most of the users are having positive and neutral sentiments towards the topic discussed in topic 3."
        sentiment_analyze_topic_4 = "Majority of the user sentiment are positive towards topic 4 while few of them have neutral sentiment and small percentage of it are having negative sentiments."
        sentiment_analyze_topic_5 = "Similar to the previous topics, most of the users are having positive sentiments towards topic 5 and some of them having neutral sentiments. Only a small part of them are negative sentiments."
        sentiment_analyze_topic_6 = "Based on the sentiment analysis figure of topic 6, most of the users are having positive sentiments towards this topic. Only a minority of users having negative sentiments and a large group of users also having neutral sentiments. "
        sentiment_analyze_topic_7 = "We can observe that although there are a lot of positive sentiments in this topic, the majority of tweets are neutral. Only a minority sentiment is negative."
        
        st.write("Similar to the previous question, we will run topic modelling on the target company which in our case is Samsung. We will first run a function to get the coherence score for each number of topics to get the optimal k.")
        st.image(coherence)
        st.write("We will be using k = 8 in the LDA model. Below figure shows the data frame of the Samsung LDA model. It contains the dominant topic and keywords of each tweet.")
                
        col = st.columns(2)
        with col[0]:
            st.image(topic)
            st.markdown("***")
        
            
        with col[1]:
            topic_0_expander = st.expander(label='Topic 0')
            topic_1_expander = st.expander(label='Topic 1')
            topic_2_expander = st.expander(label='Topic 2')
            topic_3_expander = st.expander(label='Topic 3')
            topic_4_expander = st.expander(label='Topic 4')
            topic_5_expander = st.expander(label='Topic 5')
            topic_6_expander = st.expander(label='Topic 6')
            topic_7_expander = st.expander(label='Topic 7')
            
            with topic_0_expander:
                st.header("Topic 0")
                st.image(topic_0)
                st.write(topic_0_infer)
                st.image(sentiment_topic_0)
                st.write(sentiment_analyze_topic_0)
                st.markdown("***")
                
            with topic_1_expander:
                st.header("Topic 1")
                st.image(topic_1)
                st.write(topic_1_infer)
                st.image(sentiment_topic_1)
                st.write(sentiment_analyze_topic_1)
                st.markdown("***")
            
            with topic_2_expander:
                st.header("Topic 2")
                st.image(topic_2)
                st.write(topic_2_infer)
                st.image(sentiment_topic_2)
                st.write(sentiment_analyze_topic_2)
                st.markdown("***")
            
            with topic_3_expander:
                st.header("Topic 3")
                st.image(topic_3)
                st.write(topic_3_infer)
                st.image(sentiment_topic_3)
                st.write(sentiment_analyze_topic_3)
                st.markdown("***")
            
            with topic_4_expander:
                st.header("Topic 4")
                st.image(topic_4)
                st.write(topic_4_infer)
                st.image(sentiment_topic_4)
                st.write(sentiment_analyze_topic_4)
                st.markdown("***")

            with topic_5_expander:
                st.header("Topic 5")
                st.image(topic_5)
                st.write(topic_5_infer)
                st.image(sentiment_topic_5)
                st.write(sentiment_analyze_topic_5)
                st.markdown("***")

            with topic_6_expander:
                st.header("Topic 6")
                st.image(topic_6)
                st.write(topic_6_infer)
                st.image(sentiment_topic_6)
                st.write(sentiment_analyze_topic_6)
                st.markdown("***")
                
            with topic_7_expander:
                st.header("Topic 7")
                st.image(topic_7)
                st.write(topic_7_infer)
                st.image(sentiment_topic_7)
                st.write(sentiment_analyze_topic_7)
                st.markdown("***")

elif(page == 'Assignment 3'):
    st.title("Social network analysis on Samsung and Huawei on Twitter")
    st.markdown("*****")
    st.write("Social network analysis (SNA) is the process of investigating social structures through the use of networks and graph theory. In this assignment, we will explain the results we have been found on Samsung and Huawei network.")

    st.header("Centrality Measures")
    centrality_measure = "We only use 3 type of centrality measures which is degree centrality, eigenvector centrality and page rank centrality. Degree Centrality is to measure how many nodes are connected to the brand. The degree centrality for a node is simply its degree. For degree centrality, higher values mean that the node is more central and vice-versa.Eigenvector centrality is to measure the influence of a node in a network. A high eigenvector score means that a node is connected to many nodes who themselves have high scores and vice-versa.Page rank is used to evaluate the quality and quantity of the links to a page. In our cases, it is to see how popular the brand is by calculating the value of the edges that link to the brand."
    st.write(centrality_measure)
    
    data =[["Huawei",'0.009474182851729039','0.010217521076635488','0.0036287085778269686'],["Samsung",'0.016837851490149856','0.011752899619136217','0.006565344263411281']]
    df = pd.DataFrame(data, columns = ['Brands', 'Degree Centrality','Eigenvector Centrality','Page Rank'])
    st.write(df)
    
    centrality_measure_1 = "For degree centrality, Samsung brand achieved the highest score of the centrality which indicated there are many connections (edges) for the followers or friends towards the brand and vice-versa. In contrast, Huawei has the lowest score of the centrality. For eigenvector centrality, the Samsung brands showed many influences of a node in a network. A high eigenvector score means that a node is connected to many nodes who themselves have high scores and vice-versa. Meanwhile, the Huawei brand has the lowest eigenvector score which indicates the least influences of a node in a network.For page rank, it can see that the Samsung brand has the highest page rank score among the others. Huawei have the lowest page rank score compared to the Samsung brand. Therefore we can see that Samsung is more popular than the Huawei brands."
    st.write(centrality_measure_1)
    st.markdown("*****")
    
    
    huawei_network = image.open("huawei_network.jpg")
    huawei_node_0 = image.open("huawei_node_0.jpg")
    huawei_node_1 = image.open("huawei_node_1.jpg")
    huawei_node_2 = image.open("huawei_node_2.jpg")
    huawei_node_3 = image.open("huawei_node_3.jpg")
    huawei_node_4 = image.open("huawei_node_4.jpg")
    huawei_node_5 = image.open("huawei_node_5.jpg")
    huawei_node_6 = image.open("huawei_node_6.jpg")
    
    huawei_des_0 = "Figure above show the biggest community form in the network. About 4992 out of 10556 nodes in this network form this community and in the center which is the. This user is social influencer talking about wellbeing and religions stuff. This user have 124.7k followers and we only extract 5k due to computation power. From the 5k nodes, some of them are student, some of them are small startup, some of them are news reporting channel, some also the same as him which is social influencer talking about well being stuff.  "
    huawei_des_1 = "Figure above show the 2nd biggest community form in the network.  About 1556 out of 10556 nodes in this network form this community and in the center which is @ongz87. This user is a football fans and movie critic and most of the follower is from Indonesia.  "
    huawei_des_2 = "Figure above show the 3rd biggest community form in the network.  About 906 out of 10556 nodes in this network form this community and in the center which is @ajmalmehmood1. This user is a radiologist which his profession is related to technology stuff. Most of his followers, is either a politician, journalist or tech nerds. "
    huawei_des_3 = "Figure above show the 4th biggest community form in the network.  About 906 out of 10556 nodes in this network form this community and in the center which is @SgothanGeal. This user is seller on vape product and flavor. Most of his follower are also that like to vape. "
    huawei_des_4 = "Figure above show the 5th biggest community form in the network.  About 489 out of 10556 nodes in this network form this community with 2 main nodes which is @EstylezHot  and @Crusher17755966 . @EstylezHot is a pages that sell fashion accessories while @Crusher17755966 doesn’t have much information about him other than most of his retweet are about shoes. This community is form due to their background as most of the user is from Africa side. "
    huawei_des_5 = "Figure above show the 6th biggest community form in the network.  About 378 out of 10556 nodes in this network form this community with the main node AboGhenan_7. @AboGhenan_7 is a tech nerds where most of his retweet are about mobile phone. Most of the followers of his are from the same country as him. "
    huawei_des_6 = "Figure above show the 7th biggest community form in the network.  About 331 out of 10556 nodes in this network form this community and in the center which is our main target @HuaweiMobile. This community is form because each of Huawei’s follower have their own followers at least 4 to 20 followers. "
    
    samsung_network = image.open("samsung_network.jpg")
    samsung_node_0 = image.open("samsung_node_0.jpg")
    samsung_node_1 = image.open("samsung_node_1.jpg")
    samsung_node_2 = image.open("samsung_node_2.jpg")
    samsung_node_3 = image.open("samsung_node_3.jpg")
    samsung_node_4 = image.open("samsung_node_4.jpg")
    samsung_node_5 = image.open("samsung_node_5.jpg")
    samsung_node_6 = image.open("samsung_node_6.jpg")
    
    samsung_des_0 = "Figure above show the biggest community form in the network. About 3816 out of 5940 nodes in this network form this community and in the center which is the @ismailduran66. This user is from Germany and is an Islamic person.  Most of his follower is from the same country as him which is Germany."
    samsung_des_1 = "Figure above show the 2nd biggest community form in the network. About 1210 out of 5940 nodes in this network form this community and in the center which is the @Mohsen_Najaffi. This user is from Iran most of his tweet post is regarding about politician issue in Iran. Most of his followers are from the same country and has the same interest as he is which is regarding politician issue in Iran."
    samsung_des_2 = "Figure above show the 3rd biggest community form in the network. About 299 out of 5940 nodes in this network form this community and in the center which is also our main target @SamsungMobile. Why this community is form is because each followers of SamsungMobile have at least 2 to 10 of their own followers."
    samsung_des_3 = "Figure above show the 4th biggest community form in the network. About 77 out of 5940 nodes in this network form this community and in the center is @AndresdelBosqu8. This user is a football fans. Most of his followers is either bot or adult content creator."
    samsung_des_4 = "Figure above show the 5th biggest community form in the network. About 75 out of 5940 nodes in this network form this community and in the center is @ WillPickens4. This user is a gamer and meme sharer. As for his followers, we cant seem to find any correlation between them."
    samsung_des_5 = "Figure above show the 6th biggest community form in the network. About 70 out of 5940 nodes in this network form this community and in the center is @imv_taetae30. This user is a BTS fans which is 1 of the celebrity group that promote with Samsung. Most of this user follower are also BTS fans. "
    samsung_des_6 = "Figure above show the 7th biggest community form in the network. About 61 out of 5940 nodes in this network form this community and there is 2 center nodes which is  @MunikyNathalya and @CuadrosLuxi. @MunikyNathalya is a BTS fans and @CuadrosLuxi is also a BTS fans but this user loves all korean bands like blackpink and other solo korean actor. Both of these account speak in the same language which is spanish. "

    col = st.columns(2)
    
    
    with col[0]:
        huawei_expander = st.expander(label='Huawei')
        samsung_expander = st.expander(label='Samsung')
        with huawei_expander:
            st.subheader("Top community form in Huawei Network")
            st.write("HuaweiMobile has a total 10556 nodes, 10579 edges and average degree of 2.0044 in the network. From there we found about 23 communities has been form over the network. ")
            st.image(huawei_network)
            st.write("Figure above show the top community from in these network. We will be discussing 1 by 1 of each of the top form community")
            st.markdown("***")
            
            st.subheader("1st community")
            st.image(huawei_node_0)    
            st.write(huawei_des_0)
            st.markdown("***")
            
            st.subheader("2nd community")
            st.image(huawei_node_1)    
            st.write(huawei_des_1)
            st.markdown("***")
            
            st.subheader("3rd community")
            st.image(huawei_node_2)    
            st.write(huawei_des_2)
            st.markdown("***")
            
            st.subheader("4th community")
            st.image(huawei_node_3)    
            st.write(huawei_des_3)
            st.markdown("***")
            
            st.subheader("5th community")
            st.image(huawei_node_4)    
            st.write(huawei_des_4)
            st.markdown("***")
            
            st.subheader("6th community")
            st.image(huawei_node_5)    
            st.write(huawei_des_5)
            st.markdown("***")
            
            st.subheader("7th community")
            st.image(huawei_node_6)    
            st.write(huawei_des_6)
            st.markdown("***")
            
            
        with samsung_expander:
            st.subheader("Top community form in Samsung Network")
            st.write("SamsungMobile has a total 5940 nodes, 5941 edges and average degree of 2.0003 in the network. From there we found about 18 communities has been form over the network. ")
            st.image(samsung_network)
            st.write("Figure above show the top community from in these network. We will be discussing 1 by 1 of each of the top form community")
            st.markdown("***")
            
            st.subheader("1st community")
            st.image(samsung_node_0)    
            st.write(samsung_des_0)
            st.markdown("***")
            
            st.subheader("2nd community")
            st.image(samsung_node_1)    
            st.write(samsung_des_1)
            st.markdown("***")
            
            st.subheader("3rd community")
            st.image(samsung_node_2)    
            st.write(samsung_des_2)
            st.markdown("***")
            
            st.subheader("4th community")
            st.image(samsung_node_3)    
            st.write(samsung_des_3)
            st.markdown("***")
            
            st.subheader("5th community")
            st.image(samsung_node_4)    
            st.write(samsung_des_4)
            st.markdown("***")
            
            st.subheader("6th community")
            st.image(samsung_node_5)    
            st.write(samsung_des_5)
            st.markdown("***")
            
            st.subheader("7th community")
            st.image(samsung_node_6)    
            st.write(samsung_des_6)
            st.markdown("***")
    
    with col[1]:
        st.write("")