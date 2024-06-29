FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

RUN apt-get update && apt-get install -y postgresql postgresql-contrib

USER vscode

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER vscode WITH SUPERUSER PASSWORD 'password';" &&\
    createdb -O vscode airbnb

EXPOSE 5432
