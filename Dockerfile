FROM continuumio/miniconda:latest

WORKDIR /app

COPY . /app


RUN conda env create --name app --file=environment.yml
ENV PATH /opt/conda/envs/app/bin:$PATH
RUN /bin/bash -c "source activate app"


EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["/app/app.py"]
