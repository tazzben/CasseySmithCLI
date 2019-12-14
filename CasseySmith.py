#!/usr/bin/env python
import os
import sys
import argparse
from multiprocessing import freeze_support
from CasseySmithCV import SaveSimulationTable, importStateWeights

greaterThanZero = lambda x: True if x >=0 else False 
zeroOneRange = lambda x: True if x >=0 and x<=1 else False

def main():
	os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
	os.getcwd()

	# Set default values
	sigmas = [0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 0.95, 1, 1.05, 1.1, 1.25, 1.5]
	criticalValues = [0.025, 0.05, 0.95, 0.975]
	HHICriticalValues = [0.025, 0.05, 0.95, 0.975]
	
	parser = argparse.ArgumentParser(description='Create null hypothesis distributions for the Ellison-Glaeser index based on the assumption of random plant location.')
	parser.add_argument('plants', metavar='P', type=int, nargs='+', help='Specify the plant size(s) for the simulation')
	parser.add_argument('--sigmas', nargs='*', default=None, type=float, help='Specify sigma values of underlying normal distribution')
	parser.add_argument('--states', metavar='filename', default=None, help='Specify a plain text file containing state population weights (one state per line)')
	parser.add_argument('--criticalValues', default=None, nargs='*', type=float, help='Specify a list of critical values for Gamma and G')
	parser.add_argument('--HHICValues', default=None, nargs='*', type=float, help='Specify a list of values to extract from the generated HHI distributions')

	parseresults = parser.parse_args()
	plants = list(filter(greaterThanZero,parseresults.plants))

	if parseresults.sigmas != None and len(parseresults.sigmas)>0:
		sigmas = list(filter(greaterThanZero, parseresults.sigmas))

	if parseresults.criticalValues != None and len(parseresults.criticalValues)>0:
		criticalValues = list(filter(zeroOneRange, parseresults.criticalValues))

	if parseresults.HHICValues != None and len(parseresults.HHICValues)>0:
		HHICriticalValues = list(filter(zeroOneRange, parseresults.HHICValues))
	
	if parseresults.states != None and len(parseresults.states.strip())>0:
		states = importStateWeights(parseresults.states.strip())
		SaveSimulationTable('CasseySmithOutput.csv',plants,sigmas,criticalValues=criticalValues,HHIConfInterval=HHICriticalValues, stateList=states)
	else:
		SaveSimulationTable('CasseySmithOutput.csv',plants,sigmas,criticalValues=criticalValues,HHIConfInterval=HHICriticalValues)	

if __name__ == "__main__":
	freeze_support()
	main()