def readFloat(requestMsg, errorMsg):
   while True:
      val = raw_input(requestMsg)
      try:
         val = float(val)
         return val
      except:
         print(errorMsg)

def readVal(valType, requestMsg, errorMsg):
   while True:
      val = raw_input(requestMsg)
      try:
         val = valType(val)
         return val
      except:
         print(errorMsg)


