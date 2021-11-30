import check50
import check50.c

@check50.check()
def exists():
  """hello.c Exists"""
  check50.exists("hello.c")
  
@check50.check(exists)
def compiles()
  """hello.c compiles"""
  check50.c.compile("hello.c")
  
@check50.check(compiles)
def prints_hello():
  """prints "hello, world\\n" """
  check50.run("./hello").stdout("[Hh]ello, [Ww]orld!?\n", regex=True).exit(0)
