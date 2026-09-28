'''diccionarios 
   .valves
   .items
   .update
'''
network_config_2={
   "0001": {
       "ip": "192.168.0.1",
              "device": "Switch",
              "policy": "Deny All",
              "status": False,
              "lista": [1,2,3,4,5,6,7,8,9]
   },
   "0002": {
       "ip": "192.168.0.2",
              "device": "Switch",
              "policy": "Avoid .2 .3 .4",
              "status": False,
   },
   "0003": {
       "ip": "192.168.0.3",
              "device": "Switch",
              "policy": "Allow .5 .6 .7",
              "status": False,
   },
   "0004": {
       "ip": "192.168.+0.4",
              "device": "Switch",
              "policy": "Allow .8 .9 .10",
              "status": False,
   },
   "0005": {
       "ip": "192.168.0.5",
              "device": "Switch",
              "policy": "Allow .11 .12 .13",
              "status": False,
   }
}
a= [1,2,3, [7.8,8]]
contenido= network_config_2.get("0001")
listaA= contenido.get("lista")
num = listaA[2]
print(num)