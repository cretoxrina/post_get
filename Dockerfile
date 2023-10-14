FROM python:3.11
RUN pip install fastapi uvicorn requests
RUN pip install tk
ENV API_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsZWdhbF9lbnRpdHlfaWQiOjcsImNyZWF0ZWRfYXQiOiIyMDIzLTA5LTIxIDA5OjE1OjExLjYwNDQyOSIsInBhc3N3b3JkIjoiOWViZmZkMjQtNzI2Ny00NjZkLTk0MTctZGViMTY4YzZmM2RmIn0.OLy0oUg3rUqWxJp8veLMeOXlbyQrsIJF2BqtsmQYY78"
COPY . /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
