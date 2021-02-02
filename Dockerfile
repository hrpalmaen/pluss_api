FROM python:3.7.6
ENV PYTHONUNBUFFERED 1
WORKDIR /api/
# RUN pip install pipenv
# RUN pipenv install --system
COPY requirements.txt .
RUN apt update &&  apt install wkhtmltopdf -y
RUN pip install -r requirements.txt
RUN ls
COPY . .
EXPOSE 8933
