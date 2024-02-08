# 
FROM python:3.11

# 
COPY requirements.txt app/requirements.txt

# 
WORKDIR /app

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . /app

#
ENTRYPOINT ["streamlit","run"]

CMD ["modeling.py"]