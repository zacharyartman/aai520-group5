# AAI-520 Group 5 Final Project

Chatbot based on [Stanford Question Answering Dataset](https://www.kaggle.com/datasets/stanfordu/stanford-question-answering-dataset)

* Main GPT2 based model is located `standford_qa.ipynb`
* `app/` contains saved model and files for the Chatbot web server
* `/Alternative Models/` contains alternative models exploration and training  

--- 

## Prerequisites 

* `python` and `pip` intalled

## Installation 

### Venv Setup

* Create venv

```sh
python -m venv final_project
```

* Activate venv 

Windows: 

```sh
final_project\Scripts\activate
```

MacOS and Linux: 


```sh
source final_project/bin/activate
```

### Dependencies installation 

```
pip install -r requirements.txt 
```

* When updating dependnecies: 

```
pip freeze > requirements.txt
```
