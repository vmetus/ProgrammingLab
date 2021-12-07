class Model():
   def fit(self, data):
     # Fit non implementanto nella classe base
     raise NotImplementedError('Metodo non implementato')
   def predict(self, data):
     # Predict non implementanto nella classe base
     raise NotImplementedError('Metodo non implementato')
   
   
class IncrementModel(Model):
  def predict(self, data):
     incr_med = 0
     prediction = 0
     for i in range (data[1:]):
       # Logica per la predizione
      incr_med += data[i]-data [i-1] 
     prediction = (incr_med/len(data)-1)+data[-1]
     return prediction

 # Prova
 Increment_Model = IncrementModel()
 dati_soldi = [50, 52, 60]
 print(Increment_Model.predict(dati_soldi))
