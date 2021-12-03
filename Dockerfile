FROM python
EXPOSE 5000
copy main.py .
copy books.json .
copy templates .
RUN pip install flask
CMD python main.py