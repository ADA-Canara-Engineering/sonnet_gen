**Ada Lovelace day hackathon on AI based Poetry (Sonnet) generation**
---------------------------------------------------------------------------------------------------------------------

**AIM:**	To develop solution to generate Poetry
----	(Sonnet). [Sonnet is a fourteen-line poem with a fixed 
		rhyme scheme.]


**Presentation:** https://docs.google.com/presentation/d/1gc8xoBHNAXsi5R72WOZ7wu9Et15qDCK0Ye6llba5naY

**Video** : https://drive.google.com/file/d/11Kmt_7jEcn2gBO9zvgHMfl0P_2TlChXG/view?usp=drivesdk

**Website**  : https://sonnetgen1.pythonanywhere.com/	

*Undertaking letter*  :  https://drive.google.com/file/d/1zknTaBmTsV9JZYo-vXlP9V3OO0sC_v7K/view?usp=sharing

--------------------------------------------------------------------------


**Introduction:** 
-------------	
				Here we are going to create the "character-level" model for the generation of 
				rhyme scheme sonnet. This model will going to generate the 14 line poem (sonnet) as the
				output.


**Contents:**
----------	
			1] Installation setup -- packages
			2] Downloading of required resource
			3] Model creation
			4] Generation of sonnet from model
			5] Theory/Techniques Used
			6] Technologies/Platform:
			7] Web App
			8] Grade Test


			(both in directly python / jupyter nootbook)


--------------------------------------------------------------------------
**Procedure:**
----------

1] _Package installation:_
 		Open the command prompt/any alternatives and install the following packages.

 		Example: pip install tensorflow

 		These are the required packages: 
https://drive.google.com/file/d/1RjaUGtvLzud2T3WA5Z-Kgczb_DCsnD2G/view?usp=sharing


 				1. Download "requirements.txt" from the above link
 				2. go to the directory where you downloaded this file
 				3. then run this command
 					pip install -r requirements.txt
 				4. This will directly install all the required packages.



2] _Downloading the resource:_
		download all these codes on github directly by downloading zip file
		and extract it
								or

		run this command to git from github
			 > git clone https://github.com/ADA-Canara-Engineering/sonnet_gen.git



3] _Model Creation:_
		1] after unzipping/downloading the resource, go to
			"MODEL CREATION" directry 

			[cd MODEL CREATION]

		2] If you want to run the entire program and to create the model,
			run : python creation.py

			Note:
			This will going to take more time, since the training the model is pre-set to 60 compiling datase
			(Epochs)

			
			Another way to run the program and create model is to use
			Jupytor nootbook, For this install "jupyter nootbook" from here:

https://jupyter.org/install

				in jupyter nootbook, open "creation_jupyter_note_book.ipynb" file, and run each block or run all
				block at a time.

			After the completion of training, the model "sonnet_gen_model.h5" will going to create in same directory




4] _Generation of sonnet from model_
		1] copy the generated model to the OUTPUT folder/dir,
			(here it's already model is generated and placed in 
			"OUTPUT" folder)
		2] go to directory called "OUTPUT" and run this command to
			generate the sonnet from the model that we created in step-3.
			
			python main.py


			If you are using jupyter nootbook, than open "main_jupyter_nootbook.ipynb" 
			and run this to generate the sonnet.
		3] Even we can create sonnet from google colab
			
https://colab.research.google.com/drive/11KAKfFbAmxbb1Ge6P9N02otFqp4GywgV?usp=sharing


------------------------------------------------------------------------


5] _Theory/Techniques Used:_

	a. model creation
		1] Loading the provided dataset and analysing the  character 
			length of sonnet and average character per line
		2] View of the dataset in details by plotting graph of length of 
			characters in each sonnet 
		3] Here the average length of a sonnet is found to be 625 
			characters for a sonnet
		4] Vectorization for the generation of next characters based on 
			the sequence of first line, intially 40 characters are loading from dataset with previous sample of 3.
		5] Storing all the predicted unique characters and mapping it 
			with indices
		6] Vectorizing the generated sequence with numpy array
		7] By using sequential regression in keras, and using recurrent 
			neural network for sequence prediction, creation of model.
		8] Next we have to train this probability value generating model
			with the data.(Epoch) Here 625 characters for 4 different 
			probability distribution values "0.2, 0.5, 1.0, 1.3" and 60 
			triels were done. If the distribution of characters is inversely
			proportional to randomness.
		9] character prediction loss will going to be 3.11 to 1.79 from 
			initial training to end of training, Average loss is found 
			to be 2.45% character loss.
		10] than finally saving the trained model.

	b. Generating Sonnet
		1] from the data, it will going to take rendomly some text 
			sequence, and based on the prediction created by the model,
			the nexr characters are generated.
		2] concerting the initial grabbed character sequence to 
			vectorizing and adding the pre-generated sequence along with 
			the character predicted by the model to the new string.



-------------------------------------------------------------------------
6] _Technologies/Platform:_
	GCD
	Python
	TensorFlow
	Django, js, bootstrap, js, jquery



------------------------------------------------------------------------
7] _WebApp_:
	To run website locally :
		1]  download the zip and extract from here
https://drive.google.com/file/d/1b590zlgyIWbOoI_EXzjq2Zc-ZDKUgDAa/view?usp=sharing

		2] run the following commands in the "SONNET GEN WEBSITE" directory:

			pip install -r requirements.txt
			python manage.py makepigrations
			python manage.py migrate
			python manage.py runserver
		3] than in browser type "http://127.0.0.1:8000/" to view the site



-------------------------------------------------------------------------
8] _Grade test:_
	Readability test --  Flesch Kincaid Grade Level
	10 randomanly generated sonnet are taken from the created model, 
	Flesch Kincaid Grade Level test is done on these generated sonnets and 
	the result of 43.28 is obtained which best suits the property of sonnet.

	30-50	score ensures  :
	difficult to read, best understood by college graduates
	so this ensures sonnet readebality.
	source:
https://yoast.com/flesch-reading-ease-score/


	attributions
	--------------

	 1. https://spectrum.ieee.org/artificial-intelligence/machine-learning/this-ai-poet-mastered-rhythm-rhyme-and-natural-language-to-write-like-shakespeare

 	2. https://github.com/deepmind/sonnet  reference to building model
 	3. kennyng hmm sonnet generator model - reference
 	4. Text Generation With LSTM Recurrent Neural Networks in Python with Keras
      https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/
 	5. Theory on machinelearningmastery.com by Jason Brownlee
-------------------------------------------------------------------------

