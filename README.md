## Installation

`pip install -e git+git@github.com:Rustem/docx-template.git@master#egg=docx-template`

## Usage

```
# -*- coding: utf-8 -*-
"""
Test docx module
"""
import sys
print sys.path
import os
from docx_template.docx_template import DocxDocumentTemplate

MODULE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEST_IN_DIR = os.path.join(MODULE_DIR, 'in')
TEST_OUT_DIR = os.path.join(MODULE_DIR, 'out')

class TestDocxReport(DocxDocumentTemplate):

    @property
    def output_filename(self):
        return 'test.docx'

def simple usage():
    """Ensure that placeholders is filled properly"""
    data = {
        'company_name': u"Сбербанк",
        'number': u'#0000001',
        'secretary_fio': u'Никифирова Галина Афанасьевна'
    }
    docx_tmpl = TestDocxReport(
        'test_template_placeholders.docx',
        template_dir=TEST_IN_DIR,
        output_dir=TEST_OUT_DIR)
    docx_tmpl.replace(data)
    assert len(docx_tmpl.q(':contains("{{company_name}}")')) == 0, "placeholder not replaced properly"
    assert len(docx_tmpl.q(':contains("{{number}}")')) == 0, "placeholder not replaced properly"
    assert len(docx_tmpl.q(':contains("{{secretary_fio}}")')) == 0, "placeholder not replaced properly"
    docx_tmpl.build()
    # assert len(docx_tmpl.q(':contains("secretary_fio")')) == 1, "placeholder not replaced properly"
```
