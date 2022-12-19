from torch import nn
from transformers import BertModel

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


issue_label = ["Battery",'External','Internal',	'Screen',	'Service',	'Software']


class BertClassifier(nn.Module):

    def __init__(self, dropout=0.1):

        super(BertClassifier, self).__init__()

        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(768, 6)
        self.relu = nn.ReLU()

    def forward(self, input_id, mask):

        _, pooled_output = self.bert(input_ids= input_id, attention_mask=mask,return_dict=False)
        dropout_output = self.dropout(pooled_output)
        linear_output = self.linear(dropout_output)
        final_layer = self.relu(linear_output)
        return final_layer

from sklearn.utils.extmath import softmax
import numpy as np

def predict_issue(model,text):
  # model.eval()
  return_data = {}
  input = tokenizer( text ,  padding='max_length', max_length = 185, truncation=True,return_tensors="pt") 
  mask = input['attention_mask']
  input_id = input['input_ids'].squeeze(1)
  prediction_array = list(model(input_id,mask).detach().numpy())
  return_data['prediction_array'] = softmax(prediction_array)*100
  return_data['prediction_array'] = np.round(return_data['prediction_array']).astype(int)
  return_data['prediction_output'] = issue_label[model(input_id,mask).argmax(axis=-1)]
  return_data['labels'] = issue_label
  return return_data
#   return issue_label[model(input_id,mask).argmax(axis=-1)]

