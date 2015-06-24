import os
from docx.document import DocxDocument
from docx import NSPREFIXES
from pyquery import PyQuery as pq

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


def repl_text(elem, val, repl=u''):
    # print elem, val, repl
    new_val = pq(elem).text().replace(val, repl)
    pq(elem).text(new_val)


def merge(first, q):
    first = pq(first)
    left = first.text()
    l = left.rfind("{{")
    r = left.rfind("}}")
    l = l == -1 and 10000 or l
    r = r == -1 and -10000 or r
    if l < r:
        return
    next = first.next()
    next_text = next.text()
    while "}}" not in next_text:
        left = left + next_text
        prev, next = next, next.next()
        next_text = next.text()
        prev.remove()

    idx = next_text.find('}}')
    extra, next_text = next_text[:(idx + 2)], next_text[(idx + 2):]
    if next_text == "":
        next.remove()
    else:
        next.find("w\:t").text(next_text)
    first.find("w\:t").text(left + extra)


class DocxDocumentTemplate(DocxDocument):
    default_template_dir = os.path.join(PROJECT_DIR, 'in')
    default_output_dir = os.path.join(PROJECT_DIR, 'out')
    default_output_file = os.path.join(PROJECT_DIR, 'test.docx')

    content_type = (
        'application/vnd.openxmlformats-'
        'officedocument.wordprocessingml.document')

    def __init__(self, template_name, **options):
        self.template_name = template_name
        self.template_dir = options.get(
            'template_dir', self.default_template_dir)
        self.output_dir = options.get(
            'output_dir', self.default_output_dir)
        self.output_filename = options.get('output_filename', self.default_output_file)
        super(DocxDocumentTemplate, self).__init__(self.get_template_file())
        self.q = pq(self.document, parser='xml', namespaces=NSPREFIXES)
        self.preformat()

    def build(self):
        output_file = self.get_output_file()
        self.save(output_file)
        return output_file

    def preformat(self):
        self.q('w\:proofErr').remove()
        self.q(':contains("{{")').parents('w\:r').each(lambda _, e: merge(e, self.q))

    def replace(self, data, doc=None):
        q = doc and pq(doc) or self.q
        for key, value in data.iteritems():
            key = u'{{%s}}' % key
            q(u':contains("%s")' % key).each(
                lambda _, e: repl_text(e, key, value))

    def get_output_file(self):
        return os.path.join(self.output_dir, self.output_filename)

    def get_template_file(self):
        return os.path.join(self.template_dir, self.template_name)
