import time
import pysnow
import re
c = pysnow.Client(instance='instance', user='username', password='password')
incident = c.resource(api_path='/table/incident')


#using the same assigment group above to fetch more tickets
qb = (
    pysnow.QueryBuilder()
    .field("assigned_to").equals(<id>)
    
)

response = incident.get(query=qb)
filter = re.compile(r'Router1',re.IGNORECASE)



for b in response.all():
 print (str(b['description']))
 result = filter.search(str(b['description']))
 if result:
  update = {'work_notes : 'This ticket has been caused due to automation malfunction. Closing the ticket','incident_state' : 6}
  updated_record = incident.update(query={'number': b['number']}, payload=update)
  time.sleep(3)
  print(updated_record)
  
   
   





