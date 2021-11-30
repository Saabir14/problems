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
  
  
for i in range(8):
  @check50.check(compiles)
  def prints_piramid():
    """prints piramid{i}"""
    check50.run("./mario").stdout("?\n", regex=True).exit(0)
