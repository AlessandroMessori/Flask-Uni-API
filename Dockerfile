FROM continuumio/miniconda:latest

WORKDIR /app

COPY . /app


RUN conda env create --name app --file=environment.yml
ENV PATH /opt/conda/envs/app/bin:$PATH
RUN /bin/bash -c "source activate app"

RUN ["chmod","+x","/app/boot.sh"]


EXPOSE 5000

ENTRYPOINT ["sh"]
CMD ["/app/boot.sh"]


