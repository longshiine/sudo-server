ARG PYTORCH="1.7.0"
ARG CUDA="11.0"
ARG CUDNN="8"

FROM python

RUN conda clean --all
WORKDIR /workspace

RUN pip install --upgrade pip
RUN pip install flask==1.1.2 flask_cors==3.0.9
RUN pip install flask_restful_swagger_2==0.35

WORKDIR /app
COPY ./src ./
