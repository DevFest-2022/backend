FROM python:3.7
WORKDIR /app
RUN pip install flask
RUN pip install python-dotenv
RUN pip install requests
RUN pip install flask_cors
COPY . .
CMD python main.py