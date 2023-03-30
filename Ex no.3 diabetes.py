import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
print(df)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df.info()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df.dtypes
 
import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Row ID'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Order ID'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Order Date'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Ship Date'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Ship Mode'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Customer ID'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Customer Name'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Segment'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Country'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['City'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['State'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Postal Code'].value_counts()

import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Region'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Product ID'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Category'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Sub-Category'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Product Name'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df['Sales'].value_counts()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df.describe()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df.skew()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("SuperStore.csv")
df.kurtosis()

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="Glucose",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="BloodPressure",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="SkinThickness",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="Insulin",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="BMI",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="DiabetesPedigreeFunction",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="Age",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.boxplot(x="Outcome",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="Glucose",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="BloodPressure",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="SkinThickness",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="Insulin",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="BMI",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="DiabetesPedigreeFunction",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="Age",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.countplot(x="Outcome",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["Glucose"])


import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["BloodPressure"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["SkinThickness"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["Insulin"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["BMI"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["DiabetesPedigreeFunction"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["Age"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.distplot(df["Outcome"])

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="Glucose",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="BloodPressure",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="SkinThickness",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="Insulin",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="BMI",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="DiabetesPedigreeFunction",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="Age",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.histplot(x="Outcome",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="Glucose",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="BloodPressure",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="SkinThickness",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="Insulin",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="BMI",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="DiabetesPedigreeFunction",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="Age",data=df)

import pandas as pd
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("diabetes.csv")
sns.displot(x="Outcome",data=df)
