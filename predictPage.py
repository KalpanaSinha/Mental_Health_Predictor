import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split   # used for splitting the training and testing data
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

# models
import pickle

def genderconversion(gender):
	if(gender == '0'):
		gender = "Female"
	elif gender == '1':
		gender = "Male"
	else:
		gender = "Trans"
	return gender

def familyconversion(family_history):
	if(family_history == '0'):
		family_history = "No"
	else:
		family_history = "Yes"
	return family_history

def benefitconversion(benefits):
	if(benefits == '0'):
		benefits = "Don't Know"
	elif benefits == '1':
		benefits = "Yes"
	else:
		benefits = "No"
	return benefits

def careconversion(care_options):
	if(care_options == '0'):
		care_options = "No"
	elif care_options == '1':
		care_options = "Not Sure"
	else:
		care_options = "Yes"
	return care_options

def leaveconversion(leave):
	if(leave == '0'):
		leave = "No Idea"
	elif leave == '1':
		leave = "Somewhat difficult"
	elif leave == '2':
		leave = "Somewhat easy"
	elif leave == '3':
		leave = "Very difficult"
	else:
		leave = "Very easy"
	return leave

def anonymconversion(anonymity):
	if(anonymity == '0'):
		anonymity = "Don't Know"
	elif anonymity == '1':
		anonymity = "No"
	else:
		anonymity = "Yes"
	return anonymity

def workconversion(work):
	if(work == '0'):
		work = "Don't Know"
	elif work == '1':
		work = "Never"
	elif work == '2':
		work = "Often"
	elif work == '3':
		work = "Rarely"
	else:
		work = "Sometimes"
	return work

	

df = pd.read_csv('mentalHealthSurvey.csv')

df = df.drop(['comments'], axis= 1)
df = df.drop(['state'], axis= 1)
df = df.drop(['Timestamp'], axis= 1)

defaultInt = 0
defaultString = 'NaN'
defaultFloat = 0.0

# Create lists by data type
intFeatures = ['Age']
stringFeatures = ['Gender', 'Country', 'self_employed', 'family_history', 'treatment', 'work_interfere',
                 'no_employees', 'remote_work', 'tech_company', 'anonymity', 'leave', 'mental_health_consequence',
                 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview',
                 'mental_vs_physical', 'obs_consequence', 'benefits', 'care_options', 'wellness_program',
                 'seek_help']
floatFeatures = []

# Clean the NaN's
for feature in df:
    if feature in intFeatures:
        df[feature] = df[feature].fillna(defaultInt)
    elif feature in stringFeatures:
        df[feature] = df[feature].fillna(defaultString)
    elif feature in floatFeatures:
        df[feature] = df[feature].fillna(defaultFloat)

male_str = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis man", "Cis Male", "cis male"]
trans_str = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means"]           
female_str = ["cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail"]

for (row, col) in df.iterrows():
    if str.lower(col.Gender) in male_str:
        df['Gender'].replace(to_replace=col.Gender, value='male', inplace=True)
    if str.lower(col.Gender) in female_str:
        df['Gender'].replace(to_replace=col.Gender, value='female', inplace=True)
    if str.lower(col.Gender) in trans_str:
        df['Gender'].replace(to_replace=col.Gender, value='trans', inplace=True)

#Get rid of bullshit
stk_list = ['A little about you', 'p']
df = df[~df['Gender'].isin(stk_list)]

#complete missing age with mean
df['Age'].fillna(df['Age'].median(), inplace = True)

# Filling with median() for age values < 18 and > 120
s = pd.Series(df['Age'])
s[s<18] = df['Age'].median()
df['Age'] = s
s = pd.Series(df['Age'])
s[s>120] = df['Age'].median()
df['Age'] = s

#Ranges of Age
df['age_range'] = pd.cut(df['Age'], [0,20,30,65,100], labels=["0-20", "21-30", "31-65", "66-100"], include_lowest=True)
print(df.shape)

df['self_employed'] = df['self_employed'].replace([defaultString], 'No')

df['work_interfere'] = df['work_interfere'].replace([defaultString], 'Don\'t know' )

df = df.drop(['Country'], axis= 1)
print(df.shape)

labelDict = {}
for feature in df:
    le = preprocessing.LabelEncoder()
    le.fit(df[feature])
    le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    df[feature] = le.transform(df[feature])
    # Get labels
    labelKey = 'label_' + feature
    labelValue = [*le_name_mapping]
    labelDict[labelKey] =labelValue
    
print(df.shape)

feature_cols = ['Age',	'Gender',	'self_employed',	'family_history',	'treatment',	'work_interfere',	'no_employees',	'remote_work',	'tech_company',	'benefits',	'care_options',	'wellness_program',	'seek_help',	'anonymity',	'leave',	'mental_health_consequence',	'phys_health_consequence',	'coworkers', 'supervisor',	'mental_health_interview',	'phys_health_interview',	'mental_vs_physical',	'obs_consequence',	'age_range']
X = df[feature_cols]
y = df.treatment

# split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0, shuffle=False)

print(X_train.shape)
print(X_test.shape)


#feature_scaling

# Scaling Age
scaler = MinMaxScaler()
X_train['Age'] = scaler.fit_transform(X_train[['Age']])

# Scaling Age
scaler = MinMaxScaler()
X_test['Age'] = scaler.fit_transform(X_test[['Age']])


#Puting the important features inside a column and creating a separate dataframe which will be fed into the model
selected_cols = X_train[['Age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave', 'work_interfere']]
X_train_top8 = selected_cols.copy()

#Puting the important features inside a column and creating a separate dataframe which will be fed into the model
selected_cols = X_test[['Age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave', 'work_interfere']]
X_test_top8 = selected_cols.copy()


# train a logistic regression model on the training set
clf = GradientBoostingClassifier()
clf.fit(X_train_top8, y_train)

pickle.dump(clf, open('model.pkl', 'wb'))
