# Model Validation
Validating that a model is 'good'.

Split data into 3 sets:
* Train set
* Validation set
* Test set

During training:
* Train set used for fitting the model weights
* Validation set used to check accuracy of current model during training epochs
    * **Not** used for backpropagation step to update weights
    * Only as a reference for current model performance
    * Tell if overfitting on the train set

After training:
* Test set used to evaluate performance of the trained model
    * Data is unseen to the model
    * Model would be biased towards the validation set, so use test set as a separate truly unseen set