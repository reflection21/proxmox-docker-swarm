FROM python:3.13-alpine AS builder

# RUN apk add --no-cache build-base

WORKDIR /app

COPY requirements.txt .

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

COPY . .


FROM python:3.13-alpine

WORKDIR /app

RUN addgroup --system flaskuser && \
    adduser --system --shell /bin/false --ingroup flaskuser --no-create-home flaskuser 

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

RUN chown -R flaskuser:flaskuser /app

EXPOSE 5000

USER flaskuser

ENTRYPOINT ["python"]
CMD ["app.py"]
