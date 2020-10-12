def checksession(request):
	try:
		org_id = request.session['org_id']
		return True
	except:
		return False