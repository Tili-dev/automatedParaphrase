
# Automated Paraphrasing API

We offer a tool to automatically generate paraphrases.

## Features

- Automated translation using [Yandex Translate API](https://tech.yandex.com/translate/) and [MyMemory API](https://mymemory.translated.net/doc/)
- Filter out bad paraphrases through [Hugging Face's transformers BERT model](https://huggingface.co/transformers/model_doc/bert.html#bertmodel) and [Universal Sentence Encoding](https://tfhub.dev/google/universal-sentence-encoder/4) semantic similarity
- Remove deduplicate through [Hugging Face's transformers BERT model](https://huggingface.co/transformers/model_doc/bert.html#bertmodel)

## Requirements


Installation & Usage
---------------
In order to generate paraphrases, follow these steps:

1. Create and activate a virtual environment using **Python 3** version:
    * `Linux`

        Create the virtual environment:    ```virtualenv -p python3 venv ```
        
        Activate the virtual environment: ``` source ./env/bin/activate ```

    * `Windows`
    
        Create the virtual environment: ``` c:\>c:\Python35\python -m venv c:\path\to\myenv ```
         >Unlike most Unix systems and services, Windows does not include a system supported installation of Python. [#Python installation and Creation of virtual environments](https://docs.python.org/3/using/windows.html#using-on-windows)
         
      Activate the virtual environment: ``` .\env\Scripts\activate.bat ```
2. Install the required packages inside the environment:

    ``` pip install -r requirements.txt ```
    
3. Download Spacy models, for more models see [Spacy Models & Languages](https://spacy.io/models/en).

    ```
    python -m spacy download en_core_web_sm
    ```
4. Open **config.ini** configuration file and update the values.
   > **Note**: Please make sure you fulfilled the required configs in **config.ini** file - especially YANDEX and MYMEMORY.

5. Put the sentence you want to paraphrase in a file, sentences should be separated by a line break. Save the file in the **dataset** folder(we suggest to save the file  with txt extension).

6. Generate paraphrases by runing the following command:

   ```
   $ python main.py -f file_name.txt
   ```
    This will save the generated paraphrases in the **result** folder
