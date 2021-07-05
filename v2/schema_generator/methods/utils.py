def get_set_params(params: dict) -> dict:
    return {
        k if not k.endswith("_") else k[:-1]: v
        for k, v in params.items()
        if k != "self" and v is not None
    }


