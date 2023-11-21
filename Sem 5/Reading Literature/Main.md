---
Author: Vighnesh Nayak
Date: 28/10/2023
Course: Reading Literature
tags:
  - hide
  - main
---
# Main
---

```dataview
table  regexreplace(file.folder, ".*\/([^\/]+)$", "$1") as Play, Author, Date, dateformat(file.mtime,"dd/MM/yyyy") as Modified
from "Sem 5/Reading Literature" where file.name!="Main" sort file.ctime asc 
```






