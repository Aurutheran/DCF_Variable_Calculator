
# Variable Discounted Cashflow Calculator 🧮

Hello fellow enthusiasts, have you ever wondered how you could safely value an stock investment you are thinking of purchasing. Look no further! We have created a virtual DCF model that includes both fixed and variable growth rates for key financial factors. 


## Acknowledgements

 - [Stock-Analysis Financial Documents](https://stockanalysis.com/)
 - [Discounted Cash Flow (DCF) Theory](https://www.investopedia.com/terms/d/dcf.asp)
 - [FastAPI Reference](https://fastapi.tiangolo.com/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Aurutheran/DCF_Variable_Calculator
```

Go to the project directory

```bash
  cd DCF_Variable_Calculator
```

Install following dependencies

```bash
  fastapi==0.90.1
  - pydantic [required: >=1.6.2,<2.0.0,!=1.8.1,!=1.8,!=1.7.3,!=1.7.2,!=1.7.1,!=1.7, installed: 1.10.4]
    - typing-extensions [required: >=4.2.0, installed: 4.4.0]
  - starlette [required: >=0.22.0,<0.24.0, installed: 0.23.1]
    - anyio [required: >=3.4.0,<5, installed: 3.6.2]
      - idna [required: >=2.8, installed: 3.4]
      - sniffio [required: >=1.1, installed: 1.3.0]
httptools==0.5.0
ipykernel==6.21.3
  - comm [required: >=0.1.1, installed: 0.1.2]
    - traitlets [required: >=5.3, installed: 5.9.0]
  - debugpy [required: >=1.6.5, installed: 1.6.6]
  - ipython [required: >=7.23.1, installed: 8.11.0]
    - backcall [required: Any, installed: 0.2.0]
    - colorama [required: Any, installed: 0.4.6]
    - decorator [required: Any, installed: 5.1.1]
    - jedi [required: >=0.16, installed: 0.18.2]
      - parso [required: >=0.8.0,<0.9.0, installed: 0.8.3]
    - matplotlib-inline [required: Any, installed: 0.1.6]
      - traitlets [required: Any, installed: 5.9.0]
    - pickleshare [required: Any, installed: 0.7.5]
    - prompt-toolkit [required: >=3.0.30,<3.1.0,!=3.0.37, installed: 3.0.38]
      - wcwidth [required: Any, installed: 0.2.6]
    - pygments [required: >=2.4.0, installed: 2.14.0]
    - stack-data [required: Any, installed: 0.6.2]
      - asttokens [required: >=2.1.0, installed: 2.2.1]
        - six [required: Any, installed: 1.16.0]
      - executing [required: >=1.2.0, installed: 1.2.0]
      - pure-eval [required: Any, installed: 0.2.2]
    - traitlets [required: >=5, installed: 5.9.0]
  - jupyter-client [required: >=6.1.12, installed: 8.0.3]
    - jupyter-core [required: >=4.12,!=5.0.*, installed: 5.2.0]
      - platformdirs [required: >=2.5, installed: 3.1.1]
      - pywin32 [required: >=1.0, installed: 305]
      - traitlets [required: >=5.3, installed: 5.9.0]
    - python-dateutil [required: >=2.8.2, installed: 2.8.2]
      - six [required: >=1.5, installed: 1.16.0]
    - pyzmq [required: >=23.0, installed: 25.0.1]
    - tornado [required: >=6.2, installed: 6.2]
    - traitlets [required: >=5.3, installed: 5.9.0]
  - jupyter-core [required: >=4.12,!=5.0.*, installed: 5.2.0]
    - platformdirs [required: >=2.5, installed: 3.1.1]
    - pywin32 [required: >=1.0, installed: 305]
    - traitlets [required: >=5.3, installed: 5.9.0]
  - matplotlib-inline [required: >=0.1, installed: 0.1.6]
    - traitlets [required: Any, installed: 5.9.0]
  - nest-asyncio [required: Any, installed: 1.5.6]
  - packaging [required: Any, installed: 23.0]
  - psutil [required: Any, installed: 5.9.4]
  - pyzmq [required: >=20, installed: 25.0.1]
  - tornado [required: >=6.1, installed: 6.2]
  - traitlets [required: >=5.4.0, installed: 5.9.0]
Jinja2==3.1.2
  - MarkupSafe [required: >=2.0, installed: 2.1.2]
lxml==4.9.2
matplotlib==3.6.3
  - contourpy [required: >=1.0.1, installed: 1.0.7]
    - numpy [required: >=1.16, installed: 1.24.1]
  - cycler [required: >=0.10, installed: 0.11.0]
  - fonttools [required: >=4.22.0, installed: 4.38.0]
  - kiwisolver [required: >=1.0.1, installed: 1.4.4]
  - numpy [required: >=1.19, installed: 1.24.1]
  - packaging [required: >=20.0, installed: 23.0]
  - pillow [required: >=6.2.0, installed: 9.4.0]
  - pyparsing [required: >=2.2.1, installed: 3.0.9]
  - python-dateutil [required: >=2.7, installed: 2.8.2]
    - six [required: >=1.5, installed: 1.16.0]
pandas==1.5.3
  - numpy [required: >=1.23.2, installed: 1.24.1]
  - numpy [required: >=1.21.0, installed: 1.24.1]
  - python-dateutil [required: >=2.8.1, installed: 2.8.2]
    - six [required: >=1.5, installed: 1.16.0]
  - pytz [required: >=2020.1, installed: 2022.7.1]
pip==22.3.1
pipdeptree==2.7.0
PyAutoGUI==0.9.53
  - mouseinfo [required: Any, installed: 0.1.3]
    - pyperclip [required: Any, installed: 1.8.2]
  - pygetwindow [required: >=0.0.5, installed: 0.0.9]
    - pyrect [required: Any, installed: 0.2.0]
  - pymsgbox [required: Any, installed: 1.0.9]
  - pyscreeze [required: >=0.1.21, installed: 0.1.28]
  - PyTweening [required: >=1.0.1, installed: 1.0.4]
pynput==1.7.6
  - six [required: Any, installed: 1.16.0]
pyOpenSSL==23.0.0
  - cryptography [required: >=38.0.0,<40, installed: 39.0.0]
    - cffi [required: >=1.12, installed: 1.15.1]
      - pycparser [required: Any, installed: 2.21]
PySocks==1.7.1
python-dotenv==0.21.1
python-multipart==0.0.5
  - six [required: >=1.4.0, installed: 1.16.0]
PyYAML==6.0
selenium==4.8.0
  - certifi [required: >=2021.10.8, installed: 2022.12.7]
  - trio [required: ~=0.17, installed: 0.22.0]
    - async-generator [required: >=1.9, installed: 1.10]
    - attrs [required: >=19.2.0, installed: 22.2.0]
    - cffi [required: >=1.14, installed: 1.15.1]
      - pycparser [required: Any, installed: 2.21]
    - idna [required: Any, installed: 3.4]
    - outcome [required: Any, installed: 1.2.0]
      - attrs [required: >=19.2.0, installed: 22.2.0]
    - sniffio [required: Any, installed: 1.3.0]
    - sortedcontainers [required: Any, installed: 2.4.0]
  - trio-websocket [required: ~=0.9, installed: 0.9.2]
    - async-generator [required: >=1.10, installed: 1.10]
    - trio [required: >=0.11, installed: 0.22.0]
      - async-generator [required: >=1.9, installed: 1.10]
      - attrs [required: >=19.2.0, installed: 22.2.0]
      - cffi [required: >=1.14, installed: 1.15.1]
        - pycparser [required: Any, installed: 2.21]
      - idna [required: Any, installed: 3.4]
      - outcome [required: Any, installed: 1.2.0]
        - attrs [required: >=19.2.0, installed: 22.2.0]
      - sniffio [required: Any, installed: 1.3.0]
      - sortedcontainers [required: Any, installed: 2.4.0]
    - wsproto [required: >=0.14, installed: 1.2.0]
      - h11 [required: >=0.9.0,<1, installed: 0.14.0]
  - urllib3 [required: ~=1.26, installed: 1.26.14]
setuptools==65.5.0
urllib3-secure-extra==0.1.0
uvicorn==0.20.0
  - click [required: >=7.0, installed: 8.1.3]
    - colorama [required: Any, installed: 0.4.6]
  - h11 [required: >=0.8, installed: 0.14.0]
watchfiles==0.18.1
  - anyio [required: >=3.0.0, installed: 3.6.2]
    - idna [required: >=2.8, installed: 3.4]
    - sniffio [required: >=1.1, installed: 1.3.0]
websockets==10.4
```

Example of installing dependencies
```bash
    pip install uvicorn
```
Start the server

```bash
  uvicorn main:app --reload
```

Open the website
```bash
INFO:     Will watch for changes in these directories: ['D:\\YourDirectoryWhereAppIsInstalled']
INFO:     Uvicorn running on {Your URL} (Press CTRL+C to quit)
INFO:     Started reloader process [2556] using WatchFiles
INFO:     Started server process [22556]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Stopping reloader process [2556]
```


## Authors
- [@Ajithan](https://github.com/aurutheran)
- [@Ruthvik](https://github.com/77ruthvik)


## Roadmap

- Converted from terminal to GUI application

- Adding support for other stock markets

