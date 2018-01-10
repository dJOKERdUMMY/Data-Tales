Readme.md

Please go through the Readme properly.
The best solution for neural network model is in the "Adam_5_layers_only_7000_epochs_with_200_callbacks.ipynb" notebook

Step 1 : Run the main.py file as "python main.py" in the "src" folder
		 The output is show on the console. There are various warnings which can be ignored
Step 2 : The output is generated for each process of data cleaning and scaling and can be found in "data" folder
Step 3 : The output is saved in "output" folder and can be accessed from there

Note : Due to low accuracy because of most machine learning classifiers, the predicting code in the main.py has been put under ''' <code> '''
	   Only neural network is used for predicting the final output after running the main.py file.
	   Please prefer that when evaluating the code which can be found in the "neural" folder.

The code automatically executes in the following order:
	1. main.py
	2. clean.py
	3. basic_predict.py
	4. qs_predict.py
	5. basic encoder
	6. scale.py

The above code then generates the scaled file which we will use with the neural network made

On analysis the neural network does not performs good on unscaled data as per the theory so we are using scaled csv file generated above

Step 4 : run the "Adam_5_layers_only_7000_epochs_with_200_callbacks.ipynb" Jupyter notebook
Step 5 : see the output in the neural3.csv file in the "output" folder

Various neural networks optimizers were used which can be viewed in other neural network .ipynb files
The neural network with more hidden network as in Adam_only_7000_epochs.ipynb was found to be the bestestimator of our data

The whole model is loaded and saved in the "neural" folder

All the neural network analysis files are in "neural_analysis" folder which can be seen if wanted

The output file named is "output_neural_n.csv" and is in the output folder , here n is the version of output of various submissions

Neural Analysis:

1. Adam_only_7000_epochs.ipynb                            		-- 39413.6873126868
2. Adam_only_7000_epochs_with_150_callbacks.ipynb         		-- 25100.0683333524
3. Adam_5_layers_only_7000_epochs_with_200_callbacks.ipynb 		-- 17226.4379341484 (the best submission as per Analytics Vidya)
4. adam_5_layers_10000_epochs_only_with_800_callbacks.h5		-- (current submission)

The main output is generated from neural networks only after scaling the input file.
Please prefer that while checking and validating the code for future output