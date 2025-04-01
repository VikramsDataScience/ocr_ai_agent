from smolagents import HfApiModel, TransformersModel


def HFApiCall(hf_token, model_id, max_tokens=2096, temperature=0.5):
    """
    Use Hugging Face API model. Please note that the 'hf_token' is required 
    to use this model, and that we're using the free tier of the API.
    So, inference compute credits are very limited!
    
    Args:
        hf_token: The Hugging Face API token.
        model_id: The HF model ID to use.
    """
    
    print("\'hf_token\' specified. Calling Hugging Face API model...")

    model = HfApiModel(max_tokens=max_tokens,
                    token=hf_token,
                    temperature=temperature,
                    model_id=model_id,
                    custom_role_conversions=None,
    )
    return model


def localTransformersModel(model_id, temperature=0.5, device_map="auto"):
    """
    Use Huggging Face's local Transformers model. Please note that since this uses a 
    local model, please limit your model to only using 1B-3B models, as larger models 
    will take up too much memory and compute resources.
    
    Args:
        model_id: The HF model ID to use/download.
        temperature: The temperature value to use for sampling.
        device_map: The device_map to initialize your model."""
    
    print("\'hf_token\' not used. Using local Transformers model...")

    model = TransformersModel(temperature=temperature,
                            model_id=model_id,
                            device_map=device_map,
                            custom_role_conversions=None)
    return model