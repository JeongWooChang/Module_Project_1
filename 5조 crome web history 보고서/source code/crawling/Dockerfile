FROM python
WORKDIR /code
RUN apt-get update -y && apt-get upgrade -y
RUN pip install pymysql 
COPY . /code/
RUN chmod 777 /code/run.sh
CMD /code/run.sh