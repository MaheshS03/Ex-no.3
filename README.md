# Ex-no.3    Univariate Analysis
## AIM:
To perform Univariate Analysis for the given data set.
## EXPLANATION:
Univariate analysis is basically the simplest form to analyze data. Uni means one and this means that the data has only one kind of variable. The major reason for univariate analysis is to use the data to describe. The analysis will take data, summarise it, and then find some pattern in the data
## ALGORITHM:
## STEP-1:
Read the given data.
## STEP-2:
Get the information about the data.
## STEP-3:
Perform Univariate Analysis Techniques for the given dataset.
## STEP-4:
Save the data to the file.
## CODE:
## SUPERTSORE DATA:
## NON-GRAPHICAL:
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

## GRAPHICAL:
### BOX PLOT:
import pandas as pd

import numpy as np

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("SuperStore.csv")

sns.boxplot(x="Row ID",data=df)

### COUNT PLOT:
import pandas as pd

import numpy as np

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("SuperStore.csv")

sns.countplot(x="Row ID",data=df)

### DIST PLOT:
import pandas as pd

import numpy as np

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("SuperStore.csv")

sns.distplot(df["Row ID"])

### HIST PLOT:
import pandas as pd

import numpy as np

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("SuperStore.csv")

sns.histplot(x="Row ID",data=df)

## DIABETES DATA:
### NON-GRAPHICAL:
import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

df.info()

print("\n")

df.dtypes

import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

df['Glucose'].value_counts()

import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

df['BloodPressure'].value_counts()

import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

df.describe()

import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

df.skew()

import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

df.kurtosis()

## GRAPHICAL:
### BOX PLOT:
import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

sns.boxplot(x="Glucose",data=df)

### COUNT PLOT:
import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

sns.countplot(x="Glucose",data=df)

### DIST PLOT:
import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

sns.distplot(df["Glucose"])

### HIST PLOT:
import pandas as pd

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("diabetes.csv")

sns.histplot(x="Glucose",data=df)

## CODE:
## NON-GRAPHICAL:
![Screenshot (54)](https://user-images.githubusercontent.com/127846109/232197333-11761c33-9c5c-4834-a0dc-6cec64311cad.png)

![Screenshot (55)](https://user-images.githubusercontent.com/127846109/232197405-2a2115bf-fdce-4038-8c9f-fc577300d113.png)

![Screenshot (56)](https://user-images.githubusercontent.com/127846109/232197412-43c37249-6cac-4c47-8e52-639eac203233.png)

![Screenshot (57)](https://user-images.githubusercontent.com/127846109/232197420-65117f4d-d8dc-4015-99fb-9572e8597a01.png)

![Screenshot (58)](https://user-images.githubusercontent.com/127846109/232197428-fec4a408-510f-4b52-a3ee-74c6d1deb6e5.png)

![Screenshot (59)](https://user-images.githubusercontent.com/127846109/232197440-610efce6-51fd-461e-b55a-ada6a7aa9ed3.png)

![Screenshot (60)](https://user-images.githubusercontent.com/127846109/232197449-55802ee9-befb-4d10-b333-c08358fc3cdc.png)

## GRAPHICAL:
### BOX PLOT:
![Screenshot (61)](https://user-images.githubusercontent.com/127846109/232199122-85c4a65c-9d9b-4e2d-a71a-bab432ab98af.png)

### COUNT PLOT:
![Screenshot (62)](https://user-images.githubusercontent.com/127846109/232199139-f8cb1748-957f-44c5-92e4-646ad2e66c1b.png)

### DIST PLOT:
![Screenshot (63)](https://user-images.githubusercontent.com/127846109/232199156-8d69b5d5-d45d-471d-8b04-45b8d41a8f72.png)

### HIST PLOT:
![Screenshot (64)](https://user-images.githubusercontent.com/127846109/232199174-9ae45b7b-2dec-43fe-86ab-8363cd46398e.png)

## DIABETES DATA SET:
## NON-GRAPHICHAL:
![Screenshot (65)](https://user-images.githubusercontent.com/127846109/232200609-3b420fc7-9524-4abd-a5d7-c9ef7c9f9b41.png)

![Screenshot (66)](https://user-images.githubusercontent.com/127846109/232200595-468f8b0e-9987-47b4-82b9-e8ad3c056f9b.png)

![Screenshot (67)](https://user-images.githubusercontent.com/127846109/232200616-2c37baf8-8317-4d41-9fea-ad421e9d6d8a.png)

![Screenshot (68)](https://user-images.githubusercontent.com/127846109/232200625-ebf16218-234a-4585-b461-dd122e9c370b.png)

![Screenshot (69)](https://user-images.githubusercontent.com/127846109/232200668-9f308b18-8a2b-4d6a-b167-848309e025ff.png)

![Screenshot (70)](https://user-images.githubusercontent.com/127846109/232200713-698fb74b-1b66-4e29-871e-2834075ba4df.png)

## GRAPHICAL:
### BOX PLOT:
![Screenshot (71)](https://user-images.githubusercontent.com/127846109/232201065-81484b7c-2785-44ab-b6ad-284b8554c2c7.png)

### COUNT PLOT:
![Screenshot (72)](https://user-images.githubusercontent.com/127846109/232201072-4e74aa0e-e97f-4818-ac93-3f5e3c662553.png)

### DIST PLOT:
![Screenshot (73)](https://user-images.githubusercontent.com/127846109/232201081-e8a704bc-e112-42c3-8cc3-1ebd68445822.png)

### HIST PLOT:
![Screenshot (74)](https://user-images.githubusercontent.com/127846109/232201084-f366a5be-1dc1-4e8f-94d1-ee2754aa912e.png)

## RESULTS:
Thus the Univariate Analysis for the given data set is executed and output was verified successfully.

