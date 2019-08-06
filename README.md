# Service_Now-Mass-closure


Some reasons we may have seen our monitoring software has malfuctioned and as a result it has thrown out alerts in form of tickets in SNOW.
It may be hundreds if you are lucky or thousands of tickets if its a bad day. Now the question is does Service Now inherently has a feature to 
mass close the ticket?
The answer is both yes and no. Mass closing of tickets in service now is generally limited or authorized to its admins and a generally a guy
from other platform won't be able to do the same.

But this Script may help you save the day.
The script uses restful APIs to pull out the data and push the changes. The script is pulling out the tickets using sys_user id in service now.
It uses RegEx to filter out tickets pertaining to a particular host.(Network Devices,Servers). And then closes the tickets by changing the state to 6
which means resolved. I have also added a sleep fucnction to the code as many a times service now transactions take a while to complete.

You can find the lifecycle of a Service Now incident below:

https://docs.servicenow.com/bundle/london-it-service-management/page/product/incident-management/concept/c_IncidentManagementStateModel.html

~ Thanks for Reading :)
