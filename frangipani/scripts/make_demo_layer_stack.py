import logging

from frangipani.layer import (
    Layer,
    LayerScopeAll,
    LayerScopeTag,
    LayerStack,
    LayerValueScalar,
    JsonLayerStackStore,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:MakeDemoLayerStack")

    layer_stack = LayerStack(
        name="Demo Layer Stack",
        layers=[
            Layer(
                name="Demo Layer 1 (all)",
                scope=LayerScopeTag(tags=['Odd', 'Dimmer']),
                values=[
                    LayerValueScalar(name="All", selector="*", value=0.0),
                ],
            ),
            Layer(
                name="Demo Layer 2 (dimmers)",
                scope=LayerScopeAll(),
                values=[
                    LayerValueScalar(name="Dimmers", selector="dimmer*", value=1.0),
                ],
            ),
        ],
    )

    store = JsonLayerStackStore()
    store.set_stack(layer_stack)
    store.save("demo_layer_stack.json")

    _logger.info(f"Saved layer stack to 'layer_stack.json'")

    store = JsonLayerStackStore()
    store.load("demo_layer_stack.json")

    from pprint import pprint
    pprint(store.stack)
