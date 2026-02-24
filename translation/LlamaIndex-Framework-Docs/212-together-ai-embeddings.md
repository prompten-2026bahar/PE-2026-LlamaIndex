# Together AI Embeddings

This notebook shows how to use `Together AI` for embeddings. Together AI provides access to many state-of-the-art embedding models.

Visit https://together.ai and sign up to get an API key.

## Setup

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.


```python
%pip install llama-index-embeddings-together
```


```python
!pip install llama-index
```


```python
# You can set the API key in the embeddings or env
# import os
# os.environ["TOEGETHER_API_KEY"] = "your-api-key"

from llama_index.embeddings.together import TogetherEmbedding

embed_model = TogetherEmbedding(
    model_name="togethercomputer/m2-bert-80M-8k-retrieval", api_key="..."
)
```

## Get Embeddings


```python
embeddings = embed_model.get_text_embedding("hello world")
```


```python
print(len(embeddings))
```

    768



```python
print(embeddings[:5])
```

    [-0.11657876, -0.012690996, 0.24342081, 0.32781482, 0.022501636]