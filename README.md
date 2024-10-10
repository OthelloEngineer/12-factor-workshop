# 12-factor-workshop

This repository contains a few exercises for the 12-factor-workshop held by Joakim.

To start the exercise application, you must first install the following `Python3` packages with `pip` by using the following command: (You may want to create a virtual env first...)
```bash
pip install Flask python-dotenv mysql-connector-python numpy
```

To initialize the directory for the logging exercise run: Make sure that you are in the same dir as the bash script :)
```bash
sudo ./setup.sh
```
---

After that, you are able to run the application with the following command:
```bash
python main.py
```

NOTICE! On Linux you will have to use the following instead:
```bash
python3 main.py
```
