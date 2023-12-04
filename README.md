# python-challenge

## PyBank
 analysis - Outputs of main.py which analyzes financial records of a company. 
 Resources - Budget data for script analysis to run.
 main.py - Python analysis script that outputs results

## PyPoll
 analysis - Outputs of main.py which analyzes election result data.
 resources - election data for script analysis to run. 
 main.py - Python analysis script that outputs results 



# Code leveraged outside of classroom activities below from Stack Overflow to write terminal results to blank .txt file for both analyses. 
https://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file/25023414#25023414
  
    with open(output_file, 'w') as file:
    
    # Redirect the standard output to the file
    	  import sys
    	  original_stdout = sys.stdout
    	  sys.stdout = file
        print(" ")
        
 
     # Restore the standard output
	      sys.stdout = sys.__stdout__
