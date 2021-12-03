from random import randint, choice

class service_time:
  def __init__(self, gross_weight, floor, can_use_trolley, has_elevator, postnr, predicted_st, actual_st):
      self.gross_weight = gross_weight
      self.floor = floor
      self.can_use_trolley = can_use_trolley
      self.has_elevator = has_elevator
      self.postnr = postnr
      self.predicted_st = predicted_st
      self.actual_st = actual_st

      if gross_weight is None:
          self.gross_weight = randint(0, 100)
          if self.gross_weight is 69:
              self.gross_weight = randint(100,300)

      if floor is None:
          self.floor = randint(0, 10)
        
      if can_use_trolley is None:
          self.can_use_trolley = bool(randint(0, 1))

      if has_elevator is None:
          self.has_elevator = bool(randint(0, 1))

      if postnr is None:
          samples = ["0690", "0691", "0692", "0693", "0694", "0695", "0696", "0697", "0698", "0699"]
          self.postnr = samples[randint(0, len(samples)-1)]

      service_time = 4

      # Tar utgangspunkt i perfekt scenario, floor = x med heis, tralle = True. 
      # Eller floor = 1 uten heis, tralle = true

      # For andre scenarier enn dette blir denne logikken brukt for beregning av ST

      for x in range(10, self.gross_weight, 10):
        service_time += 1
      
      for x in range(1, self.floor+1, 1):
        service_time += 1
      
      if self.can_use_trolley is False and self.has_elevator is False and self.floor > 1:
        service_time = service_time * 1.5
      
      if self.can_use_trolley is True and self.has_elevator is False and self.floor > 1:
        service_time = service_time * 1.3

      if self.can_use_trolley is False and self.has_elevator is False and self.floor == 1 or 0:
        service_time += 3
      
      if self.can_use_trolley is False and self.has_elevator is True and self.floor > 1:
        service_time = service_time * 1.25
    
      if self.postnr is "0690":
          service_time += 10
      
      self.actual_st = service_time
