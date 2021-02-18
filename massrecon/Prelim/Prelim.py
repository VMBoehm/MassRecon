"""preliminary dataset."""

import tensorflow_datasets as tfds
from astropy.io import fits
import json
import tensorflow as tf
import os
import numpy as np


_DESCRIPTION = """
'image': images size 128x128
"""

# TODO: BibTeX citation
_CITATION = """
"""


class prelim(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for preliminary dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Tensor(shape=(128,128,1),dtype=tf.float32),}),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,#('flux'),  # Set to `None` to disable
        homepage='',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
            "data_dir": '/home/nessa/Documents/codes/MassRecon/data/preliminary_maps/'
            },
        ),
    ]

  def _generate_examples(self, data_dir):

    for jj in range(1,1000):
        with tf.io.gfile.GFile(os.path.join(data_dir ,'k_%d.fits'%jj), mode='rb') as f:
            hdulist   = fits.open(f)
            im        = hdulist[0].data
            image     = np.expand_dims(im,-1).astype('float32')
            yield '%d'%int(jj), {'image': image}
            f.close()
