import check50
import check50.c

@check50.check()
def exists():
  """mario.c Exists"""
  check50.exists("mario.c")
  
@check50.check(exists)
def compiles():
  """mario.c compiles"""
  check50.c.compile("mario.c")

def piramid(n):
  if n < 1: return ''
  elif n == 1: return '#'
  else: return piramid(n - 1) + '\n' + n * '#'
  
@check50.check(compiles)
for i in range(8):
  def prints_piramid():
    """prints piramid{i}"""
    check50.run("./mario").stdout(piramid(i) + "?\n", regex=True).exit(0)
