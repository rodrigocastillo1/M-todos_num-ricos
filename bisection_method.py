#AUTOR: Rodrigo Castillo Alcántara
#NUMERICAL_METHODS -> BISECTION_METHOD
#El usuario ingresa la función sin espacios, tupla de puntos (izquierdo, derecho), y el valor máximo de error porcentual
#Ejecución con parámetros: python3 bisection_method.py tuple(dependent_variable, function) tuple(left_point, right_point) max_porcentage_error

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


class Function():													#OBJETO FUNCIÓN
	def __init__(self, function, dep_variable):						#Constructor del objeto Función
		self.dep_variable = dep_variable							#Variable dependiente de la función
		self.function = function									#Función a evaluar

	def evaluateFunction(self, value):
		available_functions = vars(math)
		variable_value = {self.dep_variable: float(value)}
		return eval(self.function, available_functions, variable_value)


class BisectionMethod():														#OBJETO MÉTODO DE BISECCIÓN
	def __init__(self, dep_variable, function, points, max_porcentage_error):	#>>Constructor del método de bisección:
		self.function = Function(function, dep_variable)						#función del tipo de objeto Function
		self.points = [float(i) for i in points]								#Lista de los puntos a evaluar casteados a flotantes
		self.max_porcentage_error = float(max_porcentage_error)					#Porcentaje máximo de error aceptado
		self.mid_point = 0														#Punto medio necesario para el algoritmo
		self.porcentage_error = 100.0											#Porcentaje de error inicial para entrar al ciclo por primera vez
		self.index = 1
		
	def printCalcInfo(self):
		s = self 
		f = s.function
		print(str(s.index).ljust(9)+"|"+str(round(s.points[0], 5)).center(10)+"|"+str(round(s.points[1], 5)).center(10)+"|"+str(round(s.mid_point, 5)).center(10)+"|"+str(round(f.evaluateFunction(s.points[0]), 5)).center(10)+"|"+str(round(f.evaluateFunction(s.points[1]), 5)).center(10)+"|"+str(round(f.evaluateFunction(s.mid_point), 5)).center(10)+"|"+str(round(self.porcentage_error, 5)).center(14))
	
	def bisection(self):															#>>Algoritmo del método de bisección	
		self.mid_point = (self.points[0]+self.points[1])/2							#Se calcula el primer punto medio
		print("\nIteración".ljust(5)+"|"+"Xizq".center(10)+"|"+"Xder".center(10)+"|"+"Xcentro".center(10)+"|"+"F(Xizq)".center(10)+"|"+"F(Xder)".center(10)+"|"+"F(Xcentro)".center(10)+"|"+"Error porcentual")
		self.printCalcInfo()
		while self.porcentage_error > self.max_porcentage_error:					#Mientras el porcentaje de error que retorne el algoritmo sea mayor que el máximo aceptable:
			if(self.isZeroInterval()): 												#Si entre el punto izquierdo y el medio nos encontramos en un intervalo que tiene raíces:
				self.points[1] = self.mid_point 									#El punto medio se convierte en el nuevo punto derecho
			else: 																	#Sino:
				self.points[0] = self.mid_point 									#El punto medio se convierte en el nuevo punto izquierdo
			self.porcentage_error = porcentageError((self.points[0]+self.points[1])/2, self.mid_point) 	#Calculamos el porcentraje de error con el punto medio anterior como valor aproximado y el nuevo cono valor real
			self.mid_point = (self.points[0]+self.points[1])/2 						#Asignamos el nuevo punto medio
			self.index+=1
			self.printCalcInfo()
		return self.mid_point														#Retornamos el valor de la raíz
				

	def isZeroInterval(self): 																#Función para saber si nos encontramos en un intervalo con raíces
		f = self.function 																	#Asignación para hacer más legible el codigo
		if(f.evaluateFunction(self.points[0])*f.evaluateFunction(self.mid_point) < 0): 		#Si el producto del extremo izquierdo y el punto medio son igual a cero:
			return True 																	#Retornamos verdadero
		else: return False 																	#Sino, retornamos falso


def porcentageError(true_val, approx_val):
	return math.fabs((true_val - approx_val)/true_val)*100

def getData(sys):
	d_dep_variable = sys.argv[1].split(", ")[0]												#Variable dependiente de la función
	d_function = sys.argv[1].split(", ")[1]													#Función a evaluar
	d_points = list(sys.argv[2].split(", "))												#Lista de los puntos a evaluar
	d_max_porcentage_error = sys.argv[3]													#Porcentaje máximo de error aceptado
	return BisectionMethod(d_dep_variable, d_function, d_points, d_max_porcentage_error)	#Se retorna una instancia del objeto Método de bisección

method = getData(sys)
method.bisection()