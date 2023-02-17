# Static Website Generator

* This a python script that generate a static website using markdown files.
* The script uses three markdown files which are then transformed to html files.
* The files convert as follows
  * [homepage.md](markdowns/homepage.md) -> [homepage.html](markdowns/generated/homepage.html)
  * [articles.md](markdowns/articles.md) -> [articles.html](markdowns/generated/articles.html)
  * [about.md](markdowns/about.md) -> [about.html](markdowns/generated/about.html)

# To Run this script
  * Install python [Download Python](https://www.python.org/downloads/)
  * Use pip to install the required library
```shell
pip install markdown
```
  * Change the location path of the markdown folder
  * I recommend you use the full path from your drive
```python
path = "C:\\Users\\username\..\markdowns"
```

