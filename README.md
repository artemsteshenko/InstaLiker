# InstaLiker
Selenium bot for viewing stories and liking them 
```
python3 main.py login password
```

More about StoriesViewer:
```
from selenium import webdriver
from loguru import logger
from stories_viewer import StoriesViewer

driver = webdriver.Safari()
viewer = StoriesViewer(driver, logger)

for account_name in users_list:
    viewer.run(account_name=account_name, with_liking=True)
```

