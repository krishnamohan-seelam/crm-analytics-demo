FROM python:3.10.6
RUN mkdir -p /crm-analytics-demo
COPY requirements.txt ./crm-analytics-demo/requirements.txt
RUN pip3 install -r /crm-analytics-demo/requirements.txt
COPY app/ /crm-analytics-demo/app/
COPY config/ /crm-analytics-demo/config/
COPY data/ /crm-analytics-demo/data/
COPY images/ /crm-analytics-demo/images/
EXPOSE 8501/
WORKDIR /crm-analytics-demo
ENTRYPOINT ["streamlit", "run"]
CMD ["app/dashboard.py"]