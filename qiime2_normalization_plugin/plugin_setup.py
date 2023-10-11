import qiime2
import biom
import qiime2.plugin
import pandas as pd
from q2_types.feature_table import FeatureTable, RelativeFrequency, Frequency
from scipy.linalg import pinv, svd
from pynmranalysis.normalization import PQN_normalization


def normalize_function(input_artifact: biom.Table) -> biom.Table:
    table_normalized = input_artifact.norm(axis="sample", inplace=False)

    return table_normalized

def PQN_normalize_function(input_artifact: biom.Table) -> biom.Table:
    df = input_artifact.to_dataframe(dense=True)
    normalized = PQN_normalization(df ,ref_norm = "median" , verbose=False) 
    table_normalized = biom.Table(normalized.values, observation_ids=normalized.index.tolist(), sample_ids=normalized.columns.tolist())
    
    return table_normalized

plugin = qiime2.plugin.Plugin(
    name='normalization_plugin',
    version='0.1.0',
    website='https://github.com/pluckySquid/qiime2_normalization_plugin.git',
    package='qiime2_normalization_plugin',
    description='A QIIME 2 plugin for qiime2_normalization_plugin functions.',
    short_description='Plugin for qiime2_normalization_plugin analysis.',
)

plugin.methods.register_function(
    function=normalize_function,
    inputs={'input_artifact': FeatureTable[Frequency]},
    parameters={},  # Add parameters if necessary
    outputs=[('output_artifact', FeatureTable[RelativeFrequency])],
    output_descriptions={
        'output_artifact': 'Description of the output artifact.'
    },
    name='dummy-function',
    description='Do normalization to a qza file.',
)

plugin.methods.register_function(
    function=PQN_normalize_function,
    inputs={'input_artifact': FeatureTable[Frequency]},
    parameters={},  # Add parameters if necessary
    outputs=[('output_artifact', FeatureTable[Frequency])],
    output_descriptions={
        'output_artifact': 'FeatureTable[Frequency])].'
    },
    name='dummy-function',
    description='Do PQN normalization to a qza file.',
)
