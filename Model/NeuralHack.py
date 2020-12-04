'''
install anaconda

install following packages:
conda create -n transformers python
conda activate transformers
conda install pytorch cpuonly -c pytorch

install simple transformers:
pip install simpletransformers
'''


from simpletransformers.conv_ai import ConvAIModel

train_args = {
    "overwrite_output_dir": True,
    "reprocess_input_data": True
}

# create model
model = ConvAIModel("gpt", "gpt_personachat_cache", args=train_args)


# train model
model.train_model("parsed_data_1.json")
