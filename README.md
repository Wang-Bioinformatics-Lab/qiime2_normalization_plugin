

## Env
Besides qiime2, you may want to install scikit-learn
```
pip install --upgrade scikit-learn
```

## Build and run

If you have already build this plugin and what to update the plugin, run:
```
 qiime dev refresh-cache
```

Go to the root folder.
First, install the plugin:
```
 pip install -e .
```

Then you can build the plugin with 
```
python setup.py install
```

To run the plugin and generate an normalized file with RELATIVEFREQUENCY type:

```
qiime normalization-plugin normalize-relativefrequency-function --i-
input-artifact data/qiime_table.qza --o-output-artifact data/output.qza
```

To run the plugin and generate an normalized file with FREQUENCY type:

```
qiime normalization-plugin normalize-frequency-function --i-input-artifact data/qiime_table.qza --o-output-artifact data/output.qza
```

Optionaly, if you want to use PQN_normalization  with RELATIVEFREQUENCY type:
```
qiime normalization-plugin PQN-normalize-relativefrequency-function --i-input-artifact data/qiime_table.qza --o-output-artifact data/output.qza
```

Optionaly, if you want to use PQN_normalization  with FREQUENCY type:
```
qiime normalization-plugin PQN-normalize-frequency-function --i-input-artifact data/qiime_table.qza --o-output-artifact data/output.qza
```
## Test


Now you should have a file output.qza in ./data

You need to unzip the output.qza file, and get a folder with a lot of numbers and letters.

Go to that folder and go to data folder in it, you should see a file names feature-table.biom.

Use this command to convert the biom file:
```
biom convert -i feature-table.biom -o feature-table.txt  --to-tsv
```



open feature-table.txt and check if it has been normalized.


## debug:
uninstall:
```
pip uninstall qiime2_normalization-plugin
```

## install from pip:
```
pip install git+https://github.com/pluckySquid/qiime2_normalization_plugin.git
```