kind: pipeline
name: default

steps:
- name: test
  image: python
  commands:
  - pip install pandas
  - 2+3
