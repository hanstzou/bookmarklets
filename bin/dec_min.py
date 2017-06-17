import slimit
import sys
import urllib.parse as ulp

infile = sys.stdin

content = ulp.unquote(infile.read())
print(slimit.minify(content))

if infile != sys.stdin:
    infile.close()
