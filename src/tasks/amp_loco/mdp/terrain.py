import mjlab.terrains as terrain_gen
from mjlab.terrains.terrain_generator import TerrainGeneratorCfg


RANDOM_ROUGH_TERRAINS_CFG = TerrainGeneratorCfg(
    size=(8.0, 8.0),
    border_width=20.0,
    num_rows=10,
    num_cols=20,
    sub_terrains={
        "flat": terrain_gen.BoxFlatTerrainCfg(proportion=0.9),
        "random_rough": terrain_gen.HfRandomUniformTerrainCfg(
            proportion=0.1,
            noise_range=(0.02, 0.05),
            noise_step=0.02,
            border_width=0.25,
        ),
        "wave_terrain": terrain_gen.HfWaveTerrainCfg(
            proportion=0.0,
            amplitude_range=(0.0, 0.2),
            num_waves=4,
            border_width=0.25,
        ),
        "slope_down": terrain_gen.HfPyramidSlopedTerrainCfg(
            proportion=0.0,
            slope_range=(0.0, 0.5),
            platform_width=1.0,
            border_width=0.25,
            inverted=False,
        ),
        "slope_up": terrain_gen.HfPyramidSlopedTerrainCfg(
            proportion=0.0,
            slope_range=(0.0, 0.5),
            platform_width=1.0,
            border_width=0.25,
            inverted=True,
        ),
    },
    add_lights=True,
)
