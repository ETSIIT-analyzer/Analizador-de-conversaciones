from invoke import task

@task 
def test(p):
	p.run("pytest analyzer/test.py")