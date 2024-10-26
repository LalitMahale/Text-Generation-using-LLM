# python official image 

FROM python:3.9

# create a working directory

WORKDIR /application

## copy code from current directory to working directory

COPY ./requirements.txt /applicaiton/requirements.txt

## installation command

RUN pip install -r requirements.txt

# set up a new user named "user"

RUN useradd user


#switch to user
USER user

# set home to the users home directory

ENV Home: /home/user \
PATH = /home/user/.local/bin:$PATH


WORKDIR  $HOME/app

## copy the current directory content into the container as $HOME/app setting the owner to home of user

COPY --chown=user . $HOME/app

## start fast api app

CMD [ "uvicorn", "app:app","--host","0.0.0.0", "7862" ]