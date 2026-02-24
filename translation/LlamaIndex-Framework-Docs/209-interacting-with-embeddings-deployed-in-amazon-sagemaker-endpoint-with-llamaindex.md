# Interacting with Embeddings deployed in Amazon SageMaker Endpoint with LlamaIndex

An Amazon SageMaker endpoint is a fully managed resource that enables the deployment of machine learning models, for making predictions on new data.

This notebook demonstrates how to interact with Embedding endpoints using `SageMakerEmbedding`, unlocking additional llamaIndex features.
So, It is assumed that an Embedding is deployed on a SageMaker endpoint.

## Setting Up
If you’re opening this Notebook on colab, you will probably need to install LlamaIndex 🦙. 


```python
%pip install llama-index-embeddings-sagemaker-endpoint
```


```python
! pip install llama-index
```

You have to specify the endpoint name to interact with.


```python
ENDPOINT_NAME = "<-YOUR-ENDPOINT-NAME->"
```

Credentials should be provided to connect to the endpoint. You can either:
-  use an AWS profile by specifying the `profile_name` parameter, if not specified, the default credential profile will be used. 
-  Pass credentials as parameters (`aws_access_key_id`, `aws_secret_access_key`, `aws_session_token`, `region_name`). 

for more details check [this link](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

**AWS profile name**


```python
from llama_index.embeddings.sagemaker_endpoint import SageMakerEmbedding

AWS_ACCESS_KEY_ID = "<-YOUR-AWS-ACCESS-KEY-ID->"
AWS_SECRET_ACCESS_KEY = "<-YOUR-AWS-SECRET-ACCESS-KEY->"
AWS_SESSION_TOKEN = "<-YOUR-AWS-SESSION-TOKEN->"
REGION_NAME = "<-YOUR-ENDPOINT-REGION-NAME->"
```


```python
embed_model = SageMakerEmbedding(
    endpoint_name=ENDPOINT_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=REGION_NAME,
)
```

**With credentials**:


```python
from llama_index.embeddings.sagemaker_endpoint import SageMakerEmbedding

ENDPOINT_NAME = "<-YOUR-ENDPOINT-NAME->"
PROFILE_NAME = "<-YOUR-PROFILE-NAME->"
embed_model = SageMakerEmbedding(
    endpoint_name=ENDPOINT_NAME, profile_name=PROFILE_NAME
)  # Omit the profile name to use the default profile
```

## Basic Usage

### Call `get_text_embedding` 


```python
embeddings = embed_model.get_text_embedding(
    "An Amazon SageMaker endpoint is a fully managed resource that enables the deployment of machine learning models, specifically LLM (Large Language Models), for making predictions on new data."
)
```


```python
embeddings
```




    [0.021565623581409454,
    ...
     0.019147753715515137,]



### Call `get_text_embedding_batch` 


```python
embeddings = embed_model.get_text_embedding_batch(
    [
        "An Amazon SageMaker endpoint is a fully managed resource that enables the deployment of machine learning models",
        "Sagemaker is integrated with llamaIndex",
    ]
)
```


```python
len(embeddings)
```




    2