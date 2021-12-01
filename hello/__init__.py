import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def saabir():
    """responds to name Saabir"""
    check50.run("./hello").stdin("Saabir").stdout("Saabir").exit()

@check50.check(compiles)
def Saim():
    """responds to name Saim"""
    check50.run("./hello").stdin("Saim").stdout("Saim").exit()
