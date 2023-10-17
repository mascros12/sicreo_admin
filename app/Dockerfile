FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ADD odbcinst.ini /etc/

RUN apt-get update -y && apt-get install -y curl gnupg
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update -y && apt-get install -y unixodbc unixodbc-dev tdsodbc freetds-common freetds-bin freetds-dev postgresql python-scipy python-numpy python-pandas
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install mssql-tools msodbcsql17

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN apt-get update

WORKDIR /app
COPY ./openssl.cnf /etc/ssl/openssl.cnf
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

#python manage.py runserver 0.0.0.0:8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


