# Data Tales - Beyond Infinity
<a href="https://datahack.analyticsvidhya.com/contest/data-tales-beyond-infinity-great-lakes-institute-o/">Analytics Vidhya online hackathon (January 2018)</a><br>
<a href="https://datahack.analyticsvidhya.com/contest/data-tales-beyond-infinity-great-lakes-institute-o/pvt_lb">Final Leaderboards (Team:dJOKERdUMMY)</a><br>
<a href="https://drive.google.com/open?id=1hCvTfZe5UwoOg-1P7ga4ZUcSFGUxTurj">Presentation Document explaining the steps and Data Analysis</a>

**Please go through the Readme properly.**
- Run the main.py file as "python main.py" in the "src" folder. The output is show on the console. There are various warnings which can be ignored
- The output is generated for each process of data cleaning and scaling and can be found in "data" folder.
- The output is saved in "output" folder and can be accessed from there.
- Run the "Adam_5_layers_only_7000_epochs_with_200_callbacks.ipynb" Jupyter notebook
- See the output in the "neural3.csv" file in the "output" folder

**Note : Due to low accuracy some of the machine learning classifiers used for predicting the output in the main.py has been commented. Only neural network models are used for predicting the final output after running the main.py file. Please prefer them when evaluating the code which can be found in the "neural" folder.**

After running the "main.py" file, the code automatically executes in the following order:
- clean.py
- basic_predict.py
- qs_predict.py
- basic encoder
- scale.py

The above code then generates the scaled file which we will use with the neural network made.

On analysis the neural networks does not performs good on unscaled data as per the theory so we are using scaled csv files generated above.

Various neural networks optimizers were used which can be viewed in other neural network .ipynb files.

The whole model is loaded and saved in the "neural" folder.

The output file named is "output_neural_(n).csv" and is in the output folder.

**RMSE score as per submission**

file name | RMSE score
------------ | -------------
Adam_5_layers_only_7000_epochs_with_200_callbacks.ipynb | 17226.4379341484 (the best submission as per Analytics Vidya)
Adam_only_7000_epochs_with_150_callbacks.ipynb | 25100.0683333524
adam_5_layers_10000_epochs_only_with_800_callbacks.ipynb | >23000
Adam_only_7000_epochs.ipynb | 39413.6873126868
Other general ML algorithms | >50000
