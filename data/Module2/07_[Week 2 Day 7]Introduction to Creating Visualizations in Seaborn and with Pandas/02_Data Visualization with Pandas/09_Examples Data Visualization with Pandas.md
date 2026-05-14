# Examples: Data Visualization with Pandas

# Examples: Data Visualization with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Examples: Data Visualization with Pandas

Icon Progress Bar (browser only)

1 min read

Let’s look at some examples of visualizing data using Pandas commands. Below are the completed visualizations from the conceptualization table on the Defining Data Visualization with Pandas page.

### Line Plot

```
import pandas as pd  
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})  
df.plot(kind='line')
```

**Output:**

![Line plot output for the python code](https://moringa.instructure.com/courses/1406/files/624797/download)

### Scatter Plot

```
import pandas as pd  
  
df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [5, 6, 7, 8]})  
  
df.plot(kind='scatter', x='x', y='y')
```

**Output:**

![Scatter plot output of the python code](https://moringa.instructure.com/courses/1406/files/625155/download)

### Bar Chart

```
import pandas as pd  
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})  
df.plot(kind='bar')
```

**Output:**

**![Bar chart output for python code](https://moringa.instructure.com/courses/1406/files/624781/download)**

### Histogram

```
import numpy as np  
import pandas as pd  
  
data = np.random.normal(0, 1, 1000)  
df = pd.DataFrame({'data': data})  
df['data'].plot(kind='hist')
```

**Output:**

**![Histogram output for python code](https://moringa.instructure.com/courses/1406/files/624774/download)**

### Box Plot

```
import pandas as pd  
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8], 'B': [5, 6, 7, 8, 9, 10, 11, 12]})  
df.plot(kind='box')
```

**Output:**

**![Box plot output for python code](https://moringa.instructure.com/courses/1406/files/624784/download)**

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243625

Scraped At: 2026-05-14T21:00:20.947061
