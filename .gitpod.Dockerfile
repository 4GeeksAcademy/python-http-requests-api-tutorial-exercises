FROM gitpod/workspace-full

USER gitpod

RUN npm pip install pytest==4.4.2 mock pytest-testdox
RUN npm i learnpack -g && learnpack plugins:install learnpack-python
