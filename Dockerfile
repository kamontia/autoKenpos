FROM python:3
MAINTAINER kamontia

# apt-get
RUN apt-get update -yq && apt-get install -yq wget zlib1g-dev

# pip install
RUN pip install --upgrade pip && pip install selenium

# Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |  apt-key add - \
    && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Set working directory
WORKDIR /root/

# Chrome driver via wget
RUN wget -q https://chromedriver.storage.googleapis.com/73.0.3683.20/chromedriver_linux64.zip -O chromedriver.zip \
    && unzip chromedriver.zip && chmod +x chromedriver && mv chromedriver /usr/local/bin && rm chromedriver.zip

# Remove cache & workfile
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Set encoding in Python
ENV PYTHONIOENCODING "utf-8"

# Copy
RUN mkdir -p /root/app
COPY ["./app","/root/app"]
