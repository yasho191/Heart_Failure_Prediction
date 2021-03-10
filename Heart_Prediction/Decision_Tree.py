import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import PowerTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

t = np.array(list(df['creatinine_phosphokinase'])).reshape(-1, 1)
pt = PowerTransformer(method = "yeo-johnson")
creatinine_phosphokinase = pt.fit_transform(t)
df['creatinine_phosphokinase'] = creatinine_phosphokinase

t = np.array(list(df['serum_creatinine'])).reshape(-1, 1)
pt = PowerTransformer(method = "yeo-johnson")
serum_creatinine = pt.fit_transform(t)
df['serum_creatinine'] = serum_creatinine

df.drop(columns = ['sex', 'diabetes'], inplace = True)
X = df.iloc[:, 0:10].values
Y = df['DEATH_EVENT'].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=6)

dclf = DecisionTreeClassifier(criterion='gini',
                              max_depth=15,
                            )
dclf.fit(x_train, y_train)

pickle.dump(dclf, open('dclf.pkl', 'wb'))

clf = pickle.load(open('dclf.pkl', 'rb'))
print(clf.score(x_test, y_test))

