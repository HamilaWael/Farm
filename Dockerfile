FROM python:3.9.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["farm.py"]