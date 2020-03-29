FROM python:3.7.6
ENV PYTHONUNBUFFERED 1
WORKDIR /api/
# RUN pip install pipenv
# RUN pipenv install --system
COPY requirements.txt .
RUN apt update
RUN apt install wkhtmltopdf -y
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
