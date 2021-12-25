FROM arm32v7/python
WORKDIR /app
COPY . .
RUN chmod 755 ./start.sh
RUN python -m pip install --upgrade pip --quiet
RUN pip install -r requirements.txt && rm requirements.txt
CMD ["./start.sh"]