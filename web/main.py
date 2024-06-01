import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.tree import export_graphviz
df=pd.read_csv(r"project2.csv")
df.info()  #provides the meta data info of the dataset
df.columns
#coverting the categorical values, Male -> 1, Female -> 0
df['gender'].replace({'Male' : 1, 'Female': 0}, inplace=True)
dict = {'Yes' : 1, 'No': 0}
df['Partner'].replace(dict, inplace=True)
df['Dependents'].replace(dict, inplace=True)
df['PhoneService'].replace(dict, inplace=True)
df.dtypes
dict1 = {'Yes' : 1, 'No': 0, 'No internet service':2}
df['OnlineSecurity'].replace(dict1, inplace=True)
# df['OnlineSecurity'].unique()
df['OnlineBackup'].replace(dict1, inplace=True)
# df['OnlineBackup'].unique()
df['DeviceProtection'].replace(dict1, inplace=True)
# df['DeviceProtection'].unique()
df['TechSupport'].replace(dict1, inplace=True)
df['StreamingTV'].replace(dict1, inplace=True)
df['StreamingMovies'].replace(dict1, inplace=True)
df['PaperlessBilling'].replace(dict, inplace=True)
df["MultipleLines"].unique()  #get the unique values of the MultipleLines Col.
df['MultipleLines'].replace({'Yes' : 1, 'No': 0, 'No phone service':2}, inplace=True)
df['Contract'].unique()
df['Contract'].replace({'Month-to-month' : 0, 'One year': 1, 'Two year':2}, inplace=True)
df['PaymentMethod'].unique()
x=list(pd.unique(df['PaymentMethod']))

code={}
p=0
for i in x:
    code[i]=p
    p+=1
    
def coder(y):
    return code[y]

df['PaymentMethod']=df['PaymentMethod'].apply(coder)
df['InternetService'].unique()
x=list(pd.unique(df['InternetService']))

code={}
p=0
for i in x:
    code[i]=p
    p+=1
    
def coder(y):
    return code[y]

df['InternetService']=df['InternetService'].apply(coder)
df['Churn'].replace(dict, inplace=True)
#convert the object type into the float type and and values are matching with any char simply replaced with NaN values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Drop rows with NaN values
df.dropna(inplace=True)
df.drop('customerID', axis=1, inplace=True)
df.info()
# Calculate correlations
correlations = df.corr()['Churn'].drop('Churn')

# Sort correlations in descending order
sorted_correlations = correlations.abs().sort_values(ascending=False)

print(sorted_correlations)
# Visualize the distribution of customer tenure, which is the number of months a customer has been with the company.
plt.hist(df['tenure'], bins=10,edgecolor='k')
plt.xlabel('Tenure')
plt.ylabel('Count')
plt.title('Distribution of Customer Tenure')
plt.show()
selected_features = ['Contract', 'tenure', 'OnlineSecurity', 'TechSupport', 'OnlineBackup', 'DeviceProtection', 'PaymentMethod', 'StreamingMovies', 'StreamingTV']
X = df[selected_features]
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_test.shape
reg=RandomForestClassifier()
reg=reg.fit(X_train,y_train)
model=reg.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test,model))
print("precision:",metrics.precision_score(y_test,model))
print("Recall:",metrics.recall_score(y_test,model))
plt.plot(X_test,model)
import streamlit as st
st.title('Welcome To :violet[learn And Build]')
st.header(':green[Telecom Coustomer Churn]')

choice= st.selectbox('Login/Signup',['Login','Sign Up'])
if choice=='Login':
    emaill=st.text_input('Email Adddress')
    Password=st.text_input('Password',type='password')
    
    st.button('Login')

else:
    emaill=st.text_input('Email Adddress')
    First_Name=st.text_input('First Name')
    Last_Name=st.text_input('Last Name')
    Password=st.text_input('Password',type='password')
    st.button('Sign Up')