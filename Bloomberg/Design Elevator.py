'''
System class: handles the elevator calling algorithm, which request to send to which elevator, etc.
Elevator class: models an elevator
Request class: Models a request

--------------
System
--------------
PendingReq: Request[*]
EmergencyReq: Request[*]

--------------
serviceNextReq()
stopSystem()
addRequest()
groundElevator(Elevator)
groundAllElevators()
----------------------

--------------
Elevator
--------------
currentRequest: Request

--------------
getCurrReq()
setCurrReq()
processReq()
--------------

----------------
Request
----------------
SrcFloorNo.
-----------------
-----------------

Derived classes of Request: FloorRequest, ElevatorRequest

FloorRequest: Requests sent from a floor
ElevatorRequest: Requests sent from the elevator

-----------------
FloorRequest
-----------------
Direction: bool
-----------------
setDirection()
getDirection()
-----------------

-----------------
ElevatorRequest
-----------------

-----------------

Derived classes of ElevatorRequest: EmergencyRequest and ServiceRequest

----------------------
EmergencyRequest
----------------------
enum emergency    (malfunction, fire, earthquake)

-----------------------


----------------------
ServiceRequest
----------------------
destFloorNo: int

-----------------------

---------------------

'''