from django_rq import job

@job
def fun():
	print 'hello user'

