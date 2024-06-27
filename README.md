# private_chat



## Getting started

This simple project is made in flask and can easily be integrated with heroku to create your own private chatgpt + dalle.

## Install all dependencies with:


```
pip install -r requirements.txt
```

## Create a new .env file following the examples in .exampleenv

You need to create an account at OPENAI and retrieve the following information:

OPENAI_API_KEY="YOUR API KEY"

OPENAI_ORGANIZATION_NAME="YOUR ORGANIZATION NAME"

OPENAI_ORGANIZATION_ID="YOUR ORGANIZATION ID"

OPENAI_PROJECT="YOUR PROJECT NAME"


## Integrate with heroku:

After creating a heroku account

```
heroku login
heroku create your-app-name
```

To update your heroku app:
```
git add .
git commit -m "Message"
git push heroku main
heroku open
```