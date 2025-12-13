import logging

from frangipani.layer import (
    JsonLayerStackStore,
    Layer,
    LayerScopeAll,
    LayerScopeTag,
    LayerStack,
    LayerValueScalar,
    LayerValueVector3,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:MakeDemoLayerStack")

    layer_tag = [
        ("Intermission", ['spot'], 1.0),
        ("Presentation", ['spot', 'face'], 1.0),
        ("Performance", ['spot', 'back'], 1.0)
    ]
    layers = []
    for layer_name, tags, value in layer_tag:
        layers.extend([
            Layer(
                name=layer_name + " Spots",
                scope=LayerScopeTag(tags=tags),
                values=[
                    LayerValueScalar(name="Dimmer", parameter_selector="dimmer", value=(value,)),
                ],
                opacity=1.0,
            ),
            Layer(
                name=layer_name + " Bowls",
                scope=LayerScopeTag(tags=['bowl']),
                values=[
                    LayerValueVector3(name="ColorRGB", parameter_selector="ColorRGB", value=(1.0, 1.0, 1.0)),
                ],
                opacity=1.0,
        )])

    layers.extend([
        Layer(
            name="Master Dimmer",
            scope=LayerScopeAll(),
            values=[
                LayerValueScalar(name="Dimmer", parameter_selector="*", value=(0.0,)),
            ],
            opacity=0.0,
        ),
        Layer(
            name="Blackout",
            scope=LayerScopeAll(),
            values=[
                LayerValueScalar(name="Dimmer", parameter_selector="*", value=(0.0,)),
            ],
            opacity=0.0,
        )
    ])

    layer_stack = LayerStack(
        name="Demo Layer Stack",
        layers=layers
    )

    store = JsonLayerStackStore()
    store.set_stack(layer_stack)
    store.save("demo.layerstack.json")

    _logger.info(f"Saved layer stack to 'demo.layerstack.json'")

    store = JsonLayerStackStore()
    store.load("demo.layerstack.json")

    from pprint import pprint
    pprint(store.layers)
