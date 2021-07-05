LINE_BREAK_STYLE = """
    """
LINE_BREAK_LENGTH = 81

RENDER_METHOD = """
class {name}Category(BaseCategory):
    async def __call__(self, {arguments}) -> {return_type}:
        \"\"\"
        {method_description}
        {argument_description}
        \"\"\"
        params = self.get_set_params(locals())
        response = await self.api.request("{endpoint}", params)
        return response
"""