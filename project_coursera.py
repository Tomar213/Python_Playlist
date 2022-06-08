import pandas as pd
import plotly.express as px
df = pd.read_csv('final_file.csv')
fig = px.line(df, ' netScore','retweet', title='Asert')
fig.show()

#__Question____________________________________________________________________________________
# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number o
# f retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.t
# xt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of 
# Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net 
# Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere 
# in the word. (Hint: remember the .replace() method for strings.)

def strip_punctuation(x):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for punc in punctuation_chars:
        if punc in x:
            x=x.replace(punc," ")
    return x
fh  = open("project_twitter_data.csv")
fp=open('positive_words.txt')
lp=list()
new_data2=[]
neg_item_list=list()
poslstOfCommon=list()
fn=open('negative_words.txt')
ln=list()
lstOfNegCommon=list()
for n in fn:
    n=n.rstrip("\n")
    ln.append(n)
for p in fp:
    p=p.rstrip("\n")
    lp.append(p)
for word in fh:
    new_data=strip_punctuation(word)
    new_data=new_data.rstrip("\n")
    new_data= new_data.split()
    for i in new_data:
        i=i.lower()
        new_data2.append(i)
    # print(new_data)
    common =  list(set(new_data2).intersection(lp))
    poslstOfCommon.append(len(common))
    negCommon  = list(set(new_data2).intersection(ln))
    neg_item_list.append(len(negCommon))
    
print(poslstOfCommon)
print(neg_item_list)
fh.close()
res_file= open("final_file.csv","a")
data = open("project_twitter_data.csv")
res_file.write(f"Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
cnt=-1
for i in data:
    cnt+=1
    i=i.rstrip("\n")
    plst=i.split(',')
    print(f"{plst[1]},   {plst[2]},    {poslstOfCommon[cnt]},   {neg_item_list[cnt]},    {poslstOfCommon[cnt]+neg_item_list[cnt]}")
    res_file.write(f"\n{plst[1]},            {plst[2]},    {poslstOfCommon[cnt]},          {neg_item_list[cnt]},      {poslstOfCommon[cnt]+neg_item_list[cnt]} ")
res_file.close()
data.close()
fp.close()




#____________________________________________________________________________________________________-
lp=list()
y=[]
positive_words=[]
def strip_punctuation(x):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for punc in punctuation_chars:
        if punc in x:
            x=x.replace(punc," ")
    return x
with open('positive_words.txt') as fp:
    for p in fp:
        p=p.rstrip("\n")
        lp.append(p)
def get_pos(x):
    x=strip_punctuation(x)
    x=x.rstrip('\n')
    x=x.split()
    for i in x:
        i=i.lower()
        y.append(i)
    cmn = list(set(lp).intersection(y))
    if len(cmn)!=0:
        for item in cmn:
            positive_words.append(item)
    return len(cmn)
print(get_pos("what a truly wonderful day it is today!"))
print(positive_words)
data = open("project_twitter_data.csv")
for lin in data:
    cnt = get_pos(lin)
    print(cnt)
print(positive_words)
data.close()

