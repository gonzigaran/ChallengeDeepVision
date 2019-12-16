FROM jupyter/base-notebook

USER root

RUN pip install --no-cache \
  scikit-learn \
  numpy \
  pandas

USER $NB_UID
