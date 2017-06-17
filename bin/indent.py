from slimit.parser import Parser
from slimit.visitors.ecmavisitor import ECMAVisitor
import sys
import urllib.parse as ulp

class ECMAVisitor_DoubleSpace(ECMAVisitor):

    def __init__(self):
        ECMAVisitor.__init__(self)

    def _make_indent(self):
        return ECMAVisitor._make_indent(self) * 2


infile = sys.stdin

parser = Parser()
visitor = ECMAVisitor_DoubleSpace()

content = ulp.unquote(infile.read())
syntax_tree = parser.parse(content)
print(visitor.visit(syntax_tree))

if infile != sys.stdin:
    infile.close()
