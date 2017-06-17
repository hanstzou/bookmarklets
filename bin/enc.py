import slimit
import sys
import urllib.parse as ulp

infile = sys.stdin

try:
    content = slimit.minify(infile.read())
    print(ulp.quote(content, '{}[]()<>=!?\'",:;#@|_`$%^&~+-*/'))
except SyntaxError:
    print("error: input content syntax error", file=sys.stderr)

if infile != sys.stdin:
    infile.close()
