FROM python:3.6-slim

MAINTAINER Alan li macroldj

WORKDIR /workspace/
ADD ./requirements.txt /tmp/requirements.txt
ADD jupyterserver.sh jupyterserver.sh
RUN pip install --no-cache-dir  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /tmp/requirements.txt && rm -rf /tmp/requirements.txt && mkdir -p /root/workspace
ADD jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
VOLUME ["/data"]
CMD [ "bash","webServer.sh" ]