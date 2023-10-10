import qiime2
import biom
import qiime2.plugin
import pandas as pd
from q2_types.feature_table import FeatureTable, RelativeFrequency


def normalize_function(input_artifact: biom.Table) -> biom.Table:

    table_normalized = input_artifact.norm(axis="sample", inplace=False)

    return table_normalized

plugin = qiime2.plugin.Plugin(
    name='normalization_plugin',
    version='0.1.0',
    website='https://github.com/pluckySquid/~/qiime2_normalization_plugin.git',
    package='qiime2_normalization_plugin',
    description='A QIIME 2 plugin for qiime2_normalization_plugin functions.',
    short_description='Plugin for qiime2_normalization_plugin analysis.',
)

plugin.methods.register_function(
    function=normalize_function,
    inputs={'input_artifact': FeatureTable[RelativeFrequency]},
    parameters={},  # Add parameters if necessary
    outputs=[('output_artifact', FeatureTable[RelativeFrequency])],
    output_descriptions={
        'output_artifact': 'Description of the output artifact.'
    },
    name='dummy-function',
    description='A description of your function.',
)