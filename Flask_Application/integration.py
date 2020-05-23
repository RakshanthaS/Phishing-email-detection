
import pickle
import pandas as pd
import numpy as np
import sklearn
def text_prediction(text):
    filename = 'finalized1_text_model.sav'
    loaded_model_text = pickle.load(open(filename, 'rb'))
    data=[['1',text]]
    df = pd.DataFrame(data,columns = ['No','content'])
    predictions = loaded_model_text.predict(df.content)
    print(predictions)
    text_pred=predictions[0]
    pred_prob=loaded_model_text.predict_proba(df.content)
    print("text prediction" +str(text_pred))
    print("probability of text" +str(pred_prob))
    x=np.shape(pred_prob)
    pred_prob1=[]
    for i in range(0,x[0]):
        for j in range(0,x[1]):
            pred_prob1.append(round(pred_prob[i][j],5))
    text_prob=pred_prob1[1]  
    return text_prob,text_pred
def long_url(l):
    l= str(l)
    """This function is defined in order to differntiate website based on the length of the URL"""
    if len(l) < 54:
        return 0
    elif len(l) >= 54 and len(l) <= 75:
        return 2
    return 1

def have_at_symbol(l):
    """This function is used to check whether the URL contains @ symbol or not"""
    if "@" in str(l):
        return 1
    return 0

def redirection(l):
    """If the url has symbol(//) after protocol then such URL is to be classified as phishing """
    if "//" in str(l):
        return 1
    return 0

def prefix_suffix_seperation(l):
    if '-' in str(l):
        return 1
    return 0
	
def sub_domains(l):
    l= str(l)
    if l.count('.') < 3:
        return 0
    elif l.count('.') == 3:
        return 2
    return 1
	
def url_prediction(list):
	df=pd.DataFrame(data=list)
	df.rename(columns={0:"URL"})
	seperation_of_protocol = df[0].str.split("://",expand = True) #expand argument in the split method will give you a new column
	seperation_domain_name = seperation_of_protocol[1].str.split("/",1,expand=True)
	seperation_domain_name.columns=["domain_name","address"]
	splitted_data = pd.concat([seperation_of_protocol[0],seperation_domain_name],axis=1)
	splitted_data.columns = ['protocol','domain_name','address']
	splitted_data['long_url'] = df[0].apply(long_url) 
	splitted_data['having_@_symbol'] = df[0].apply(have_at_symbol)
	splitted_data['redirection_//_symbol'] = seperation_of_protocol[1].apply(redirection)
	splitted_data['prefix_suffix_seperation'] = seperation_domain_name['domain_name'].apply(prefix_suffix_seperation)
	splitted_data['sub_domains'] = splitted_data['domain_name'].apply(sub_domains)
	features = ['long_url', 'having_@_symbol', 'redirection_//_symbol','prefix_suffix_seperation','sub_domains']
	X=splitted_data[features]
	filename = 'urlphishing.sav'
	loaded_model = pickle.load(open(filename, 'rb'))
	ls = loaded_model.predict(X)
	print(ls)
	url_pred_prob = loaded_model.predict_proba(X)
	print(url_pred_prob)
	tup=np.shape(url_pred_prob)
	n=tup[1]-1
	x=url_pred_prob[:,[n]]
	url_prob=float(max(x))
	url_pred=findMajority(ls,len(ls))
	print("Url prediction" +str(url_pred))
	return url_prob,url_pred

def findMajority(arr, n): 
    maxCount = 0; 
    index = -1 # sentinels 
    for i in range(n): 
        count = 0
        for j in range(n): 
          
            if(arr[i] == arr[j]): 
                count += 1
          
        # update maxCount if count of  
        # current element is greater 
        if(count > maxCount): 
          
            maxCount = count 
            index = i 
      
    # if maxCount is greater than n/2  
    # return the corresponding element  
    if (maxCount > n//2): 
        in1=arr[index]
      
    else: 
        print("No Majority Element")
        in1=0
    return in1


	