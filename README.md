

## Build and run
If you have already build this plugin and what to update the plugin, run:
```
 qiime dev refresh-cache
```

Go to the roo folder.

Then you can build the plugin with 
```
python setup.py install
```

To run the plugin and generate an normalized file:

```
qiime normalization-plugin normalize-function   --i-input-artifact ../qiime2_dummy_plugin/data/test_otu_table.transpose.qza  --o-output-artifact data/output.qza
```

## Test


Now you should have a file output.qza in ./data

You need to unzip the output.qza file, and get a folder with a lot of numbers and letters.

Go to that folder and go to data folder in it.

Use this command to convert the biom file:
```
biom convert -i feature-table.biom -o feature-table.txt  --to-tsv
```

open feature-table.txt and check if it has been normalized.