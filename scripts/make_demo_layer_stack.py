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
                name="DimmerFixtures all parameters",
                scope=LayerScopeTag(tags=['Dimmer']),
                values=[
                    LayerValueScalar(name="All", parameter_selector="*", value=0.0),
                ],
            ),
            Layer(
                name="RGBFixtures dimmer values",
                scope=LayerScopeTag(tags=['RGB']),
                values=[
                    LayerValueScalar(name="Dimmers", parameter_selector="dimmer*", value=1.0),
                ],
            ),
            Layer(
                name="Master Dimmer",
                scope=LayerScopeAll(),
                values=[
                    LayerValueScalar(name="Dimmers", parameter_selector="dimmer*", value=0.0),
                ],
                opacity=0.0,
            ),
            Layer(
                name="Blackout",
                scope=LayerScopeAll(),
                values=[
                    LayerValueScalar(name="Dimmers", parameter_selector="dimmer*", value=0.0),
                ],
                opacity=0.0,
            ),
        ],
    )

    store = JsonLayerStackStore()
    store.set_stack(layer_stack)
    store.save("demo.layerstack.json")

    _logger.info(f"Saved layer stack to 'demo.layerstack.json'")

    store = JsonLayerStackStore()
    store.load("demo.layerstack.json")

    from pprint import pprint
    pprint(store.layers)
