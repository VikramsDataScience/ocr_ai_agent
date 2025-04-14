from smolagents import HfApiModel, TransformersModel
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer
import torch


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

    return HfApiModel(max_tokens=max_tokens,
                    token=hf_token,
                    temperature=temperature,
                    model_id=model_id,
                    custom_role_conversions=None,
    )


def localTransformersModel(model_id, tokenizer=None, temperature=0.6, device_map="auto", torch_dtype="auto"):
    """
    Use Huggging Face's local Transformers model. Please note that since this uses a 
    local model, please limit your model to only using 1B-3B models, as larger models 
    will take up too much memory and compute resources.
    
    Args:
        model_id: The HF model ID to use/download.
        temperature: The temperature value to use for sampling.
        device_map: The device_map to initialize your model. Use with larger models.
        However, using larger models on low-end GPUs will mean I/O bottlenecks."""
        
    print(f"\'hf_token\' not used. Using local Transformers model: {model_id}...")

    return TransformersModel(temperature=temperature,
                             tokenizer=tokenizer,
                             device="cuda",
                            model_id=model_id,
                            device_map=device_map,
                            torch_dtype=torch_dtype,
                            custom_role_conversions=None)


def localQuantizedLlamaModel(model_id, temperature=0.5, max_new_tokens=2096):
    """Use this Quanitization function with LLAMA models ONLY. This function
    won't work with other models, since the quantization configurations are 
    individual to each LLM. Please refer to the model cards on Hugging Face 
    hub for the specific quantization configurations (if available).

    Args:
        model_id: The HF model ID to use/download.
        temperature: The temperature value to use for sampling.
        max_new_tokens: The maximum number of new tokens to generate."""
    
    # Configure quantization
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4"
    )
    
    # Create a custom TransformersModel that applies quantization when loading
    class QuantizedTransformersModel(TransformersModel):
        def __init__(self, model_id, temperature, max_new_tokens):
            super().__init__(
                temperature=temperature,
                max_new_tokens=max_new_tokens,
                model_id=model_id
            )
            
        def _load_model(self):
            # Override the model loading method to apply quantization
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                device_map="auto",
                torch_dtype=torch.bfloat16,
                quantization_config=quantization_config
            )
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
    
    return QuantizedTransformersModel(
        model_id=model_id,
        temperature=temperature,
        max_new_tokens=max_new_tokens
    )