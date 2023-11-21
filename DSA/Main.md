---
Author: Vighnesh Nayak
Date: 01/11/2023
Topic: DSA
tags:
  - hide
  - main
---
# Main
---

```dataview
table  Topic, Author, Date, dateformat(file.mtime,"dd/MM/yyyy") as Modified
from "DSA" where file.name!="Main" sort Date desc 
```






