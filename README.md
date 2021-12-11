# 2301853786_PasteBin Sebagai C&C
Kondisi ini adalah step post-exploitation. Asumsi agent sudah terpasang di host. Buatlah script python dan taruh di git.
 
Lakukan Host Reconnaissance pada agent.
Kumpulkan info mengenai Hostname, User yang login, dan Current Privileges
 
Upload informasi yang di dapat ke pastebin dengan sebelumnya di encode Base64.

## Jawaban (Source Code)
Source code terlampir dalam : 2301853786_GSLC_Pastebin.py

## Note
api_dev_key didapat dengan melakukan sign up pada Pastebin

```python
api_dev_key = "[UNIQUE_API_DEVELOPERS_KEY]"
```

## Reference
https://programmerall.com/article/90051358161/
