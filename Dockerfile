FROM python:3.8-alpine

RUN \
  apk update -q \
  && apk add -q \
  chromium \
  chromium-chromedriver

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "tests/", "--driver", "Chrome", "--html=reports/report.html", "--self-contained-html"]
