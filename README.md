PARKING LOCATOR

-->It's a ardunio+python project

-->conept is to help people to locate or find the vacant parking slots
from anywhere.and get notified of vacant slots through MAIL.

-->sensor used is Infrared Obstacle Avoidance Sensor Module M395.

KEYPOINT-->without making use of any h/w like wifi module arduino communicates with 
          user indirectly through PYTHON
          
-->How things work ?
    
    1.arduino echo's the o/p to it's console as '1' for reserved slot and 
      '0' for vacant slot.after reading the values which are returned by the sensor's
    
    2.concurently two python script's execute's. 
          i]script for SERIAL COMMUNICATION[pyserail.pys]
          ii]Script to SEND MAIL[mailhandler.py]
    
    3.[pyserial.py] establishes serial communication with arduino
      then read's data from that and store it in some csv file as[timestamp,string of 1 and 0]
    
    4.parallely [mailhandler.py] open's the csv file read data last record from that 
      formulate the message and send it to the user's mail-id 
   
