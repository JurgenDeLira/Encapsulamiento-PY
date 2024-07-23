@<decorator>
def <algunMetodo>(self,<parametros>)

class Ejemplo():
  def __init__(self, valorInicial):
    self._x=valorInicial

  @property
  def x(self): #este es el método de lectura con el decorator property.
    return self._x

  @x.setter
  def x(self,valor): #este es el método de escritura con el decorator setter.
    self._x=valor