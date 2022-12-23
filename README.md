# word2pdf

Bulk converts multiple Word files (`.doc` and `.docx`) to PDFs by using the [docx2pdf](https://pypi.org/project/docx2pdf/) library. The time taken for the conversion depends on the number of Word files you have.

## How to use

- Clone the repo by running `git clone https://github.com/deepakness/word2pdf.git` command
- Delete exising Word and PDF files from `word` and `pdfs` folders respectively
- Copy-paste all your `.doc` or `.docx` in the `word` folder, and
- Run the following command:

```python
python word2pdf.py
```

And within minutes, all your Word files will be converted to PDFs. You can access the generated PDFs under `pdfs` folder.

Enjoy!