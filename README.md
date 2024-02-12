# Personal Data Detector

Detect personal data in text with LLM. This project consists of a Jupyter Notebook `personal_data_detector.ipynb` and module `create_synthetic_dataset.py`. 

The notebook contains code to perform the following tasks:

## 1. Install Dependencies

The notebook starts by installing necessary dependencies using pip.

## 2. Create Synthetic Text Data with Personal Data

Synthetic text data is generated with personal data included in half of the data points. Uncomment the code to generate and store synthetic data.

## 3. Work with Synthetic Data

The synthetic data is loaded, checked, and balanced. The dataset is then split into training, validation, and test sets.

## 4. Train Model on Synthetic Data

A DistilBERT model is trained on the synthetic data. The notebook includes code for initializing the tokenizer and model, creating custom datasets, and training the model using the Trainer class from the transformers library.

## 5. Make a Classifier to Distinguish Whether Text Contains Personal Data or Not

A trained model is loaded, and a function is defined to classify input text as containing personal data or not. The function is applied to various examples to demonstrate its usage.

## Usage

- Clone the repository:
`git clone https://github.com/alexey-krasnov/personal_data_detector.git`

- Configure  Python environment and install necessary dependencies installed.
`pip install -r requirements.txt`

- Open and run the Jupyter Notebook `personal_data_detector.ipynb` step-by-step.

- Follow the instructions in the notebook to generate synthetic data, train the model, and use the classifier to classify text.

## Author

[Dr. Aleksei Krasnov](https://github.com/alexey-krasnov)
email: alexeykrasnov1989@gmail.com

Feel free to contribute, report issues, or provide feedback!

## License
This project is licensed under the MIT - see the LICENSE.md file for details.
