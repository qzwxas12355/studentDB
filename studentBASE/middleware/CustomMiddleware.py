from datetime import datetime, date, time
from django.db import connection

class AddDateAndSql(object):
	def process_response(self, request, response):
		cnt = len(connection.queries)
		time = 'SQLcount: ' + cnt.__str__()+ '. DateTime: ' + str(datetime.now()) + '</body>'
		time = str.encode(time)
		
		response.content = response.content.replace(b'</body>', time)
		#response.write('CoolMiddleware works here</body>')
		return response